import os
import requests
from dotenv import load_dotenv

from langchain.tools import tool
from langchain_groq import ChatGroq
#from langchain_openai import ChatOpenAI
# from langgraph.prebuilt import create_react_agent
from langchain.agents import create_agent

# Load environment variables
load_dotenv()

#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# Initialize model
""" model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
) """
model = ChatGroq(
    #model="llama3-70b-8192",
    model="llama-3.3-70b-versatile",
    temperature=0
)

# WEATHER TOOL
@tool
def get_weather(city: str) -> str:
    """
    Get current weather information for a city.
    """

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

        response = requests.get(url)

        data = response.json()

        if response.status_code != 200:
            return f"Could not get weather for {city}"

        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]

        return f"The current temperature in {city} is {temp}°C with {description}."

    except Exception as e:
        return f"Weather tool error: {str(e)}"


# COUNTRY TOOL
@tool
def get_country_info(country: str) -> str:
    """
    Get information about a country.
    """

    try:
        url = f"https://restcountries.com/v3.1/name/{country}"

        response = requests.get(url)

        data = response.json()[0]

        capital = data.get("capital", ["Unknown"])[0]
        population = data.get("population", "Unknown")

        currencies = data.get("currencies", {})
        currency_names = list(currencies.keys())

        return (
            f"{country} has capital city {capital}. "
            f"Population is approximately {population}. "
            f"Currency: {', '.join(currency_names)}."
        )

    except Exception as e:
        return f"Country info error: {str(e)}"


# TOOLS LIST
tools = [get_weather, get_country_info]

# SYSTEM PROMPT
system_prompt = """
You are a helpful travel assistant.

Use the tools provided whenever necessary.

You help users:
- check weather
- learn about countries
- decide what to wear
- decide what to pack

Always give practical travel advice.
"""

# CREATE AGENT
graph = create_agent(
    model=model,
    tools=tools,
    system_prompt=system_prompt
)

# USER INPUT
while True:

    user_input = input("\nAsk me anything (type 'exit' to quit): ")

    if user_input.lower() == "exit":
        break

    for chunk in graph.stream(
        {"messages": [("user", user_input)]},
        stream_mode="values"
    ):

        message = chunk["messages"][-1]

        print("\n====================\n")

        if hasattr(message, "tool_calls") and message.tool_calls:
            print("TOOL CALL:")
            print(message.tool_calls)

        elif message.content:
            print("AGENT RESPONSE:")
            print(message.content)

# STREAM OUTPUT
for chunk in graph.stream(
    {"messages": [("user", user_input)]},
    stream_mode="values"
):

    message = chunk["messages"][-1]

    print("\n====================\n")

    if hasattr(message, "tool_calls") and message.tool_calls:
        print("TOOL CALL:")
        print(message.tool_calls)

    elif message.content:
        print("AGENT RESPONSE:")
        print(message.content)
# Travel Assistant Agent

An AI-powered travel assistant built with LangChain and LangGraph.

This assistant can:
- Check current weather conditions
- Provide country information
- Suggest what to wear
- Recommend what to pack for travel

The assistant uses external APIs and tool-calling capabilities to provide real-time responses.

---

# Features

## Weather Checker
Gets real-time weather information for any city using the OpenWeatherMap API.

Example:

```text
What should I wear in Lagos today?
```

---

## Country Information Tool
Provides useful information about countries including:
- capital city
- population
- currency

Example:

```text
Tell me about Bahamas.
```

---

## Travel Recommendations
The assistant combines weather data and country information to provide:
- clothing suggestions
- travel preparation tips
- packing recommendations

---

# Technologies Used

- Python
- LangChain
- LangGraph
- Groq LLM
- OpenWeatherMap API
- REST Countries API
- python-dotenv

---

# APIs Used

## OpenWeatherMap API
Used for fetching current weather information.

Website:
https://openweathermap.org/api

---

## REST Countries API
Used for fetching country information.

Website:
https://restcountries.com/

---

## Groq API
Used as the Large Language Model provider.

Website:
https://console.groq.com/

---

# Project Structure

```text
homework1-travel-agent/
│
├── venv/
├── main.py
├── .env
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Setup Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/osfolaranmi/travelAgent.git
```

---

## 2. Open the Project

Open the project folder in VS Code.

---

## 3. Create Virtual Environment

```bash
py -m venv venv
```

Activate virtual environment:

### PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root folder.

Add the following:

```env
GROQ_API_KEY=your_groq_api_key
WEATHER_API_KEY=your_weather_api_key
```

---

# Run the Application

```bash
py main.py
```

---

# Example Prompts

```text
What should I wear in Lagos today?
```

```text
Tell me about Bahamas and what I should pack.
```

```text
What is the weather in Tokyo?
```

---

# Streaming Output

The application streams:
- tool calls
- tool outputs
- final AI responses

This helps users inspect agent reasoning and execution flow.

---

# Other Features Implemented

- Multiple custom tools
- External API integration
- Conversational interaction
- Error handling
- Streaming responses

---

# Author

Oluwatosin Folaranmi — Agentic AI Bootcamp

<img width="1277" height="755" alt="Screenshot1" src="https://github.com/user-attachments/assets/847c4a27-433c-4ccb-a26f-a81b337fff66" />
<img width="1705" height="844" alt="Screenshot2" src="https://github.com/user-attachments/assets/c4236fd8-f99d-4d7f-862d-cc1801ea9e07" />
<img width="1706" height="941" alt="Screenshot3" src="https://github.com/user-attachments/assets/8c6d8d92-8d02-4a7b-993c-9a148c6f9624" />

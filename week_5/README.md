# University Student Services AI Agent

## Overview

This project implements an AI-powered University Student Services Assistant using Retrieval-Augmented Generation (RAG), Chroma Vector Database, LangGraph workflows, Ollama, and OpenWeatherMap.

The assistant answers student questions using university knowledge documents while preventing hallucinations by grounding responses in retrieved evidence.

In addition, the agent supports:

* Conversational Memory (Bonus Challenge 1)
* Multi-Source Routing (Bonus Challenge 2)

  * University Knowledge Base (RAG)
  * Weather Tool (OpenWeatherMap)
  * Web Search Tool

---

# Architecture

```text
START
  |
Route Question
  |
+---------------------------------------+
|            |            |             |
|            |            |             |
Knowledge   Weather      Web         General
|            |            |             |
Retrieve     Weather      Search      LLM
Documents    Tool         Tool        Answer
|            |            |             |
Generate     Generate     Generate    Generate
Answer       Answer       Answer      Answer
 \             |            |          /
  \            |            |         /
           Review Node
                |
          Memory Node
                |
               END
```

---

# Technologies Used

* Python
* LangChain
* LangGraph
* ChromaDB
* HuggingFace Embeddings
* Ollama (Llama 3)
* OpenWeatherMap API
* DuckDuckGo Search
* RecursiveCharacterTextSplitter

---

# Knowledge Sources

The assistant uses the following university documents:

1. Campus Services Guide
2. Career Services FAQ
3. Course Registration Guide
4. Financial Aid Guide
5. Housing FAQ
6. International Student Handbook
7. Student Handbook
8. Tuition Guide

---

# Features

## Document Loading

Loads all university knowledge documents into LangChain Document objects.

---

## Document Chunking

Uses RecursiveCharacterTextSplitter.

```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
```

---

## Embeddings

Uses HuggingFace sentence transformers.

```python
HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
```

---

## Vector Database

Uses ChromaDB for semantic search.

```python
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./student_service_db"
)
```

---

## Retriever

```python
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)
```

---

## Conditional Routing

The router classifies incoming questions into one of four categories:

* knowledge
* general
* weather
* web

Examples:

### Knowledge

* What GPA is required for graduation?
* What is the tuition refund policy?
* Where can I get IT support?

### General

* Tell me a joke
* Explain machine learning

### Weather

* What is the weather in Lagos?
* Will it rain tomorrow in Abuja?

### Web Search

* Who won the last FIFA World Cup?
* Latest AI news



---

# Review Node

All generated responses pass through a review node before final delivery.

This ensures:

* Response validation
* Consistent output formatting
* Improved answer quality

---

# Bonus Challenge 1 - Conversational Memory

Implemented using LangGraph MemorySaver.

```python
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()

workflow = graph.compile(
    checkpointer=memory
)
```

Memory is maintained using thread IDs:

```python
config = {
    "configurable": {
        "thread_id": "student_demo"
    }
}
```

This allows the assistant to answer follow-up questions using previous conversation context.

Example:

User:
"What GPA is required for graduation?"

User:
"What happens if it falls below that?"

The assistant correctly understands that "that" refers to GPA.

---

# Bonus Challenge 2 - Multi-Source Agent

Implemented using conditional routing.

Supported sources:

### University Documents

Uses Chroma vector search and RAG.

### Weather Tool

Uses OpenWeatherMap API.

```python
https://api.openweathermap.org/data/2.5/weather
```

### Web Search Tool

Uses DuckDuckGo Search.

This allows the assistant to dynamically select the most appropriate information source.

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/osfolaranmi/AgenticAIBootcamp/tree/master/week_5
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
OPENWEATHER_API_KEY=YOUR_API_KEY
```

---

## Install Ollama

Download:

https://ollama.com

Pull model:

```bash
ollama pull llama3
```

Verify:

```bash
ollama run llama3
```

---

# Running the Application

Open the Jupyter Notebook and execute all cells in sequence.

---

# Example Questions

## Knowledge

```text
What GPA is required for graduation?
```

```text
What is the attendance policy?
```

```text
What is the tuition refund policy?
```

---

## Weather

```text
What is the weather in Lagos?
```

```text
Will it rain tomorrow in Abuja?
```

---

## Web Search

```text
Who won the last FIFA World Cup?
```

```text
Latest AI developments
```

---

## General

```text
Tell me a joke
```

```text
Explain machine learning
```

---

# Project Structure

```text
project/
│
├── knowledge_documents/
│   ├── student_handbook.txt
│   ├── financial_aid_guide.txt
│   └── campus_services_guide.txt
│
├── student_service_db/
│
├── University_Student_Service_Agent.ipynb
│
├── README.md
│
├── requirements.txt
│
└── .env
```

---

# AI Usage Acknowledgement

AI assistance was used during development for:

* Architecture design guidance
* RAG pipeline design
* Debugging support
* Documentation generation


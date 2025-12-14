# Multi-Modal Travel Assistant

## Overview

This project is a Multi-Modal Travel Assistant built as part of an AI/ML engineering assignment.  
The goal of the project is to demonstrate agent-based orchestration using LangGraph, along with structured state handling and tool routing — without relying on external or paid APIs.

The application allows a user to enter a city name and receive:

- A short city summary
- A 5-day temperature forecast
- Representative city images

All data sources are mocked, as required by the assignment brief.

---

## Problem Statement

Design an AI-style system that:

- Uses an agent architecture rather than linear function calls
- Routes between different tools based on input
- Combines multiple modalities (text, numerical data, images)
- Works without external APIs
- Maintains structured state throughout execution

---

## High-Level Architecture

The system follows a graph-based execution model using LangGraph.

### Flow:

1. User enters a city name in the UI
2. The agent routes the request:
   - Known cities → vector store lookup
   - Unknown cities → mock web search
3. Weather and image tools are executed
4. Results are aggregated into a shared state
5. Final state is rendered in the UI

LangGraph manages node execution, routing logic, and state propagation.

---

## Tech Stack

- Python
- LangGraph
- LangChain (Chroma vector store)
- Streamlit (UI)
- Matplotlib (weather visualization)
- FakeEmbeddings (for vector store without APIs)

---

## Project Structure

MULTIMODAL_TRAVEL_AGENT/
├── app.py # Streamlit frontend
├── graph.py # LangGraph definition and routing
├── state.py # Agent state schema
├── generate_graph.py # Graph export utility
├── graph.md # Text-based graph representation
├── tools/
│ ├── weather.py # Mock weather data
│ ├── images.py # Mock image search
│ └── search.py # Mock web search
├── vectorstore/
│ ├── seed.py # Vector DB initialization
│ └── db/ # Chroma persistence
└── README.md

---

## Use of LangGraph

LangGraph is used to model the system as a stateful agent graph rather than a sequential pipeline.

Key aspects:

- Nodes represent logical steps (routing, vector search, weather, images)
- Conditional routing determines execution path
- A shared `AgentState` object is passed and updated across nodes
- The graph is compiled and invoked as a single agent

This approach allows clear separation of concerns and easy extensibility.

---

## Mock APIs and No External Services

As per the assignment constraints, no external APIs are used.

Instead:

- Weather data is returned from a deterministic mock function
- Image URLs are static placeholders
- City summaries are either vector-retrieved or mock-searched

These mocks simulate real API behavior while keeping the project self-contained and reproducible.

---

## JSON and Structured Data Handling

Although no standalone `.json` files are required, the system heavily relies on JSON-style structured data:

- Tool outputs return dictionaries and lists
- Weather forecasts are structured as lists of daily values
- LangGraph internally serializes and passes state in JSON-compatible formats

This satisfies the assignment requirement for JSON-based data handling.

---

## Weather Visualization Design

The weather forecast is displayed using a simple, user-friendly graph:

- Y-axis represents temperature in °C
- X-axis represents day progression (Today → Next days)
- Optional annotations display temperature values directly

The design prioritizes clarity for non-technical users.

---

## How to Run the Project

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python vectorstore/seed.py
streamlit run app.py
```

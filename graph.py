from langgraph.graph import StateGraph
from state import AgentState
from langchain_chroma import Chroma

from tools.weather import get_weather
from tools.images import get_images
from tools.search import web_search

# Load vector store
db = Chroma(persist_directory="vectorstore/db")

KNOWN_CITIES = {"Tokyo", "Paris", "New York"}

# -------------------------
# Router DECISION FUNCTION
# (used only for conditional edges)
# -------------------------
def route_decision(state: AgentState) -> str:
    city = state.city.strip().title()
    return "vector" if city in KNOWN_CITIES else "web"

# -------------------------
# Router NODE
# (must return state, NOT a string)
# -------------------------
def router_node(state: AgentState):
    return state

def vector_node(state: AgentState):
    # Vector DB confirms city is known,
    # but summary text comes from deterministic web mock
    state.city_summary = web_search(state.city)
    return state


def web_node(state: AgentState):
    state.city_summary = web_search(state.city)
    return state

def weather_node(state: AgentState):
    state.weather_forecast = get_weather(state.city)
    return state

def image_node(state: AgentState):
    state.image_urls = get_images(state.city)
    return state

# -------------------------
# Build LangGraph
# -------------------------
graph = StateGraph(AgentState)

graph.add_node("router", router_node)
graph.add_node("vector", vector_node)
graph.add_node("web", web_node)
graph.add_node("weather", weather_node)
graph.add_node("images", image_node)

graph.set_entry_point("router")

graph.add_conditional_edges(
    "router",
    route_decision,
    {
        "vector": "vector",
        "web": "web"
    }
)

graph.add_edge("vector", "weather")
graph.add_edge("web", "weather")
graph.add_edge("weather", "images")

graph.set_finish_point("images")

app_graph = graph.compile()

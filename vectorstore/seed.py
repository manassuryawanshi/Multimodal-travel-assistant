from langchain_chroma import Chroma

cities = {
    "Tokyo": "Tokyo is Japan's capital, known for technology, culture, and temples.",
    "Paris": "Paris is the capital of France, famous for art, fashion, and Eiffel Tower.",
    "New York": "New York is a major US city, known for finance, Broadway, and skyline."
}

db = Chroma(persist_directory="vectorstore/db")

for city, text in cities.items():
    db.add_texts([text], metadatas=[{"city": city}])

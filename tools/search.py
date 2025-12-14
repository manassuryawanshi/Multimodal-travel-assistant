def web_search(city: str) -> str:
    city = city.strip().title()

    return (
        f"{city} is a globally renowned city known for its history, culture, "
        f"architecture, and tourism. It attracts millions of visitors each year "
        f"and plays an important role in its country's economy and heritage."
    )

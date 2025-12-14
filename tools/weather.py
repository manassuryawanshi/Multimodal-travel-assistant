import time

def get_weather(city: str):
    days = ["Today", "Tomorrow", "Day 3", "Day 4", "Day 5"]
    temperatures = [25, 27, 26, 24, 23]  # example values

    return {
        "days": days,
        "temperatures": temperatures,
        "summary": (
            f"Expected temperature will range between "
            f"{min(temperatures)}°C and {max(temperatures)}°C "
            f"over the next 5 days."
        )
    }

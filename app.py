import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from graph import app_graph
from state import AgentState

st.set_page_config(page_title="Multi-Modal Travel Assistant", layout="centered")

st.title("Multi-Modal Travel Assistant")
st.write("Enter a city name to get summary, weather, and images.")

city = st.text_input("City name")

if st.button("Search") and city:
    try:
        state = AgentState(city=city)
        result = app_graph.invoke(state)

        # Result is a DICT, not AgentState
        st.subheader("City Summary")
        st.write(result["city_summary"])

        if result.get("weather_forecast"):
            st.subheader("Weather Forecast")

            weather = result["weather_forecast"]

            days = ["Today", "Tomorrow", "Day 3", "Day 4", "Day 5"]
            temps = weather["temperatures"]

            st.caption("Expected temperature trend over the next 5 days")

            st.info(
                f"Expected temperature will range between "
                f"{min(temps)}°C and {max(temps)}°C."
            )

            # Create DataFrame
            df = pd.DataFrame({
                "Day": days,
                "Temperature (°C)": temps
            })

            # Create matplotlib figure
            fig, ax = plt.subplots(figsize=(7, 4))

            # Line chart
            ax.plot(
                df["Day"],
                df["Temperature (°C)"],
                marker="o",
                linewidth=2
            )

            # Add °C labels above each point
            for day, temp in zip(days, temps):
                ax.text(
                    day,
                    temp + 0.4,
                    f"{temp}°C",
                    ha="center",
                    fontsize=9
                )

            # Axis labels (UX clarity)
            ax.set_xlabel("Day")
            ax.set_ylabel("Temperature (°C)")
            ax.set_title("5-Day Temperature Forecast")

            ax.grid(True, linestyle="--", alpha=0.4)

            st.pyplot(fig)





        if result.get("image_urls"):
            st.subheader("Images")
            for img in result["image_urls"]:
                st.image(img, width=600)

    except Exception as e:
        st.error(str(e))

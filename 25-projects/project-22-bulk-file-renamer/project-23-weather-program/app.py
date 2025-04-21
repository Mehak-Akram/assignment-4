import streamlit as st
import requests

# OpenWeatherMap API settings
API_KEY = "ac3cd5575f5a2f600c8b09c335a11baf"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Custom CSS for blue & white theme
def set_custom_theme():
    st.markdown("""
        <style>
        .main {
            background-color: #e6f0ff;
            color: #003366;
        }
        .stTextInput>div>div>input {
            border: 2px solid #003366;
        }
        .stButton>button {
            background-color: #007acc;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
        }
        .stButton>button:hover {
            background-color: #005c99;
        }
        .weather-card {
            color: #007acc;
            padding: 1.5rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_html=True)

# Function to fetch weather data
def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] != 200:
            return None, data['message']
        else:
            weather_info = {
                'city': data["name"],
                'country': data["sys"]["country"],
                'temp': data["main"]["temp"],
                'description': data["weather"][0]["description"].capitalize(),
                'humidity': data["main"]["humidity"],
                'wind_speed': data["wind"]["speed"]
            }
            return weather_info, None

    except requests.exceptions.RequestException as e:
        return None, str(e)

# Streamlit App
def main():
    set_custom_theme()

    st.title("🌤️ Weather Forecast App")
    st.markdown("### Enter a city to get the latest weather information.")

    city_name = st.text_input("City Name", placeholder="e.g. Karachi")

    if st.button("Get Weather"):
        if city_name.strip() == "":
            st.warning("Please enter a city name.")
        else:
            with st.spinner("Fetching weather data..."):
                weather, error = get_weather(city_name)
                if error:
                    st.error(f"Error: {error}")
                else:
                    st.markdown(f"## 📍 Weather in {weather['city']}, {weather['country']}")

                    with st.container():
                        st.markdown(f"""
                            <div class="weather-card">
                                <h3>🌡️ Temperature: {weather['temp']}°C</h3>
                                <p>☁️ <b>{weather['description']}</b></p>
                                <p>💧 Humidity: {weather['humidity']}%</p>
                                <p>💨 Wind Speed: {weather['wind_speed']} m/s</p>
                            </div>
                        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

    st.markdown("""
        <hr style="border: 1px solid #007acc; margin-top: 3rem; margin-bottom: 1rem;">
        <div style='text-align: center; color: white; font-size: 1rem;'>
             Developed with 💙 by Mehak Akram | © 2025 🚀
        </div>
    """, unsafe_allow_html=True)
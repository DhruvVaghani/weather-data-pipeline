import requests
api_key = "83e48ac3e3723a5e4d237b8b680e6633"
api_url = "http://api.weatherstack.com/current?access_key=83e48ac3e3723a5e4d237b8b680e6633&query=New York"

def fetch_data():
    response = requests.get(api_url)
    return(response.json())



def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-07-13 17:35', 'localtime_epoch': 1752428100, 'utc_offset': '-4.0'}, 'current': {'observation_time': '09:35 PM', 'temperature': 27, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0002_sunny_intervals.png'], 'weather_descriptions': ['Partly cloudy'], 'astro': {'sunrise': '05:37 AM', 'sunset': '08:27 PM', 'moonrise': '10:28 PM', 'moonset': '08:19 AM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 95}, 'air_quality': {'co': '310.8', 'no2': '38.295', 'o3': '55', 'so2': '7.4', 'pm2_5': '16.835', 'pm10': '20.905', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 17, 'wind_degree': 155, 'wind_dir': 'SSE', 'pressure': 1018, 'precip': 0, 'humidity': 65, 'cloudcover': 75, 'feelslike': 29, 'uv_index': 3, 'visibility': 16, 'is_day': 'yes'}}
from fastapi import FastAPI
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test")
def test_run():
    url = "https://api.openweathermap.org/data/2.5/weather?lat=42.3314&lon=83.0458&appid={API_KEY}"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat=42.3314&lon=-83.0458&appid={API_KEY}&units=metric"

    trial = requests.get(url).json()
    #getting the current weather description
    current = trial["weather"]
    weather = current[0]["description"]
    #creating function to get the current temperature
    temperature = trial["main"]
    temp = temperature["temp"]
    feelings = temperature["feels_like"]
    humidity = temperature["humidity"]
    
    return {'current weather is: ': weather, 'temperature is: ': temp, 'feelings is: ': feelings, 'Humidity is: ': humidity}


import requests

API_KEY = "01866adc84874fe6ebead6f9f15ed0a2"
CITY = "Bangalore"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    print("Current Temperature:", data['main']['temp'], "°C")
    print("Weather Condition:", data['weather'][0]['description'])
else:
    print("Error:", data["message"])

import requests

api_key = "55c8bfaf9fff464f3bf6f3c283186dc6"

user_input = input("Enter the city: ")


weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

# https://api.openweathermap.org/data/2.5/weather?q=${city},${country}&appid=${apiId}
# api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=55c8bfaf9fff464f3bf6f3c283186dc6

print(weather_data.json())
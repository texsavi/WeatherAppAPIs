import requests, json


timezone = "EAT"
latitude = -1.175389
longitude = 36.817223

result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

user = result.json()

weathercode = user["daily"]["weathercode"][0]
temp_max = user["daily"]["temperature_2m_max"][0]
temp_min = user["daily"]["temperature_2m_min"][0]

# Interpret weathercode
if weathercode == 0:
  print("\033[32mClear sky\033[0m")
elif weathercode == 1 or weathercode == 2 or weathercode == 3:
  print("\033m[1;33mMainly clear, partly cloudy, and overcast\033[0m")
else:
  print("Error Identifying Weather")

print(f"\033[91mThe maximum temperature for today is: {temp_max}°C\033[0m")
#print("\033[91mRed Text\033[0m")

print(f"\033[34mThe minimum temperature for today is: {temp_min}°C\033[0m")

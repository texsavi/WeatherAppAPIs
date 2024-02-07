import requests, json
timezone = "EAT"
latitude = -1.175389
longitude = 36.817223

result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

user = result.json()

weathercode = user["daily"]["weathercode"][0]
temp_max = user["daily"]["temperature_2m_max"][0]
temp_min = user["daily"]["temperature_2m_min"][0]

#interpret weathercode
if weathercode == 0:
  print("\033[32mClear sky\033[0m\n\n")
elif weathercode == 1 or weathercode == 2 or weathercode == 3:
  print("\033[1;33mMainly clear, partly cloudy, and overcast\033[0m\n\n")
else:
  print("Error Identifying Weather")

print(f"Maximum temperature today: \033[1;31m{temp_max}°C\033[0m")

print(f"Minimum temperature today: \033[1;34m{temp_min}°C\033[0m")
#except Exception as {e}:
  #  print("Error Identifying Weather: ", e)

#print(json.dumps(user, indent=2))
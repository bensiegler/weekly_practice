import requests, sys, json

api_key = "3fa700bbbc80f981e69b05b67cf5b8eb"

city_name = "Chicago"
print(city_name)
geo_loc = requests.get("http://api.openweathermap.org/geo/1.0/direct", {"q": city_name, "limit": 5, "appid": api_key})

print("these are the possible locations found for your query: \n")

for i in range(5):
    curr = geo_loc.json()[i]
    print(i + 1, ":", curr["name"], curr["state"], curr["country"])

loc_choice = int(input("which location would you like to use? ")) - 1

lat = geo_loc.json()[loc_choice]["lat"]
lon = geo_loc.json()[loc_choice]["lon"]


response = requests.get("https://api.openweathermap.org/data/3.0/onecall", {"lat": lat, "lon": lon})
print(response.json())

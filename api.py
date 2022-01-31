import requests

name = "den"

params = {
        "name": name,
    }
response_nation = requests.get(f"https://api.nationalize.io", params=params)
response_nation.raise_for_status()
nation = response_nation.json()["country"][0]["country_id"]

print(nation)
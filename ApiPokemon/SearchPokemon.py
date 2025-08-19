import requests 

url = "https://api.pokemontcg.io/v2/cards/pl1-1"

response = requests.get(url)

print(response)

pokemon = response.json()
pokemon_name = pokemon['data']['resistances'][0]['value']
print(pokemon_name)
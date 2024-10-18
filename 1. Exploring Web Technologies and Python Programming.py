import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {pokemon_name}")
        return None

def print_pokemon_data(pokemon_data):
    name = pokemon_data['name']
    abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
    print(f"Name: {name}")
    print(f"Abilities: {', '.join(abilities)}\n")

def calculate_average_weight(pokemon_list):
    total_weight = sum([pokemon['weight'] for pokemon in pokemon_list])
    return total_weight / len(pokemon_list) if pokemon_list else 0

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

pokemon_list = []
for name in pokemon_names:
    data = fetch_pokemon_data(name)
    if data:
        pokemon_list.append(data)
        print_pokemon_data(data)

average_weight = calculate_average_weight(pokemon_list)
print(f"Average Weight: {average_weight}")
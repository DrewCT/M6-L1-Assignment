import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)

    if response.status_code == 200:
        planets = response.json()['bodies']
        return [planet for planet in planets if planet['isPlanet']]
    else:
        print(f"Error fetching data: {response.status_code}")
        return []

def display_planet_info(planets):
    for planet in planets:
        name = planet.get('englishName', 'Unknown')
        mass = planet['mass']['massValue'] if planet.get('mass') else 'N/A'
        orbit_period = planet.get('sideralOrbit', 'N/A')
        print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

def find_heaviest_planet(planets):
    heaviest_planet = None
    max_mass = 0

    for planet in planets:
        if planet.get('mass'):
            mass_value = planet['mass']['massValue']
            mass_exponent = planet['mass']['massExponent']
            actual_mass = mass_value * (10 ** mass_exponent)

            if actual_mass > max_mass:
                max_mass = actual_mass
                heaviest_planet = planet

    if heaviest_planet:
        return heaviest_planet['englishName'], max_mass
    else:
        return "Unknown", 0

def main():
    print("Fetching data about planets...\n")
    
    planets = fetch_planet_data()

    if planets:
        print("Planet Information:\n")
        display_planet_info(planets)

        name, mass = find_heaviest_planet(planets)
        print(f"\nThe heaviest planet is {name} with a mass of {mass} kg.")
    else:
        print("No planets data found.")

if __name__ == "__main__":
    main()
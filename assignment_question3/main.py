import requests
import json
import pandas as pd

# Function to download data from the URL
def download_data(url):
    response = requests.get(url)
    data = response.json()
    return data

# Function to convert data to properly structured format
def convert_data(data):
    # Extracting the required attributes from the data
    pokemon_data = []
    for pokemon in data['pokemon']:
        pokemon_info = {
            'id': pokemon['id'],
            'num': pokemon['num'],
            'name': pokemon['name'],
            'img': pokemon['img'],
            'type': ', '.join(pokemon['type']),
            'height': pokemon['height'],
            'weight': pokemon['weight'],
            'candy': pokemon.get('candy', ''),
            'candy_count': pokemon.get('candy_count', ''),
            'egg': pokemon.get('egg', ''),
            'spawn_chance': pokemon.get('spawn_chance', ''),
            'avg_spawns': pokemon.get('avg_spawns', ''),
            'spawn_time': pokemon.get('spawn_time', ''),
            'weakness': ', '.join(pokemon['weaknesses'])
        }
        pokemon_data.append(pokemon_info)
    
    return pokemon_data

# Function to save data in Excel format
def save_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

# Main function to execute the program
def main():
    url = 'https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json'
    filename = 'pokemon_data.xlsx'

    # Download data from the provided URL
    data = download_data(url)

    # Convert data to properly structured format
    converted_data = convert_data(data)

    # Save data in Excel format
    save_to_excel(converted_data, filename)
    print(f"Data saved in '{filename}'")

# Run the program
if __name__ == '__main__':
    main()

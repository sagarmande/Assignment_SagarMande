import requests
import json
import csv

def download_data(url):
    response = requests.get(url)
    data = response.json()
    return data

def process_data(data):
    processed_data = []
    for item in data:
        processed_item = {
            'Name of Earth Meteorite': item['name'],
            'id': item['id'],
            'nametype': item['nametype'],
            'recclass': item['recclass'],
            'mass (g)': item.get('mass (g)', None),  # Handle missing attribute
            'year': item.get('year', None),  # Handle missing attribute
            'reclat': item.get('reclat', None),  # Handle missing attribute
            'reclong': item.get('reclong', None),  # Handle missing attribute
            'point coordinates': item['geolocation']['coordinates']
        }
        processed_data.append(processed_item)
    return processed_data

def save_as_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

# URL for the data
url = 'https://data.nasa.gov/resource/y77d-th95.json'

# Download the data
data = download_data(url)

# Process the data
processed_data = process_data(data)

# Save as CSV file
filename = 'meteorite_data.csv'
save_as_csv(processed_data, filename)

print(f"Data downloaded and saved as '{filename}' successfully!")
import requests
import json
import csv

def download_data(url):
    response = requests.get(url)
    data = response.json()
    return data

def process_data(data):
    processed_data = []
    for item in data:
        geolocation = item.get('geolocation', {})
        coordinates = geolocation.get('coordinates', None)
        
        processed_item = {
            'Name of Earth Meteorite': item['name'],
            'id': item['id'],
            'nametype': item['nametype'],
            'recclass': item['recclass'],
            'mass (g)': item.get('mass (g)', None),  # Handle missing attribute
            'year': item.get('year', None),  # Handle missing attribute
            'reclat': item.get('reclat', None),  # Handle missing attribute
            'reclong': item.get('reclong', None),  # Handle missing attribute
            'point coordinates': coordinates
        }
        processed_data.append(processed_item)
    return processed_data

def save_as_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

# URL for the data
url = 'https://data.nasa.gov/resource/y77d-th95.json'

# Download the data
data = download_data(url)

# Process the data
processed_data = process_data(data)

# Save as CSV file
filename = 'meteorite_data.csv'
save_as_csv(processed_data, filename)

print(f"Data downloaded and saved as '{filename}' successfully!")

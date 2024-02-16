import requests
import matplotlib.pyplot as plt

# NASA API Key
NASA_API_KEY = 'zOpGoqJdp9tjkydekW65khLKjcx866FQyrV9BJKB'

# NEO API endpoint
NEO_API_URL = f'https://api.nasa.gov/neo/rest/v1/feed/today?api_key={NASA_API_KEY}'

# Function to fetch NEO data
def fetch_neo_data():
    response = requests.get(NEO_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return None

# Function to parse data and generate graph
def generate_distance_graph(data):
    distances = []
    names = []
    for date in data['near_earth_objects']:
        for neo in data['near_earth_objects'][date]:
            distances.append(float(neo['close_approach_data'][0]['miss_distance']['kilometers']))
            names.append(neo['name'])
    
    plt.figure(figsize=(10, 6))
    plt.barh(names, distances, color='skyblue')
    plt.xlabel('Distance from Earth (km)')
    plt.ylabel('Near Earth Object')
    plt.title('Distance of Near Earth Objects from Earth')
    plt.gca().invert_yaxis()  # Invert y-axis to display the closest objects on top
    plt.tight_layout()
    plt.show()

# Main function
def main():
    neo_data = fetch_neo_data()
    if neo_data:
        generate_distance_graph(neo_data)

if __name__ == "__main__":
    main()

import requests
import concurrent.futures

def get_weather(city):
    url = f'https://api.open-meteo.com/v1/forecast?latitude={city["latitude"]}&longitude={city["longitude"]}&hourly=temperature_2m'
    response = requests.get(url)
    data = response.json()
    temperatures = data['hourly']['temperature_2m']
    return city["name"], max(temperatures), sum(temperatures) / len(temperatures)

def main():
    cities = [
        {"name": "Kyiv", "latitude": 50.4501, "longitude": 30.5234},
        {"name": "Krakow", "latitude": 50.0647, "longitude": 19.9450},
        {"name": "Tokyo", "latitude": 35.6895, "longitude": 139.6917},
        {"name": "Vyshhorod", "latitude": 50.5844, "longitude": 30.4710},
        {"name": "Warsaw", "latitude": 52.5200, "longitude": 21.0357}
    ]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(get_weather, city) for city in cities]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]

    hottest_city = max(results, key=lambda x: x[1])
    average_temperature = sum(r[2] for r in results) / len(cities)

    print("Найспекотніше місто зараз:", f"{hottest_city[0]} ({hottest_city[1]:.2f}°C)")
    print("Середня температура у містах:")
    for city in results:
        print(f"{city[0]}: {city[2]:.2f}°C")

    print(f"\nСередня температура по всім містам: {average_temperature:.0f}°C")

if __name__ == "__main__":
    main()

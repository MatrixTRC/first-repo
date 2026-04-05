"""Fetch and print real-time weather data for a city using Open-Meteo APIs."""

from urllib import error, parse, request
import json
import time


GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def _get_json(url, params, retries=3, backoff=1.0):
    """Make a GET request and return decoded JSON data, retrying on transient failures."""
    query_string = parse.urlencode(params)
    full_url = f"{url}?{query_string}"

    last_exc = None
    for attempt in range(retries):
        try:
            with request.urlopen(full_url, timeout=10) as response:
                if response.status != 200:
                    raise RuntimeError(f"API request failed with status {response.status}")
                return json.loads(response.read().decode("utf-8"))
        except (error.URLError, RuntimeError) as exc:
            last_exc = exc
            if attempt < retries - 1:
                time.sleep(backoff * (2 ** attempt))
    raise last_exc


def _normalize_unit(unit):
    normalized = unit.strip().lower()
    if normalized in {"celsius", "c", "metric"}:
        return "celsius", "C"
    if normalized in {"fahrenheit", "f", "imperial"}:
        return "fahrenheit", "F"
    raise ValueError("Unit must be Celsius/C or Fahrenheit/F")


def check_weather(city, unit="Celsius"):
    """Look up a city and print current weather conditions."""
    if not city or not city.strip():
        print("Please provide a city name.")
        return

    try:
        temperature_unit, unit_label = _normalize_unit(unit)

        geocode_data = _get_json(
            GEOCODE_URL,
            {
                "name": city.strip(),
                "count": 1,
                "language": "en",
                "format": "json",
            },
        )

        results = geocode_data.get("results", [])
        if not results:
            print(f"No matching city found for '{city.strip()}'.")
            return

        location = results[0]
        weather_data = _get_json(
            WEATHER_URL,
            {
                "latitude": location["latitude"],
                "longitude": location["longitude"],
                "current": "temperature_2m,wind_speed_10m",
                "temperature_unit": temperature_unit,
            },
        )

        current = weather_data.get("current", {})
        temperature = current.get("temperature_2m")
        wind_speed = current.get("wind_speed_10m")

        print(
            f"Current weather in {location['name']}, {location.get('country', 'Unknown')}:"
        )
        print(f"Temperature: {temperature}°{unit_label}")
        print(f"Wind speed: {wind_speed} km/h")

    except ValueError as exc:
        print(f"Input error: {exc}")
    except error.URLError as exc:
        print(f"Network error while contacting weather service: {exc}")
    except (KeyError, TypeError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"Could not fetch weather data: {exc}")


if __name__ == "__main__":
    city_name = input("Enter city name: ").strip()
    unit_name = input("Enter unit (Celsius/Fahrenheit): ").strip() or "Celsius"
    check_weather(city_name, unit_name)

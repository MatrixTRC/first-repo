# first-repo

A beginner Python repository used to demonstrate GitHub features and workflows. It contains two small, self-contained Python utilities:

| File | Purpose |
|---|---|
| `weather.py` | Fetch and display real-time weather for any city |
| `list_operations.py` | Utility function to find the largest number in a list |

---

## Repository Structure

```
first-repo/
├── weather.py          # Real-time weather fetcher (uses Open-Meteo APIs)
├── list_operations.py  # List utility: find the biggest number
├── LICENSE             # MIT License
└── README.md           # This file
```

---

## `weather.py` — Weather Checker

Fetches current temperature and wind speed for any city using the free
[Open-Meteo](https://open-meteo.com/) APIs (no API key required).

### Features
- Geocodes a city name to coordinates via the Open-Meteo Geocoding API.
- Retrieves current temperature and wind speed from the Open-Meteo Forecast API.
- Supports both **Celsius** and **Fahrenheit** (accepts `"C"`, `"Celsius"`, `"metric"` / `"F"`, `"Fahrenheit"`, `"imperial"`).
- Handles network errors, unknown cities, and invalid unit inputs gracefully.

### Requirements

- Python 3.x (standard library only — no third-party packages needed)

### Usage

Run interactively from the command line:

```bash
python weather.py
```

You will be prompted for:
1. **City name** — e.g. `London`, `New York`, `Tokyo`
2. **Unit** — `Celsius` (default) or `Fahrenheit`

**Example output:**
```
Enter city name: Paris
Enter unit (Celsius/Fahrenheit): Celsius
Current weather in Paris, France:
Temperature: 14.2°C
Wind speed: 18.5 km/h
```

You can also import and call `check_weather()` from your own code:

```python
from weather import check_weather

check_weather("Tokyo", unit="Fahrenheit")
```

---

## `list_operations.py` — List Utilities

Contains a single utility function for working with Python lists.

### `find_biggest_number_or_error(numbers)`

Returns the largest number in the provided list.  
Raises a `ValueError` if the list is empty.

```python
from list_operations import find_biggest_number_or_error

result = find_biggest_number_or_error([3, 1, 4, 1, 5, 9, 2, 6])
print(result)  # 9

find_biggest_number_or_error([])  # raises ValueError: The list is empty
```

---

## License

This project is licensed under the [MIT License](LICENSE).

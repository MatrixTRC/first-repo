def check_weather(city, unit):  # Defines a function that accepts a city and a temperature unit as parameters
    if city == "":  # Checks if no city name was provided
        print("please provide a city name.") # Displays a message asking the user to provide a city
        return # Stops the function if the city name is missing
  
    print("Checking weather for", city) # Displays a message indicating which city's weather is being checked
    
    print("Temperature unit selected:", unit)  # Displays the temperature unit that will be used
  
    print("Connecting to weather service...")  # Simulates connecting to a weather service

check_weather("Paris", "Celsius")  # Calls the function with "Paris" as city and "Celsius" as temperature unit

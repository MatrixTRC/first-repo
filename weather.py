def check_weather(city, unit):  
    if city == "":  
        print("please provide a city name.") 
        return 
  
    print("Checking weather for", city) 
    
    print("Temperature unit selected:", unit)  
  
    print("Connecting to weather service...")  

check_weather("Paris", "Celsius")  

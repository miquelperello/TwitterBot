
from tweepy import OAuthHandler, Stream, StreamListener, API
from PIL import Image 

import requests, json



api_weather = "6ba6eacb5c2c7f9036467585be821a39"

api_base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = "temps barcelona"
end = len(city_name)
city_name= city_name[6:end]
print(city_name)


complete_url = api_base_url + "appid=" + api_weather + "&q=" + city_name
response = requests.get(complete_url) 
x = response.json() 
if x["cod"] != "404": 

    # store the value of "main" 
    # key in variable y 
    y = x["main"] 
  
    # store the value corresponding 
    # to the "temp" key of y 
    current_temperature = y["temp"] 
    #print("t" + str(current_temperature))
  
    # store the value corresponding 
    # to the "pressure" key of y 
    current_pressure = y["pressure"] 
  
    # store the value corresponding 
    # to the "humidity" key of y 
    current_humidiy = y["humidity"] 
  
    # store the value of "weather" 
    # key in variable z 
    z = x["weather"] 
  
    # store the value corresponding  
    # to the "description" key at  
    # the 0th index of z 
    weather_description = z[0]["description"] 
  
    # print following values 
    
    print( " Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
          " atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          " humidity (in percentage) = " +
                    str(current_humidiy) +
          " description = " +
                    str(weather_description)) 
  
else: 
    print(" City Not Found ") 
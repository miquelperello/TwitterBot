# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 18:48:49 2020

@author: miquelperello
"""
from tweepy import OAuthHandler, Stream, StreamListener, API
from PIL import Image 
from googletrans import Translator

import requests, json


consumer_key=""
consumer_secret=""


access_token=""
access_token_secret=""

#TEMPS

api_weather = ""

api_base_url = "http://api.openweathermap.org/data/2.5/weather?"

translator = Translator()

class StdOutListener(StreamListener):
    
    def on_status(self, status):
       print (status.author.screen_name, status.created_at, status.text, status.id)
       author = status.author.screen_name
       text = status.text
       statID = status.id
       if "temps" in text:
       	end = len(text)
       	text= text[21:end]
       	respondtemps(statID, author, text)
       elif "imatge" in text:	
       	image = status.entities["media"][0]["media_url"]
       	converteiximatge(image)
       	respondimatge(statID, author)
       return True

    def on_error(self, status):
        print(status)

def converteiximatge(url): 
	image_file = Image.open(requests.get(url, stream=True).raw)
	image_file = image_file.convert('1') # convert image to black and white
	image_file.save("result.png")

def respondimatge(tweetid, author):
	filename = "result.png"
	api.update_with_media(filename, status = "Hey, @" +author , in_reply_to_status_id = tweetid)

def respondtemps(tweetid, author, text):
	city_name = text
	print (city_name)
	complete_url = api_base_url + "appid=" + api_weather + "&q=" + city_name
	response = requests.get(complete_url) 
	x = response.json() 

	if x["cod"] != "404": 

	    y = x["main"] 
	    current_temperature = y["temp"] 
	    current_pressure = y["pressure"] 
	    current_humidiy = y["humidity"] 
	    z = x["weather"] 
	    weather_description = z[0]["description"] 
	  
	    api.update_status("@" +author + " Temps de " +
	                    str(int(current_temperature) - 273) + 
	          "ºC. Pressió atmosfèrica de " +
	                    str(current_pressure) +
	          "hPa. Humitat =  " +
	                    str(current_humidiy) +
	          "%. " +
	                    translator.translate(str(weather_description), dest='ca').text, in_reply_to_status_id = tweetid) #ca -> catalan
	  
	else: 
	    api.update_status("@"+ author +" Sorry! City Not Found", in_reply_to_status_id = tweetid) 

	return True


l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

stream = Stream(auth, l)
stream.filter(track=['<@yourbot>'])

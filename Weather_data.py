import sys
import urllib2
import json
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = "03850e141206c03d3ffaf6e6288dfc66"

#get the city name
print("enter city name")
cityname = input()

#get temperature
def get_temperature():
    url = 'http://api.openweathermap.org/data/2.5/weather?q='+cityname+'&appid='+API_KEY
    response = urllib2.urlopen(url)
    data = json.load(response)
    temp_k = (float)(data['main']['temp'])
    temp_f = (temp_k -273.15) * 1.8 + 32
    return(temp_f)

temp = get_temperature()
print(temp)
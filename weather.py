
print("_______weather_______")

import requests

city = input("enter city to know weather:")
date = input("enter date in yyyy-mm-dd format:")

url=f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date}?key=MA5EM6XKSSNC22F458RBK7VVP"

r=requests.get(url)
print(r.text)
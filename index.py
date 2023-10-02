import urllib.parse
import requests

main_api = 'http://ip-api.com/json/?fields=status,message,country,regionName,city,isp,query'

json_data = requests.get(main_api).json()

print("Country: " + (json_data["country"]))
print("Region: " + (json_data["regionName"]))
print("City: " + (json_data["city"]))
print("ISP: " + (json_data["isp"]))
print("IP address: " + (json_data["query"]))
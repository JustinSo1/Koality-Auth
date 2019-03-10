import time
import re
import requests

ip_request = requests.get('https://get.geojs.io/v1/ip.json')
my_ip = ip_request.json()['ip']
print("Current ip is: " + str(my_ip))

geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
geo_request = requests.get(geo_request_url)
geo_data = geo_request.json()

initial_location = [geo_data['latitude'],geo_data['longitude']]

iTime = 0
i = 0
while True:
    try:
        ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        my_ip1 = ip_request.json()['ip']
    except:
        my_ip1 = my_ip
        if i == 0:
            iTime = time.time()
            i += 1
    
    if my_ip1 != my_ip:
        i = 0
        break

# measuring time difference
fTime = time.time()
td = fTime - iTime

my_ip = ip_request.json()['ip']
print("IP Changed to: " + str(my_ip))
geo_request = requests.get(geo_request_url)
geo_data = geo_request.json()
final_location = [geo_data['latitude'],geo_data['longitude']]

vpn = True
x = re.search("^([0-9]){1,3}[.]([0-9]){1,3}[.]([0-9]){1,3}[.]([0-9]){1,3}$", my_ip1)
if (x):
    vpn = False

if td < 200:
    print("Program verified changed IP. Location not changed. No action is required.")
else:
    if vpn == True:
        print("Location change detected. Please disconnect vpn and verify location.")
    else:
        if final_location == initial_location:
            print("Program verified changed IP. Location not changed. No action is required.")
        else:
            print("Location change detected. Please contact customer care to verify authenticity.")
            
    
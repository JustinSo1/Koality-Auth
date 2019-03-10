
import time
import cv2 as cv

cam = cv.VideoCapture(0)
time.sleep(5)
returnVal,image = cam.read()
cv.imwrite('opencv.jpg', image)
cam.release()
cv.destroyAllWindows()


import cognitive_face as CF

KEY = '2f4f336ad9c146f4b8d52926cba85498'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

img_url1 = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
img_url2 = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
result = CF.face.verify('50c3e52d-a679-4f16-9141-4672753efbfc','50c3e52d-a679-4f16-9141-4672753efbfc')
print(result)



import requests
ip_request = requests.get('https://get.geojs.io/v1/ip.json')
my_ip = ip_request.json()['ip']
print("Current ip is: " + str(my_ip))

while True:
    try:
        ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        my_ip1 = ip_request.json()['ip']
    except:
        my_ip1 = my_ip
    
    if my_ip1 != my_ip:
        break
    
my_ip = ip_request.json()['ip']
print("IP Changed to: " + str(my_ip))
    
    
    
    
geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
geo_request = requests.get(geo_request_url)
geo_data = geo_request.json()
#print(geo_data)

import re

x = re.search("^([0-9]){1,3}[.]([0-9]){1,3}[.]([0-9]){1,3}[.]([0-9]){1,3}$", my_ip1)
if (x):
    print("yes")
else:
    print("error")
    
    
    
    
    
import serial
from gps_class import gps


serGPS = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE, timeout=None,
                    xonxoff=False, rtscts=False,
                    writeTimeout=None, dsrdtr=False,
                    interCharTimeout=None)

gps_ser = gps(serGPS)
while(True):
    print(gps_ser.readGPS())
    
    
    
    
    
    
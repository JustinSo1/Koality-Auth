import time
import re
import requests
from tkinter import *
import time
import cv2 as cv
import cognitive_face as CF
KEY = 'ff9d9585fe5f4057bfa037f9f36adee5'  
CF.Key.set(KEY)
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  
CF.BaseUrl.set(BASE_URL)
img_url1 = 'polarbear1.jpg'
face1 = CF.face.detect(img_url1)[0]['faceId']

window = Tk()       

def clicked():
    cam = cv.VideoCapture(0)
    time.sleep(4)
    returnVal,image = cam.read()
    cv.imwrite('polarbear2.jpg', image)
    cam.release()
    cv.destroyAllWindows()
    img_url2 = 'polarbear2.jpg'
    face2 = CF.face.detect(img_url2)[0]['faceId']
    result = CF.face.verify(face1,face2)
    if result['isIdentical'] == True:
        lbl.configure(text="Verification successful! User Authenticated")
    else:
        lbl.configure(text="Verification failed! Please reauthenticate")
window.title("KoalityAuth")
window.geometry('550x100')

# label for status 
lbl1 = Label(window, text="Authentication: ")
lbl1.grid(column=1, row=1)

# label for displaying result
lbl = Label(window, text="Awaiting status")
lbl.grid(column=2, row=1)

# label for beauty
lblq = Label(window, text="| ")
lblq.grid(column=0, row=0)
lblw = Label(window, text="-------------------------")
lblw.grid(column=1, row=0)
lbly = Label(window, text="------------------------------------------------   |")
lbly.grid(column=2, row=0)
lble = Label(window, text="| ")
lble.grid(column=0, row=3)
lblr = Label(window, text="-------------------------")
lblr.grid(column=1, row=3)
lblt = Label(window, text="------------------------------------------------   |")
lblt.grid(column=2, row=3)

 
btn = Button(window, text="Authenticate", command=clicked)
btn.grid(column=1, row=2)

window.mainloop()
import os
import pyautogui

import pyautogui
import time
from PIL import ImageGrab,Image
import numpy as np
import time
import cv2
start=time.time_ns()
myList=[]
for x in range(1,21):
    # myscreenshot=pyautogui.screenshot(f"./vidImages/{x}.png")
    myscreenshot=ImageGrab.grab()
    myList.append(myscreenshot)
    # myscreenshot.save(f"./vidImages/{str(x)}.png")
end=time.time_ns()

seconds=(end-start)/(1000**3)
print(seconds,"seconds taken to record all frames")



fourcc=cv2.VideoWriter_fourcc('m','p','4','v')
captured_video=cv2.VideoWriter('output.mp4',fourcc,10.0,(1366,768))

# start=time.time_ns()
# for x in range(1,601):
#     af=pyautogui.grab("./vidImages/"+str(time.time_ns())+".png")
# end=time.time_ns()
# duration=(end-start)/(1000**3)
# print(duration)

for image in myList:
    # img=Image.open(f"./vidImages/{image}")
    img=np.array(image)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    captured_video.write(img)
end2=time.time_ns()

seconds2=(end2-end)/(1000**3)
print(seconds2,"seconds taken to save images to video")

import os
import pyautogui
import time
import numpy as np
from PIL import ImageGrab,Image
import time
import cv2

fourcc=cv2.VideoWriter_fourcc('m','p','4','v')
captured_video=cv2.VideoWriter('output.mp4',fourcc,10.0,(1366,768))

# start=time.time_ns()
# for x in range(1,601):
#     af=pyautogui.grab("./vidImages/"+str(time.time_ns())+".png")
# end=time.time_ns()
# duration=(end-start)/(1000**3)
# print(duration)
for image in os.listdir("./vidImages"):
    img=Image.open(f"./vidImages/{image}")
    img=np.array(img)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    captured_video.write(img)

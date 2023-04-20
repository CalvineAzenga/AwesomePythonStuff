import time
from PIL import ImageGrab
import numpy as np
import time
import cv2

start=time.time_ns()

fourcc=cv2.VideoWriter_fourcc('m','p','4','v')
captured_video=cv2.VideoWriter('output.mp4',fourcc,20.0,(1366,768))
for x in range(1,100):
    myscreenshot=ImageGrab.grab(include_layered_windows=1,all_screens=1)
    img=np.array(myscreenshot)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    captured_video.write(img)


end=time.time_ns()
seconds=(end-start)/(1000**3)
print(seconds,"seconds taken to record all frames")


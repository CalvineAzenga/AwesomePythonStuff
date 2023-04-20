from PIL import ImageFilter, ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime
import time
from PIL import Image,ImageTk,ImageDraw,ImageOps


def circulateImage(image, size):
            mask = Image.new('L', size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + size, fill=255)
            im=image
            im = im.resize(size, Image.ANTIALIAS)
            output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
            output.putalpha(mask)
            return output
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

STOP=False
time_stamp=None
filename=None
fourcc = None
captured_video = None
def releaseVideo():
    global STOP
    STOP=True
    captured_video.release()
    cv2.destroyAllWindows()
    
def record(hey,root,lbl):
    global time_stamp,filename,captured_video,STOP
    STOP=False
    time_stamp=datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    filename=f'./saves/{time_stamp}.mp4'

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    captured_video = cv2.VideoWriter(filename, fourcc, 9.22, (width, height))
    webcam = cv2.VideoCapture(0)
    a=0
    startt=time.time_ns()
    while True:
        img = ImageGrab.grab(bbox=(0,0,width,height))
        _, frame= webcam.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        image=Image.fromarray(gray)
        image=circulateImage(image,(int(128),int(128)))
        mask = Image.new('L', (128,128), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + (128,128), fill=255)
        img.paste(image,box=(img.size[0]-140,img.size[1]-140),mask=mask)
        
        img_np =np.array(img)
        img_final=cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        img=img.resize((lbl.winfo_width(),lbl.winfo_height()))
        dfg=ImageTk.PhotoImage(img,master=root)
        lbl.create_image(0,0,image=dfg,anchor='nw')
        lbl.image=dfg
                
        captured_video.write(img_final)
        a+=1
        # if cv2.waitKey(1) == ord('q'):
        #     releaseVideo()
        #     break
        if STOP:
            stopt=time.time_ns()
            dur=round(((stopt-startt)/1000000000),2)
            print(f"{a} Frames captured after {dur} seconds")
            break


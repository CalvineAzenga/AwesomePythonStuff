import time
from PIL import ImageGrab
import numpy as np
import time
import cv2
import ctypes, win32gui, win32ui
from PIL import Image, ImageGrab,ImageDraw
import time

class ScreenRecorder:
    def __init__(self,fourcc="default",fps=20.0,screenSizeTuple=(1366,768)) -> None:
        self.ratio=ctypes.windll.shcore.GetScaleFactorForDevice(0)/100
        self.screenSizeTuple=screenSizeTuple
        self.fps=fps
        self.captured_video=None
        self.start=time.time_ns()
        self.stillRecording=True
        self.startAt=time.time_ns()
        if fourcc=="default":
            self.fourcc=cv2.VideoWriter_fourcc('m','p','4','v')
        else:
            self.fourcc=fourcc
        
    def get_cursor(self):
        try:
            hcursor=win32gui.GetCursorInfo()[1]
            hdc=win32ui.CreateDCFromHandle(win32gui.GetDC(0))
            hbmp=win32ui.CreateBitmap()
            hbmp.CreateCompatibleBitmap(hdc,36,36)
            hdc=hdc.CreateCompatibleDC()
            hdc.SelectObject(hbmp)
            hdc.DrawIcon((0,0), hcursor)
            bmpinfo=hbmp.GetInfo()
            bmpbytes=hbmp.GetBitmapBits()
            bmpstr=hbmp.GetBitmapBits(True)

            cursor= Image.frombuffer('RGB',(bmpinfo['bmWidth'],bmpinfo['bmHeight']),bmpstr,'raw','BGRX',0,1).convert("RGBA")
            try:
                win32gui.DestroyIcon(hcursor)
            except:
                pass
            win32gui.DeleteObject(hbmp.GetHandle())
            hdc.DeleteDC()
            pixdata=cursor.load()
            minsize=[32, None]

            width, height=cursor.size
            for y in range(height):
                for x in range(width):
                    if pixdata[x,y]==(0,0,0,255):
                        pixdata[x,y]=(0,0,0,0)
                    else:
                        if minsize[1]==None:
                            minsize[1]=y
                        if x<minsize[0]:
                            minsize[0]=x
            hotspot=win32gui.GetIconInfo(hcursor)[1:3]
        except:
            pass

        return (cursor,hotspot)
    def pointer_ellipse(self,image,xpos,ypos):
        image=image
        draw=ImageDraw.Draw(image,'RGBA')
        # draw.ellipse((100,150,275,300),outline="black",width=1,fill=(100,100,0,128))
        draw.ellipse((xpos-25,ypos-25,xpos+25,ypos+25),outline=None,width=0,fill=(20, 133, 43,75))
        return image
        # image.save(output_path)
    def startRecording(self,outputPath='useTime'):
        if outputPath=="useTime":
            outputPath=f'output_{str(time.time_ns())}.mp4'
        self.captured_video=cv2.VideoWriter(outputPath,self.fourcc,self.fps,self.screenSizeTuple)
        print("Recording started")
        self.startAt=time.time_ns()
        while self.stillRecording:
            try:
                cursor,(hotspot_x,hotspot_y)=self.get_cursor()
                img=ImageGrab.grab(bbox=None,include_layered_windows=True)

                pos_win=win32gui.GetCursorPos()
                pos=(round(pos_win[0]*self.ratio-hotspot_x),round(pos_win[1]*self.ratio-hotspot_y))
                img=self.pointer_ellipse(img,pos[0],pos[1])

                img.paste(cursor,pos,cursor)
                img=np.array(img)
                img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                self.captured_video.write(img)
            except Exception as msg:
                print("++ERROR++",msg)
                pass
    def getRecordingSecondsElapsed(self):
        duration_in_seconds=time.time_ns()-self.startAt
        return int(duration_in_seconds/(1000**3))
    def stopRecording(self):
        self.stillRecording=False
        self.captured_video.release()
        
    def __del__(self):
        end=time.time_ns()
        duration=(end-self.start)/(1000**3)
        print("Class Deleted after",duration,"seconds")

    
import ctypes, win32gui, win32ui
from PIL import Image, ImageGrab,ImageDraw
import time

def get_cursor():
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
    win32gui.DestroyIcon(hcursor)
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

    return (cursor,hotspot)

def pointer_ellipse(image_path,output_path,xpos,ypos):
    image=Image.open(image_path)
    draw=ImageDraw.Draw(image,'RGBA')
    # draw.ellipse((100,150,275,300),outline="black",width=1,fill=(100,100,0,128))
    draw.ellipse((xpos-30,ypos-30,xpos+30,ypos+30),outline="black",width=1,fill=(100,100,0,128))
    image.save(output_path)

# time.sleep(3) # gives us time to set up scene

size=round(ctypes.windll.shcore.GetScaleFactorForDevice(0)/100*32)
cursor,(hotspot_x,hotspot_y)=get_cursor()


ratio=ctypes.windll.shcore.GetScaleFactorForDevice(0)/100

img=ImageGrab.grab(bbox=None,include_layered_windows=True)
pos_win=win32gui.GetCursorPos()
pos=(round(pos_win[0]*ratio-hotspot_x),round(pos_win[1]*ratio-hotspot_y))

img.paste(cursor,pos,cursor)
img.save(f"screenshotx.png")
# pointer_ellipse(f"screenshotx.png",f"ellipse_{int(time.time())}.png",pos[0],pos[1])
 
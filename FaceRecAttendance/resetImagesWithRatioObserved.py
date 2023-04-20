from PIL import Image
import os


fxh=500
FOLDER=r"C:\Users\SHADY SUPERSUSER\Desktop\pythonProjects\FaceRecognitionMUTattendance\Imgs2Resize"
os.chdir(FOLDER)
for imgPath in os.listdir(FOLDER):
    imgPath=os.path.abspath(imgPath)
    img=Image.open(imgPath)
    hpercnt=(fxh/float(img.size[1]))
    wsize=int((float(img.size[0])*float(hpercnt)))
    img=img.resize((wsize,fxh),Image.NEAREST)
    img.save(imgPath)



    
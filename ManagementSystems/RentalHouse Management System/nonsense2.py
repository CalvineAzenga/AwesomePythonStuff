import os
from PIL import Image,ImageDraw
import random
import shutil
# images=[]

# width=400
# height=400
# for path,subdirs,filenames in os.walk(r"D:\New folder\Others\Image\Dirty"):
#     for file in filenames:
#         if str(file).endswith('.jpg') or str(file).endswith('.png'):
#             try:
#                 img=Image.open(os.path.join(path,file))
#                 img=img.resize((width,height),Image.ANTIALIAS)
#                 images.append(img)
#             except:
#                 pass

# images[0].save('./dirtypics.gif',save_all=True,append_images=images[1:],optimize=False,duration=1000,loop=0)

# Put Hollywood Movies into Folders
# path=r"D:\Videos\Movies"
# files=os.listdir(path)

# for file in files:
#     folder=path+"/"+'.'.join(str(file).split(".")[0:-1])
#     try:
#         os.mkdir(folder)
#         shutil.move(os.path.join(path,file),os.path.join(folder,file))
#     except:
#         pass
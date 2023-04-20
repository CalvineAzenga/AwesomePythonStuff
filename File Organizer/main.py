
import shutil
import os
# File Organizer according to filenames

folder='C:/Users/CALVOKILROY/Music/audio/Trials'

def splitter(stringx):
    thisString=str(stringx).replace('_',' ').replace('-',' ').replace(',',' ').replace('&',' ').replace('%',' ')
    thisString=thisString.split(' ')
    return thisString



# for path, subdirlist, filelist in os.walk(folder):
#     for onefile in filelist:
#         onefile1=onefile
#         onefile1=onefile1[:-4]
#         for word in splitter(onefile1):
#             if os.path.exists(os.path.join(path,word)):
#                 try:
#                     shutil.move(os.path.join(path,onefile),os.path.join(path+'/'+word,onefile))
#                     break
#                 except:
#                     pass
#             else:
#                 try:
#                     os.makedirs(os.path.join(path,word))
#                     shutil.move(os.path.join(path,onefile),os.path.join(path+'/'+word,onefile))
#                     break
#                 except:
#                     pass



# for path, subdirlist, filelist in os.walk(folder):
#     for onefile in filelist:
#         try:
#             shutil.move(os.path.join(path,onefile),os.path.join(folder,onefile))
#         except:
#             pass


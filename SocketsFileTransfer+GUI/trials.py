import os

with open("D:/Videos",'rb') as df:
    print(len(os.path.getsize(df)))

import os

a=1
for path, subdir, filenames in os.walk("./profile_images"):
    for file in filenames:
        extension=str(file).split(".")[-1]
        try:
            os.rename(os.path.join(path,file),os.path.join(path,str(a)+"."+extension))
            a+=1
        except:
            print("ERROR Occurred")
            pass
print(f"{a} files renamed")
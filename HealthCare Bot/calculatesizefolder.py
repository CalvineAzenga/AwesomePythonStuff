import os

errors=[]
pathtosearch="C:/Users/CalvineAzenga"
sizeofFolder=0
for path,subdir,filenames in os.walk(pathtosearch):
    for file in filenames:
        try:
            sizeofFolder+=os.path.getsize(os.path.join(path,file))
        except Exception as msg:
            errors.append(msg)
            pass

print(f"Size of {pathtosearch} is {round(sizeofFolder/(1024*1024*1024),2)} Gb")
if len(errors)>0:
    print(f"\n A total of {len(errors)} errors found in {pathtosearch}\tThe errors are {errors}")
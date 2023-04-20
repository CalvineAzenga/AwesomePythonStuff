from PIL import Image,ImageFilter

def dropShadow(image, offset=(5,5), background="white", shadow="grey", border=8, iterations=3):
    totalWidth=image.size[0]+abs(offset[0])+2*border
    totalHeight=image.size[0]+abs(offset[1])+2*border
    back=Image.new(image.mode, (totalWidth,totalHeight),background)

    shadowLeft= border+max(offset[0],0)
    shadowTop=border+max(offset[1],0)
    back.paste(shadow, [shadowLeft,shadowTop,shadowLeft+image.size[0],shadowTop+image.size[1]])

    n=0
    while n<iterations:
        back=back.filter(ImageFilter.BLUR)
        n+=1

    imageLeft=border-min(offset[0],0)
    imageTop=border-min(offset[1],0)
    back.paste(image,(imageLeft,imageTop))
    return back

if __name__=="__main__":
    image=Image.open("./profiles/b (4).jpg")
    image.thumbnail((200,200),Image.ANTIALIAS)
    dropShadow(image).show()
    dropShadow(image,background="beige", shadow=0x444444, offset=(0,5)).show()

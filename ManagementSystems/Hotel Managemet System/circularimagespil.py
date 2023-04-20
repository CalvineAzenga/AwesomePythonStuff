from PIL import Image,ImageOps,ImageDraw
size=(70,70)
mask=Image.new('L',size,0)
draw=ImageDraw.Draw(mask)
draw.ellipse((0,0) + size,fill=255)

im=Image.open('./profiles/a (2).jpg')

output=ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
output.putalpha(mask)
output.save('cally.png')
from PIL import Image,ImageDraw,ImageFont
import pandas as pd
import os
import time

df=pd.read_csv("./studentdata.csv")

# print(df)
records=df.to_dict('records')
# print(records)
font=ImageFont.truetype("./fonts/SourceSansPro-Regular-webfont.185ff557118a.ttf",size=16)

template_image=Image.open("./c_template.png")



def generateCard(data):
    template_image=Image.open("./c_template.png")
    profile_image=Image.open(f"./profile_images/{data['image']}").resize((154,140),Image.Resampling.LANCZOS)
    template_image.paste(profile_image,(2,99))
    image_draw=ImageDraw.Draw(template_image)
    image_draw.text((250,107),text=data['name'],font=font,fill="#880015")
    image_draw.text((250,130),text=data['reg'],font=font,fill="#880015")
    image_draw.text((250,150),text=str(data['phone']),font=font,fill="#880015")
    image_draw.text((250,169),text=data['course'],font=font,fill="#880015")
    image_draw.text((250,190),text=data['school'],font=font,fill="#880015")
    image_draw.text((250,210),text=data['validity'],font=font,fill="#880015")
    template_image.save(f"./generated_images/{str(data['image'])}",subsampling=0,quality=100)
    del template_image
def generateAllCards():
    for record in records:
        print("Generating card for::",record['name'],'->',record['reg'])
        generateCard(record)
generateAllCards()
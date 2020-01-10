from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime
import pandas as pd 




## creates the text and adjusts the font depending on its lengts

# gets the first joke from the csv list
def hae_vitsi():
    data = pd.read_csv("Z:\python\dadjokeai\jokelist.csv") 
    return data.iloc[0,1]


# funktion for checking the correct font size so that it fits in the img
def etsi_font(joke):
    # TEST BY ITERATION THE SIZE OF THE FONT
    i = 38
    while True:
        fnt = ImageFont.truetype('arial.ttf', i)
        #THIS FUNCTION BELOW GETS THE LENGHT OF TEXT IN PIXELS GIVEN A FONT
        pituus = fnt.getsize(max(joke.split('\n'), key=len))
        if pituus[0] <= 850:
            break
        i = i - 1
    return i


def gen_kuva():
    # gets the joke and deletes the "joke:" and black squares
    vitsi = hae_vitsi()
    vitsi = vitsi[7:len(vitsi)]
    vitsi = vitsi.replace("\r", '')


    fnt = ImageFont.truetype('arial.ttf', etsi_font(vitsi))

    # create new image
    image = Image.new(mode = "RGB", size = (900,900), color = "white")
    draw = ImageDraw.Draw(image)

    draw.text((50,400), vitsi, font=fnt, fill=(0,0,0))

    # watermark
    wmfont = ImageFont.truetype("arial.ttf", 18)
    draw.text((600,350), "@ai_dadjokes", fill=(0,0,0), font=wmfont)


    # save the file
    # check if there is a dir for posted jokes
    if os.path.isdir("postedjokes"):
        print("dir exists")
        pass
    else:
        os.mkdir("postedjokes")

    # name of the file to save
    now = datetime.now()
    dt_string = now.strftime("%d.%m.%Y_%H.%M.%S")
    print("date and time =", dt_string)	
    filename = f'Z:/python/dadjokeai/postedjokes/joke_{dt_string}.jpg'  


    image.save(filename)

    # open the file
    os.system(filename)

    return filename





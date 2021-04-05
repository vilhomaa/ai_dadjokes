from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime
import pandas as pd
from sys import platform



## creates the text and adjusts the font depending on its lengts

# gets the first joke from the csv list
def hae_vitsi(special = False, norm = False):
    if platform != 'darwin':
        os.chdir("Z:\python\dadjokeai")
    if platform == 'darwin':
        os.chdir("/Users/Lassi 1/Documents/python/ai_dadjokes")
    if special is False:
        data = pd.read_csv("jokelist.csv")
        if norm is True:
            data = pd.read_csv("norm_jokelist.csv")
    else:
        data = pd.read_csv("special_jokelist.csv")

    return data.iloc[0,1]


# funktion for checking the correct font size so that it fits in the img
def etsi_font(joke):
    # TEST BY ITERATION THE SIZE OF THE FONT
    i = 38
    if platform != 'darwin':
        font_name = "arial.ttf"
    if platform == 'darwin':
        font_name = "Arial.ttf"
    while True:
        fnt = ImageFont.truetype(font_name, i)
        #THIS FUNCTION BELOW GETS THE LENGHT OF TEXT IN PIXELS GIVEN A FONT
        pituus = fnt.getsize(max(joke.split('\n'), key=len))
        if pituus[0] <= 850:
            break
        i = i - 1
    return i


def gen_kuva(unique = False,norm = False):
    # gets the joke and deletes the "joke:" and black squares
    vitsi = hae_vitsi(special=unique, norm= norm)
    vitsi = vitsi[7:len(vitsi)]
    vitsi = vitsi.replace("\r", '')

    if platform != 'darwin':
        font_name = "arial.ttf"
    if platform == 'darwin':
        font_name = "Arial.ttf"

    fnt = ImageFont.truetype(font_name, etsi_font(vitsi))

    # create new image
    image = Image.new(mode = "RGB", size = (900,900), color = "white")
    draw = ImageDraw.Draw(image)

    draw.text((50,400), vitsi, font=fnt, fill=(0,0,0))

    # watermark
    if platform != 'darwin':
        font_name = "arial.ttf"
    if platform == 'darwin':
        font_name = "Arial.ttf"
    wmfont = ImageFont.truetype(font_name, 18)
    draw.text((600,350), "@ai_dadjokes", fill=(0,0,0), font=wmfont)


    # save the file
    # check if there is a dir for posted jokes


    if os.getcwd() == 'Z:\\python\\dadjokeai' or os.getcwd() == "/Users/Lassi 1/Documents/python/ai_dadjokes":
        if os.path.isdir("postedjokes"):
            print("dir exists")

        else:
            os.mkdir("postedjokes")

        os.chdir("postedjokes")



    if os.getcwd() == 'Z:\\python\\dadjokeai\\dadjokevenv':
        os.chdir("..")
        os.chdir("postedjokes")


    # name of the file to save
    now = datetime.now()
    dt_string = now.strftime("%d.%m.%Y_%H.%M.%S")
    print("date and time =", dt_string)
    if unique is False:
        filename = f'joke_{dt_string}.jpg'
        if norm is True:
            filename = f'norm_joke_{dt_string}.jpg'
    else:
        filename = f'special_joke_{dt_string}.jpg'


    image.save(filename)

    # open the file
    os.system(filename)

    return filename

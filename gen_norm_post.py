import os

import kuvanteko
import gen_special_joke
import time
from uus_postaa import launch_browser, upload_photo
from sys import platform
os.chdir('..')

print("Hellou and welcome to mad_instagram")


onko_vitsi_ok = "n"

while onko_vitsi_ok is "n":
    # Tekee vitsin
    jokes = gen_special_joke.gen_special_joke()
    # Tallentaa sen
    gen_special_joke.save_special_joke(jokes,special=False)

    # Tsekkaa onko vitsi ok:n pituinen
    if kuvanteko.etsi_font(kuvanteko.hae_vitsi(special=False,norm=True)) < 24:
        print("Vitsi on liian pitkä, tekee uuden")
        continue

    onko_vitsi_ok = input("Onko vitsi hyvä? jos ei paina n ja enter, jos on paina jotain muuta: ")


kuvateksti = input("Laita kuvateksti:")


## Vitsistä kuvanteko

kuva_path = kuvanteko.gen_kuva(norm=True)


## postaus

browser = launch_browser()
time.sleep(5.5)

upload_photo(kuva_path,captiontext=f'{kuvateksti}'
                +'\r\n.\r\n.' + '#dad #joke #jokes #dadjokes #ai #machine #learning #artificial #intelligence #neural #network #funny #future #robot #humour',selain = browser)

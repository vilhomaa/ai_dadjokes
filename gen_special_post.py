import os

import kuvanteko
import gen_special_joke
import time
from uus_postaa import launch_browser, upload_photo
os.chdir('..')

print("Hellou and welcome to mad_instagram")

vitsi_input = input("Kirjoita input vitsille: ")
submitter_account = input("Keneltä input on (ei tarvitse laittaa @): ")
account = f'@{submitter_account}'

onko_vitsi_ok = "n"

while onko_vitsi_ok is "n":
    # Tekee vitsin
    jokes = gen_special_joke.gen_special_joke(vitsi_input)
    # Tallentaa sen
    gen_special_joke.save_special_joke(jokes)

    # Tsekkaa onko vitsi ok:n pituinen
    if kuvanteko.etsi_font(kuvanteko.hae_vitsi(special=True)) < 24:
        print("Vitsi on liian pitkä, tekee uuden")
        continue

    onko_vitsi_ok = input("Onko vitsi hyvä? jos ei paina n ja enter, jos on paina jotain muuta: ")





## Vitsistä kuvanteko

kuva_path = kuvanteko.gen_kuva(unique=True, norm= True)


## postaus

browser = launch_browser()
time.sleep(5.5)

upload_photo(kuva_path,captiontext='Do you want to help the algorithm in generating a joke? Comment down below an input, and a dad joke will be generated based on it. The suggestion input with the most likes will be chosen\r\n.\r\n'
                +f'The input used here was "{vitsi_input}" submitted by {account}! Thank you for your submission!"' 
                +'\r\n.\r\n' + '#dad #joke #jokes #dadjokes #ai #machine #learning #artificial #intelligence #neural #network #funny #future #robot #humour',selain = browser)


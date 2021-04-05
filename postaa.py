
import os
os.chdir("Z:\python\dadjokeai\dadjokevenv")
import kuvanteko
from uus_postaa import launch_browser, upload_photo
os.chdir("Z:\python\dadjokeai")
import pandas as pd
import time
import numpy as np
from random import sample 

#importing login details for the ig account
import sys

sys.path.insert(1, 'Z:\python')

from salasanat import dadjokelogin


# moves the joke from jokelist to postedjokes
def vitsin_siirto(liian_pitk = False):
        joke = kuvanteko.hae_vitsi()

        # makes a csv for posted jokes if it doesnt exist
        if os.path.exists("postedjokes.csv"):
                print("postedjokes.csv exists")
                tempdf = pd.read_csv("postedjokes.csv")
                if liian_pitk == False:
                        tempdf.loc[len(tempdf)] = joke
                else:
                        tempdf.loc[len(tempdf)] = "NOT POSTED" + joke
                tempdf.to_csv("postedjokes.csv", index=False)
        else:
                tempdf = pd.DataFrame([joke])
                tempdf.to_csv("postedjokes.csv",index=False)
        # Drops the joke from the main joke list
        aaaa = pd.read_csv("jokelist.csv")
        aaaa = aaaa.loc[1:]
        aaaa = aaaa.reset_index(drop = True)
        aaaa.to_csv("jokelist.csv",index=False)

joke = kuvanteko.hae_vitsi()

# check if the font will be too small

def tsekkaa(unique = False):
        if kuvanteko.etsi_font(kuvanteko.hae_vitsi(special=unique)) < 24:
                vitsin_siirto(liian_pitk = True)
                return True
        else:
                return False

while tsekkaa():
        print("deleted'd joke because it was too long")



## 50% chance konetta startatessa että tää postaa
numba = np.random.normal(0)

if numba > 0:
        print("POSTAA!!!")               
        path = kuvanteko.gen_kuva()

        # ottaa vikan osan pathista
        path = path.split("/")[4]


        ## KUVAN POSTAUS


        browser = launch_browser()
        time.sleep(5.5)
        upload_photo(path,captiontext='\r\n' +'\r\n' +'\r\n' + '#dad #joke #jokes #dadjokes #ai #machine #learning #artificial #intelligence #neural #network #funny #future #robot #humour',selain = browser)
        ## moves the joke 
        vitsin_siirto()
        

else:
        print("ei postaa")



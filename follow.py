from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np

#importing login details for the ig account
import sys

sys.path.insert(1, 'Z:\python')

from salasanat import dadjokelogin

## script for following people using selenium


browser = webdriver.Chrome("Z:\lataukset\chromedriver.exe")

# menee chromeen
browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
time.sleep(np.random.normal(2,0.2))

# kirjautuu sisään
elem = browser.find_element_by_name("username")
elem.send_keys(dadjokelogin[0])
time.sleep(np.random.normal(2,0.2))
elem = browser.find_element_by_name("password")
elem.send_keys(dadjokelogin[1])
elem.send_keys(Keys.RETURN)

# painaa ilmotusjutun pois
time.sleep(np.random.normal(2,0.2))
elem = browser.find_element_by_xpath(".//*[@class='aOOlW   HoLwm ']")
time.sleep(np.random.normal(2,0.2))
elem.send_keys(Keys.RETURN)
time.sleep(np.random.normal(5,0.2))


# scrollailee vähän - esittää oikeeta ihmistä, 1-3 krt

randint_scrolling = np.random.randint(1,3)
for i in range(randint_scrolling):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    time.sleep(np.random.normal(67,10))

# tämä funtktio toimii seuraavasti:
# 1. menee search bariin ja ettii listasta annetun tilin ja menee sen sivulle
# 2. seuraa follaajia avaamalla followers ikkunan

def seuraa(tili):
    # menee search bariin
    elem = browser.find_element_by_xpath(".//*[@class='XTCLo x3qfX ']")
    time.sleep(np.random.normal(1,0.2))
    elem.send_keys(tili) # voisit kehittää jonkun joka ottaa randomisti jonkun tilin
    time.sleep(np.random.normal(2,0.2))
    elem = browser.find_element_by_xpath(".//*[@class='z556c']")
    elem.click()


    # hakee tilin nimen jotta löytäis followers napin
    time.sleep(np.random.normal(2,0.2))
    account_name = browser.find_element_by_xpath(".//*[@class='_7UhW9       fKFbl yUEEX   KV-D4            fDxYl     ']")
    account_name = account_name.text
    # nää ylemmät koodit vois korvata vaan tilillä, mutta tällä tapaa
    # jos on ollu pieni typo tilinimen kirjottamisessa niin se löytää 
    # sen tilin nimen mitä todennäköisemmin

    # tässä try koska seuraaminen saattaa kusee jos se tili on private?
    try:
        # avaa followers ikkunan
        time.sleep(np.random.normal(2,0.2))
        elem = browser.find_element_by_xpath(f".//*[@href='/{account_name}/followers/']")
        elem.click()
        time.sleep(np.random.normal(1,0.2))

        #seuraa listasta
        buttons = browser.find_elements_by_xpath(".//*[@class='sqdOP  L3NKy   y3zKF     ']")
        time.sleep(np.random.normal(2,0.2))

        for i in buttons[0:8]:
            i.click()
            time.sleep(np.random.normal(80,10))


        # klikkaa pois valikosta
        elem = browser.find_element_by_xpath(".//*[@class='wpO6b ']")
        elem.click()
        time.sleep(np.random.normal(2,0.2))
        browser.refresh()
        print("doned for: " + tili)
    except:
        print("Account salee private - skipping " + tili)


## Funktio unfollaamiseen
def unfollaa(monta): 
    elem = browser.find_element_by_xpath(f".//*[@href='/ai_dadjokes/']")
    elem.click()

    #klikkaa omalle sivulle
    elem = browser.find_element_by_xpath(f".//*[@href='/ai_dadjokes/']")
    time.sleep(np.random.normal(1,0.2))
    elem.click()
    # avaa seuraajat
    elem = browser.find_element_by_xpath(f".//*[@href='/ai_dadjokes/following/']")
    elem.click()

    # ettii seurattujen napit ja alkaa unfollaa
    buttons = browser.find_elements_by_xpath(".//*[@class='sqdOP  L3NKy    _8A5w5    ']")
    time.sleep(np.random.normal(2,0.2))

    for i in buttons[0:monta]:
        i.click()
        time.sleep(np.random.normal(1,0.2))
        elem = browser.find_element_by_xpath(".//*[@class='aOOlW -Cab_   ']")
        time.sleep(np.random.normal(1,0.2))
        elem.click()
        time.sleep(np.random.normal(80,10))
    
    print("unfolled 8 ppls")

# menee unfollaa




# menee seuraamaan näiden tilien tyyppejä
tilit = ["dadsaysjokes","dadjokes._", "_codehub_" ]
np.random.shuffle(tilit)


# tekee seurausprosessin kolmelle tilille (kuumottaa et enempi voi lead to ban)
# venaa about tunnin ennen ku menee taas seuraamaan
for i in tilit[0:3]:
    seuraa(i)
    time.sleep(np.random.normal(3600, 180))

followers_amount = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").text
followers_amount = int(followers_amount)

if followers_amount > 100:
    unfollaa(followers_amount - 100)
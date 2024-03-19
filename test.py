import pyautogui
import time

import bs4 as bs
import urllib.request
from urllib.request import FancyURLopener
'''
afl_link = "http://amzn.to/2BgFhiY"
def run_bs4(afl_link):

    class MyOpener(FancyURLopener):
        version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

    myopener = MyOpener()
    page = myopener.open(afl_link).read()
    soup = bs.BeautifulSoup(page, 'lxml')
    thing = str(soup.find_all(id="productTitle")[0])
    thing2 = thing.split(">")[1]
    thing3 = thing2.split("<")[0]
    thing4 = thing3.lstrip()
    thing5 = thing4.rstrip()
    return thing5


print(run_bs4(afl_link))
'''
'''
image_num = 1

while(True):

    print(pyautogui.position())

'''
'''
pyautogui.moveTo(795, 128)
pyautogui.click()
time.sleep(3)
'''
'''
while(True):
    time.sleep(5)
    pyautogui.scroll(-318)  # scroll down 318 pixels
'''
'''
time.sleep(7)
pyautogui.moveTo(500, 400, duration=0.5)
pyautogui.rightClick()
pyautogui.moveTo(571, 575, duration=0.1)
pyautogui.click()
time.sleep(1.5)
# name image
pyautogui.typewrite(str("stuff"))
time.sleep(0.5)
pyautogui.press('enter')
# click on large image
pyautogui.moveRel(-150, -250, duration=0.5)
pyautogui.rightClick()
pyautogui.moveRel(10, 5, duration=0.5)
pyautogui.click()
time.sleep(4)
pyautogui.moveTo(283, 13, duration=1)
pyautogui.click()
time.sleep(3)
# Grab affiliate link text
pyautogui.moveTo(186, 90, duration=1)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.keyDown('ctrl')
pyautogui.press('c')
pyautogui.keyUp('ctrl')
# copy from clipboard to variable
'''
'''
link_list = ['http://amzn.to/2BuQG2N', 'http://amzn.to/2BusxJx', 'http://amzn.to/2Bi7wxI']
afl_link ='http://amzn.to/2BusxJx'

if afl_link in link_list:
    print("GOT HERE")
'''
pyautogui.moveTo(396,47,duration=0.5)
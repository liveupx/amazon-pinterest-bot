import pyautogui
import time
import win32clipboard as clip
import bs4 as bs
from urllib.request import FancyURLopener
link_list = [0,0,0]
bottleneck = 5

def run_bs4(afl_link):
    try:

        class MyOpener(FancyURLopener):
            version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

        myopener = MyOpener()
        page = myopener.open(afl_link).read()
    except:
        return "Must Have!"
    soup = bs.BeautifulSoup(page, 'lxml')
    thing = str(soup.find_all(id="productTitle")[0])
    thing2 = thing.split(">")[1]
    thing3 = thing2.split("<")[0]
    thing4 = thing3.lstrip()
    thing5 = thing4.rstrip()
    return thing5


def check_if_slot_is_link():
    #give time for page to fully load so it keeps cached data on how much scroll item page contained
    time.sleep(bottleneck)
    #move cursor to where thenew tab would be (or ghost tab is not) and click that location to open the tab
    pyautogui.moveTo(534,11, duration=1)
    pyautogui.click()
    #move cursor to /shop/ in address bar
    pyautogui.moveTo(396,47,duration=0.5)
    pyautogui.doubleClick()
    #copy those four letters
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    clip.OpenClipboard()
    copied = clip.GetClipboardData()
    clip.CloseClipboard()
    if(copied == 'shop'):
        #close the tab
        pyautogui.keyDown('ctrl')
        pyautogui.press('w')
        pyautogui.press('pgup')
        pyautogui.keyUp('ctrl')
        return True
    else:
        return False


def renew_state():
    # close tab
    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')
    # close big image of previous item
    pyautogui.press('esc')
    pyautogui.moveTo(773, 235, duration=0.5)


def run_algorithm():
    skip_state = False
    pyautogui.moveTo(500,400, duration=0.5)
    pyautogui.rightClick()
    pyautogui.moveTo(571,575,duration=0.5)
    pyautogui.click()
    time.sleep(1.5)
    # name image
    pyautogui.typewrite(str(image_num))
    time.sleep(1)
    pyautogui.press('enter')
    # click on large image
    pyautogui.moveRel(-150, -250, duration=0.5)
    pyautogui.rightClick()
    pyautogui.moveRel(10, 5, duration=0.5)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(283, 13, duration=1)
    pyautogui.click()
    time.sleep(4)
    # Grab affiliate link text
    pyautogui.moveTo(186, 90, duration=1)
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    #copy from clipboard to variable
    clip.OpenClipboard()
    afl_link = clip.GetClipboardData()
    clip.CloseClipboard()
    if "http" not in afl_link:
        afl_link = "www.kiitri.com"
    #copy part link
    pyautogui.moveTo(361,45)
    pyautogui.dragTo(443,45,duration=1)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    #copy from clipboard to variable
    clip.OpenClipboard()
    part_link = clip.GetClipboardData()
    clip.CloseClipboard()
    #check if part of link is one of last 3 used links
    if part_link in link_list:
        renew_state()
        pyautogui.scroll(-318)  # scroll down 318 pixels
        skip_state = True
        return skip_state
    else:
        link_list[0] = link_list[1]
        link_list[1] = link_list[2]
        link_list[2] = part_link
        print(link_list)
    #Get text desciption of this item
    description = run_bs4(afl_link)
    # close tab
    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')
    #go to pinterest tab
    pyautogui.moveTo(283, 13, duration=0.5)
    pyautogui.click()
    # hover over plus sign
    pyautogui.moveTo(1192, 90, duration=1)
    # move to hover over "upload image"
    pyautogui.moveTo(1192, 156, duration=0.5)
    pyautogui.click()
    time.sleep(0.5)
    # hover over "destination url"
    pyautogui.moveTo(567, 446, duration=0.5)
    pyautogui.click()
    time.sleep(0.5)
    # paste affiliate link
    pyautogui.typewrite(afl_link)
    # upload image I just created
    pyautogui.moveTo(866, 359)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.typewrite(str(image_num) + ".jpg")
    pyautogui.press('enter')
    time.sleep(1)
    # post item (Pinterest)
    pyautogui.moveTo(891, 510, duration=0.2)
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    # add caption (Pinterest)
    pyautogui.moveTo(432, 525, duration=0.2)
    pyautogui.click()
    time.sleep(0.4)
    pyautogui.typewrite(description)
    # choose board (Pinterest)
    pyautogui.moveTo(764,170)
    pyautogui.doubleClick()
    pyautogui.typewrite('Best Amazon Finds')
    time.sleep(2)
    pyautogui.moveTo(773, 235, duration=0.5)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(484, 640, duration=0.5)
    pyautogui.click()
    time.sleep(3)
    # jump back to amazon page
    pyautogui.keyDown('ctrl')
    pyautogui.press('pgup')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    # close big image of previous item
    pyautogui.press('esc')
    pyautogui.moveTo(773, 235, duration=0.5)
    return skip_state


time.sleep(5)
image_num = 1
while True:
    slot = 1
    while slot<=5:
        pyautogui.moveTo(150+ (slot-1)*255, 250, duration=0.5)
        #click image corresponding to this slot.
        pyautogui.mouseDown()
        time.sleep(0.6)
        pyautogui.mouseUp()
        time.sleep(0.5)
        if check_if_slot_is_link(): #move mouse to where new tab would open and see if theres a tab there.
            slot +=1
        else:
            if run_algorithm():
                slot = 0
        slot +=1
        image_num +=1
    #Grab scroll bar and move down a row
    time.sleep(2)
    pyautogui.scroll(-318)  # scroll down 318 pixels

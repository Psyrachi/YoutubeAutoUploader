import pyautogui as pg
import time
import sys


def openchrome():
    pg.leftClick(103,1045,.2,.12)
    pg.typewrite('Google Chrome')
    time.sleep(1)
    pg.hotkey('enter')
    time.sleep(1)
    return


def openyoutube():
    pg.leftClick(265, 80, .2, .12)
    pg.hotkey('space')
    pg.typewrite('youtube.com')
    pg.hotkey('enter')
    time.sleep(5)
    pg.leftClick(1590, 140, .2, .12)
    pg.leftClick(1607, 217, .2, .12)
    time.sleep(5)
    pg.leftClick(950, 735, .2, .12)
    time.sleep(.5)
    return


def openvideo():
    pg.leftClick(180, 70, .2, .12)
    pg.typewrite('C:\\Users\\YOUR_USERNAME\\Desktop\\Video')
    pg.hotkey('enter')
    time.sleep(.5)
    pg.moveTo(380, 310, .12)
    pg.doubleClick()
    return


def enterdesc():
    pg.hotkey('space')
    pg.typewrite('CHANGE_ME')
    pg.leftClick(335, 675, .2, .12)
    pg.typewrite('CHANGE_ME')
    pg.moveTo(1670, 450, .12)
    pg.dragTo(1670, 640, .5)
    return


def openthumb():
    pg.leftClick(405, 505, .2, .12)
    time.sleep(1)
    pg.leftClick(180, 70, .2, .12)
    pg.typewrite('C:\\Users\\YOUR_USERNAME\\Desktop\\Thumbnail')
    pg.hotkey('enter')
    time.sleep(.5)
    pg.moveTo(380, 310, .12)
    pg.doubleClick()
    return


def finishparameters():
    pg.moveTo(1670, 647, .12)
    pg.dragTo(1672, 835, 1)
    pg.leftClick(328, 587, .2, .12)
    pg.moveTo(1613, 907, .12)
    pg.doubleClick()
    pg.leftClick(405, 789, .2, .12)
    pg.moveTo(1516, 903, .12)
    pg.doubleClick()
    print("Done!")
    return

openchrome()
openyoutube()
openvideo()
time.sleep(5)
enterdesc()
openthumb()
finishparameters()

sys.exit()

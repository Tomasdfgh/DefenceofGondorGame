import pyautogui
from pynput.mouse import Button, Controller
import keyboard
import sys
import tkinter as tk
import time
import os

def start():
    myScreenshot = pyautogui.screenshot()
    icon_image = myScreenshot.convert("RGB")
    attack = 0
    rgb_pixel = "0"
    x_cord = 0
    y_cord = 0
    x_use = 0
    y_use = 0
    day = 1
    rgb_pixel = icon_image.getpixel((170, 100))
    rgb_pixel = icon_image.getpixel((x_cord, y_cord))
    while True:
        if keyboard.is_pressed('Esc'):
            print("Hello")
            sys.exit(0)
            quit()
        while str(rgb_pixel) != "(237, 28, 36)" and y_cord < 1080:
            x_cord = 0
            while str(rgb_pixel) != "(237, 28, 36)" and x_cord < 1920:
                rgb_pixel = icon_image.getpixel((x_cord, y_cord))
                x_cord += 1
            y_cord += 1
        mouse = Controller()
        mouse.position = (x_cord + 100,y_cord - 20)
        mouse.press(Button.left)
        mouse.position = (300, 130)
        time.sleep(0.1)
        mouse.release(Button.left)
        
        #Starting Game
        mouse.position = (900,500)
        mouse.click(Button.left, 1)
        #First 3 days
        i = 0
        while i < 6:
            mouse.position = (1650,250) #Next button
            mouse.click(Button.left, 1)
            time.sleep(0.1)
            mouse.position = (1300,400) #Ore refinery right
            mouse.click(Button.left, 1)
            time.sleep(0.1)
            i += 1
        i = 0
        while i < 3:
            mouse.position = (300, 600)
            mouse.click(Button.left, 1)
            time.sleep(0.15)
            mouse.position = (1650,250)
            mouse.click(Button.left, 1)
            time.sleep(0.15)
            i += 1
        mouse.position = (300, 600)
        mouse.click(Button.left, 1)
        i = 0
        while i<5:
            mouse.position = (1300, 300)
            mouse.click(Button.left, 1)
            time.sleep(0.1)
            mouse.position = (1650,250)
            mouse.click(Button.left, 1)
            time.sleep(0.1)
            i += 1
        mouse.position = (1300, 300)
        mouse.click(Button.left, 1)
        i = 0
        while i < 4:
            mouse.position = (300, 520) #Lodge left
            mouse.click(Button.left, 1)
            time.sleep(0.15)
            mouse.position = (1650,250)
            mouse.click(Button.left, 1)
            time.sleep(0.15)
            i += 1
        mouse.position = (1650, 850) # Next Day
        mouse.click(Button.left, 1)
        day += 1
        i = 0
        while i < 17:
            mouse.position = (1650,250)
            mouse.click(Button.left, 1)
            time.sleep(0.1)
            i += 1
        i = 0
        while i < 2:
            mouse.position = (1300,500)
            mouse.click(Button.left, 1)
            time.sleep(0.1)
            mouse.position = (1650,250)
            mouse.click(Button.left, 1)
            time.sleep(0.1)
            i += 1
        i = 0
        while i < 2:
            mouse.position = (1300,600)
            mouse.click(Button.left, 1)
            time.sleep(0.1)
            mouse.position = (1650,250)
            mouse.click(Button.left, 1)
            time.sleep(0.1)
            i += 1
        mouse.position = (1650, 850) # Next Day
        mouse.click(Button.left, 1)
        day += 1
        i = 0
        while i < 21:
            mouse.position = (1650,250)
            mouse.click(Button.left, 1)
            time.sleep(0.1)
            i += 1
        i = 0
        mouse.position = (300, 700)
        mouse.click(Button.left, 1)
        time.sleep(0.1)
        mouse.position = (1650,250)
        mouse.click(Button.left, 1)
        time.sleep(0.1)
        mouse.position = (1300,500)
        mouse.click(Button.left, 1)
        time.sleep(0.1)
        mouse.position = (1650,250)
        mouse.click(Button.left, 1)
        time.sleep(0.1)
        while i < 2:
            mouse.position = (1300,600)
            mouse.click(Button.left, 1)
            time.sleep(0.1)
            mouse.position = (1650,250)
            mouse.click(Button.left, 1)
            time.sleep(0.1)
            i += 1
        mouse.position = (1650, 850) # Next Day
        mouse.click(Button.left, 1)
        day += 1
        time.sleep(1)
        mouse.position = (1650,350) #Stronghold Button
        mouse.click(Button.left, 1)
        i = 0
        while i < 5:
            upgradeStrongHold()
            i += 1
        i = 0
        while i < 4:
            upgradeWall()
            i += 1
        for i in range(25):
            traintroops("a")
        

        queue_today = []
        queue_tomorrow = []
        mouse.position = (1650, 850) # Next Day
        mouse.click(Button.left, 1)
        day += 1
        time.sleep(0.02)
        #Death and attack check
        myScreenshot = pyautogui.screenshot()
        icon_image = myScreenshot.convert("RGB")
        rgb_pixel = icon_image.getpixel((500, 600))
        rgb_pixel_2 = icon_image.getpixel((1200, 600))
        if keyboard.is_pressed('Esc'):
            sys.exit(0)
            quit()
        
        while str(rgb_pixel) != "(127, 127, 127)" and rgb_pixel_2 != "(127, 127, 127)":
            if keyboard.is_pressed('Esc'):
                print("Hello")
                sys.exit(0)
                quit()
            orcs = 0
            trolls = 0
            urukhai = 0
            goblins = 0
            total = 0
            if len(queue_today) >= 25:
                queue_today = []
            if str(rgb_pixel) == "(237, 28, 36)" and str(rgb_pixel_2) == "(237, 28, 36)":
                queue_today.insert(0,"Heal Wall")
                time.sleep(1)
                orcs = round((0.0072*(int(day) - 10)**2 + 20) * 0.7)
                goblins = round((0.007*(int(day) - 10)**2 + 20) * 0.7)
                if day >= 30:
                    trolls = round((0.0001*(int(day) - 30)**2 + 2) * 0.75)
                else:
                    trolls = 0
                if day >= 15:
                    urukhai = round((0.0001*(int(day) - 15)**2 + 5) * 0.7)
                else:
                    urukhai = 0
                total = urukhai + goblins + orcs + trolls
                while total > 0:
                    if total > 1000:
                        traintroops("c")
                        total -= 1000
                        time.sleep(0.2)
                        myScreenshot = pyautogui.screenshot()
                        icon_image = myScreenshot.convert("RGB")
                        rgb_pixel_3 = icon_image.getpixel((800, 600))
                        rgb_pixel_4 = icon_image.getpixel((1100, 600))
                        if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                            queue_today = []
                            print("Cancel 1")
                    if total > 100:
                        traintroops("b")
                        total -= 100
                        time.sleep(0.2)
                        myScreenshot = pyautogui.screenshot()
                        icon_image = myScreenshot.convert("RGB")
                        rgb_pixel_3 = icon_image.getpixel((800, 600))
                        rgb_pixel_4 = icon_image.getpixel((1100, 600))
                        if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                            queue_today = []
                            print("Cancel 2")
                    else:
                        traintroops("a")
                        total -= 1
                        myScreenshot = pyautogui.screenshot()
                        icon_image = myScreenshot.convert("RGB")
                        rgb_pixel_3 = icon_image.getpixel((800, 600))
                        rgb_pixel_4 = icon_image.getpixel((1100, 600))
                        if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                            queue_today = []
                            print("Cancel 3")
            if keyboard.is_pressed('Esc'):
                print("Hello")
                sys.exit(0)
                quit()
            if day % 3 == 0: #Lodge
                queue_today.append("UpStrongHold")
                queue_today.append("UpSlot9") 
                queue_today.append("UpSlot10")
                queue_today.append("UpSlot11")
                queue_today.append("UpSlot12")
                queue_today.append("UpSlot13")
                queue_today.append("UpSlot14")
                queue_today.append("UpSlot15")
                queue_today.append("UpSlot16")
            if day > 25 and day % 6 == 0: #Ore
                queue_today.append("UpSlot1")
                queue_today.append("UpSlot2")
                queue_today.append("UpSlot3")
                queue_today.append("UpSlot4")
                queue_today.append("UpSlot5")
                queue_today.append("UpSlot6")
                queue_today.append("UpSlot7")
                queue_today.append("UpSlot8")
            if day > 10 and day % 6 == 0: # Wood
                queue_today.append("UpSlot17")
                queue_today.append("UpSlot18")
                queue_today.append("UpSlot22")
                queue_today.append("UpSlot21")
                
            if day % 10 == 0:
                queue_today.append("UpWall")
            if day > 15 and day % 10 == 0: #Stone
                queue_today.append("UpSlot23")
                queue_today.append("UpSlot24")
                queue_today.append("UpSlot19")
                queue_today.append("UpSlot20")

            while len(queue_today) > 0:
                if keyboard.is_pressed('Esc'):
                    print("Hello")
                    sys.exit(0)
                    quit()
                item = queue_today.pop(0)
                if item == "Heal Wall": 
                    mouse.position = (1650,550) #Wall Button
                    mouse.click(Button.left, 1)
                    time.sleep(0.05)
                    mouse.position = (1430, 640)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot1":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.2)
                    mouse.position = (900,500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.2)
                    mouse.position = (1650,250) #Next button
                    mouse.click(Button.left, 1)
                    time.sleep(0.2)
                    mouse.position = (1300,600)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpStrongHold":
                    mouse.position = (1650,350) #Stronghold Button
                    mouse.click(Button.left, 1)
                    time.sleep(1)
                    upgradeStrongHold()
                    time.sleep(0.3)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpWall":
                    upgradeWall()
                    time.sleep(0.4)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot9":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(9):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (1300,600)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot23":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(23):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (1300,600)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot10":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(10):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (1300,600)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot11":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(11):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (1300,600)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot12":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(12):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (1300,600)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot13":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(13):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (1300,600)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot2":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(2):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (1300,600)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot3":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(3):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (1300,600)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot4":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(4):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (1300,600)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot5":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(5):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (1300,600)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot17":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(17):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (1300,600)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot18":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(18):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (1300,600)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot19":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(19):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (1300,600)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot20":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(20):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (1300,600)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot24":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(24):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (1300,600)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot22":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(22):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (1300,600)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot14":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(14):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (300,800)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot15":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(15):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (300,800)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot16":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(16):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (300,800)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot6":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(6):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (300,800)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot7":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(7):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (300,800)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot8":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(8):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (300,800)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if item == "UpSlot21":
                    mouse.position = (1650, 750)
                    mouse.click(Button.left, 1)
                    time.sleep(0.1)
                    mouse.position = (900, 500)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    for i in range(21):
                        mouse.position = (1650,250) #Next button
                        mouse.click(Button.left, 1)
                        time.sleep(0.01)
                    mouse.position = (300,800)
                    mouse.click(Button.left, 1)
                    time.sleep(0.15)
                    myScreenshot = pyautogui.screenshot()
                    icon_image = myScreenshot.convert("RGB")
                    rgb_pixel_3 = icon_image.getpixel((800, 600))
                    rgb_pixel_4 = icon_image.getpixel((1100, 600))
                    if str(rgb_pixel_3) == "(237, 28, 36)" and str(rgb_pixel_4) == "(237, 28, 36)":
                        queue_tomorrow.append(item)
                if keyboard.is_pressed('Esc'):
                    print("Hello")
                    sys.exit(0)
                    quit()
            print(queue_tomorrow)
                
        
            mouse.position = (1650, 850) # Next Day
            mouse.click(Button.left, 1)
            day += 1
            time.sleep(0.02)
            #Death and attack check
            myScreenshot = pyautogui.screenshot()
            icon_image = myScreenshot.convert("RGB")
            rgb_pixel = icon_image.getpixel((500, 600))
            rgb_pixel_2 = icon_image.getpixel((1200, 600))
            queue_today = queue_tomorrow
            queue_tomorrow = []

        
            
    

def upgradeStrongHold():
    mouse = Controller()
    mouse.position = (1380, 600) # Stronghold upgrade
    mouse.click(Button.left, 1)
    time.sleep(0.1)

def upgradeWall():
    mouse = Controller()
    mouse.position = (1650,550) #Wall Button
    mouse.click(Button.left, 1)
    time.sleep(0.05)
    mouse.position = (1300, 650) #Wall upgrade Button
    mouse.click(Button.left, 1)
    time.sleep(0.05)

def traintroops_use():
    mouse = Controller()
    mouse.position = (260, 670)
    mouse.click(Button.left, 1)

def train100troops_use():
    mouse = Controller()
    mouse.position = (260, 715)
    mouse.click(Button.left, 1)
    time.sleep(1)
    
def train1000troops_use():
    mouse = Controller()
    mouse.position = (260, 750)
    mouse.click(Button.left, 1)
    time.sleep(1) 

def traintroops(a):
    mouse = Controller()
    mouse.position = (1650, 650)
    mouse.click(Button.left, 1)
    time.sleep(0.01)
    if a == "a":
        traintroops_use()
    if a == "b":
        train100troops_use()
    if a == "c":
        train1000troops_use()

def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )

def repath(a):
    last = a.rfind("\\")
    a = a[:last+1] + "DefenceofGondorPhotos" + a[last:]
    b = "\\"
    c = "\\\\"
    a = a.replace(b,c)
    return a
    

root = tk.Tk()
root.geometry("270x150")
root.title("DoG Autoplayer")
root.resizable(False,False)

icon = repath(resource_path("IconAP.ico"))
root.iconbitmap(icon)


startButton = tk.Button(root, text = " Start ", command = start)
startButton.place(x = 135, y = 30, anchor = "center")

Notification = tk.Label(root, text =
'''
Put the Bot UI away from the corner
of the game and ensure that the top
left corner of the game is clearly visibile.
Hold "Esc" and wait until the
program terminates itself''')
Notification.place(x = 135, y = 90, anchor= "center")

root.mainloop()

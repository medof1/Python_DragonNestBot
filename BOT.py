import pyautogui
import time
import keyboard
import pydirectinput

right = 0
con, grey = 0.9, True #Confident
screen = (0,0,1024,1024) #Screen that will be processed
state,prevState = 0,0 #Switching between function
id,char,step = 0,0,0
pos = None
prevPos = None
name = 'woxe'
berak = False

#ADDITIONAL FUNCTION

def locate(image,cursor):
    global id, char, con, screen,grey,pos
    pos = pyautogui.locateCenterOnScreen(image, region= screen, grayscale= grey, confidence= con)
    if pos != None:
        if cursor == True:
            x, y = pos
            pyautogui.moveTo(x, y, 0.1) 
            if right == 1:
                pyautogui.mouseDown(button='right')
                time.sleep(.1)
                pyautogui.mouseUp(button='right')
            else:
                pyautogui.mouseDown()
                time.sleep(.1)
                pyautogui.mouseUp()
        return True
    else:
        return False
    
def refresh():
    global id,char,name,screen
    screen = (0,0,1024,1024)
    id,char = 0,0
    name = 'woxe'

def printing():
    global state, prevState, id, char
    if state != prevState:
        refresh()
        if state == 0:
            print("all function Deadactived")
        if state == 1:
            print("DN_Create Character actived")
        if state == 2:
            print("DN_Delte Character activated")
        if state == 3:
            print("DN_Auto Roulete activated")
        if state == 4:
            print("DN_Auto Sunset activated")
        if state == 5:
            print("DN_Auto Sunset Master activated")
        if state == 6:
            print("DN_Auto Sunset Abyss activated")
        if state == 7:
            print("GTA_Auto Tanam activated")
        if state == 8:
            print("Auto Click activated")
        if state == 9:
            print("Auto Swim activated")
        if state == 98:
            print("Ready to function")
        if state == 99:
            print("Function is completed")
            state = 0
        if state == 100:
            print("Function is under construction")
            state = 0
        prevState = state

def switch():
    global state
    if keyboard.is_pressed('ctrl+shift+num 0') == True:
        state = 0   
        printing()    
    elif keyboard.is_pressed('ctrl+shift+num 1') == True:
        state = 1 
        printing()        
    elif keyboard.is_pressed('ctrl+shift+num 2') == True:
        state = 2    
        printing()    
    elif keyboard.is_pressed('ctrl+shift+num 3') == True:
        state = 3
        printing()
    elif keyboard.is_pressed('ctrl+shift+num 4') == True:
        state = 4
        printing()
    elif keyboard.is_pressed('ctrl+shift+num 5') == True:
        state = 5
        printing()
    elif keyboard.is_pressed('ctrl+shift+num 6') == True:
        state = 6
        printing()
    elif keyboard.is_pressed('ctrl+shift+num 7') == True:
        state = 7
        printing()
    elif keyboard.is_pressed('ctrl+shift+num 8') == True:
        state = 8
    elif keyboard.is_pressed('ctrl+shift+num 9') == True:
        state = 9
        printing()

def alttab(tab):
    if tab >= 1 and tab <= 4:
        pydirectinput.keyDown('alt')
        time.sleep(.1)
        pydirectinput.keyDown('tab')
        time.sleep(.1)
        pydirectinput.keyUp('tab')
        time.sleep(.1)
        pydirectinput.keyUp('alt')
        time.sleep(.1)
            
#MAIN FUNCTION    

def undercons():
    global state
    time.sleep(1)
    state = 100
    printing()

def createCharacter():
    global id, char, state, name, con, screen, berak
    if id == 0:
        name = 'lllIlIlIl'
    if id == 1:
        name = 'lIlllIlIl'
    if id == 2:
        name = 'lIlIlllIl'
    if id == 3:
        name = 'lIlIlIlll'
    locate('createCharacter.png',True)
    if locate('warrior.png',False) == True and locate('gesture.png',False) == False:
        locate('academic.png',True)
        locate('create.png',True)
    if locate('eyeColor.png',False) == True:
        if locate('nameBox.png',True) == True:
            pyautogui.write(name+str(char))
            time.sleep(.1)
            pyautogui.press('enter')
            print(".id:", id, "char:", char)
            if char >= 6:
                char = 0
                id += 1
                alttab(id)
                if id >= 4:
                    id = 0
                    state = 99
                    printing()
                    #berak = True
            else:
                char += 1

def deleteCharacter():
    global char, id, state
    if locate('deleteCharacter.png',False) == True:
        locate('boxDelete.png',True)
        pyautogui.write('Delete Character')
        time.sleep(.1)
        pyautogui.press('enter')
        char += 1
    elif char >= 7:
        char = 0
        id += 1
        alttab(id)
        if id >= 4:
            id = 0
            state = 99
            printing()
    elif locate('academic1.png',False) == True:
        locate('delete.png',True)
    
    #else:
    #    alttab(1)

def autoRoulete():
    global prevPos
    prevPos = pyautogui.position()
    x, y = prevPos
    if locate('okRolet.png',True) == True:
        print("Clicking ok")
        pyautogui.moveTo(x, y)
    elif locate('spin.png',False) == True:
        locate('autoSpin.png',True)
        print("Auto spining")
        pyautogui.moveTo(x, y)

def autoSunset():
    if locate('CloisterMenu.png',False) == True and locate('CloisterMenu1.png',False) == True:
        pydirectinput.keyDown('w')
        time.sleep(.1)
    if locate('normal.png',False) == True:
        pydirectinput.keyUp('w')
        time.sleep(.1)
        locate('enter.png',True)
        print("Entering Sunset")
    if locate('f12.png',True) == True and locate('where.png', False) == False:
        pydirectinput.keyDown('ctrl')
        time.sleep(.1)
        pydirectinput.keyUp('ctrl')
        time.sleep(.1)
        print("Clicking f12")
    if locate('enterance.png',True) == True:
        print("Clicking Stage enterance")

def autoSunsetMaster():
    if locate('CloisterMenu.png',False) == True and locate('CloisterMenu1.png',False) == True:
        pydirectinput.keyDown('w')
        time.sleep(.1)
    if locate('master.png',True) == True:
        pydirectinput.keyUp('w')
        time.sleep(.1)
        print("Clicking master")
    elif locate('master1.png',False) == True:
        locate('enter.png',True)
        print("Entering Sunset")
    if locate('f12.png',True) == True and locate('where.png', False) == False:
        pydirectinput.keyDown('ctrl')
        time.sleep(.1)
        pydirectinput.keyUp('ctrl')
        time.sleep(.1)
        print("Clicking f12")
    if locate('enterance.png',True) == True:
        print("Clicking Stage enterance")

def autoSunsetAbyss():
    if locate('CloisterMenu.png',False) == True and locate('CloisterMenu1.png',False) == True:
        pydirectinput.keyDown('w')
        time.sleep(.1)
    if locate('abyss.png',True) == True:
        pydirectinput.keyUp('w')
        time.sleep(.1)
        print("Clicking abyss")
    elif locate('abyss1.png',False) == True:
        locate('enter.png',True)
        print("Entering Sunset")
    if locate('f12.png',True) == True and locate('where.png', False) == False:
        pydirectinput.keyDown('ctrl')
        time.sleep(.1)
        pydirectinput.keyUp('ctrl')
        time.sleep(.1)
        print("Clicking f12")
    if locate('enterance.png',True) == True:
        print("Clicking Stage enterance")

def autoTanam():
    pydirectinput.keyDown('w')
    pydirectinput.keyDown('alt')
    pydirectinput.keyDown('1')
    time.sleep(.01)
    pydirectinput.keyUp('1')
    time.sleep(.01)
 
def autoClick():
    pydirectinput.leftClick()
    print("Clicking")
    time.sleep(.5)

def autoSwim():
    pydirectinput.keyDown('w')
    pydirectinput.keyDown('a')
    print("Swimmin")
    time.sleep(.5)
    
print("""Command List (Press ctrl + shift + number below):
num 0: Deadactive all function
num 1: DN_Create Character
num 2: DN_Delete Character
num 3: DN_Auto Roulete
num 4: DN_Auto Sunset
num 5: DN_Auto Sunset Master
num 6: DN_Auto Sunset Abyss
num 7: GTA_Auto Tanam
num 8: Auto Click
num 9: TOF_Auto Swim
""")
while(1):
    if state == 0:
        time.sleep(.5)
        if keyboard.is_pressed('ctrl+shift') == True:
            state = 98
            printing()
    elif state != 0:
        switch()
    if keyboard.is_pressed('alt') == True:
        print("Alt is pressed")
    elif state == 1:
        createCharacter()
    elif state == 2:
        deleteCharacter()
    elif state == 3:
        autoRoulete()
    elif state == 4:
        autoSunset()
    elif state == 5:
        autoSunsetMaster()
    elif state == 6:
        autoSunsetAbyss()
    elif state == 7:
        autoTanam()
    elif state == 8:
        autoClick()
    elif state == 9:
        autoSwim()
    elif berak == True:
        break

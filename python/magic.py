import pyautogui

distance = 200
while True:
    pyautogui.moveRel(distance,0,duration=0.5)
    distance -=5
    pyautogui.moveRel(0,distance,duration=0.5)
    pyautogui.moveRel(-distance,0,duration=0.5)
    distance -=5
    pyautogui.moveRel(0,-distance,duration=0.5)
    distance +=10
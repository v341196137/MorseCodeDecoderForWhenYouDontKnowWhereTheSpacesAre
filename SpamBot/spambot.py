import pyautogui, time

time.sleep(5)
while 1:
    pyautogui.typewrite("angry")
    time.sleep(0.7)
    pyautogui.press("up")
    pyautogui.press("enter")

from os import link

import pyautogui
import time



group= ['234468325515498','363916517127998','1171843326268182']

time.sleep(5)






for i in range(len(group)):
    pyautogui.hotkey('ctrl','t')
    links= 'www.facebook.com/groups/'+group[i]
  
    pyautogui.typewrite(links) 
    pyautogui.typewrite('\n') 
    print("waiting for 20 secondds \n")  
    time.sleep(20)
    pyautogui.hotkey('ctrl','f')
    pyautogui.typewrite("Exprimez-vous...") 
    pyautogui.press('enter')
    pyautogui.press('escape')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.typewrite("Salam alykom <3 .\n")
    pyautogui.typewrite("disponible iphonet.\n")
    pyautogui.typewrite("Visit l page 5lilna Message w amml commande.\n")
    pyautogui.typewrite('www.facebook.com/profile.php?id=100085250791184')
    time.sleep(10)
    pyautogui.press('Tab',presses=10)
    pyautogui.press('enter')
  
    time.sleep(20)

   
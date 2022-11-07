#Developed by github.com/gitzoomer
#This script was made for educational purposes. I do not hold any responsibility for your actions using this script.

from colorama import Fore, init
import webbrowser
import ctypes, pyautogui, os, time
from pynput.keyboard import Key, Controller

keyboard = Controller()

ascii_text = f"""{Fore.GREEN}
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@*,*,**,*,*,*,@@@@@@@@@@@@@
@@@@@@@@@.,*                .**,@@@@@@@@
@@@@@@ *,    ./////////////     ,,.@@@@@
@@@@@*,   ((((((((((((((((((((    **(@@@
@@@/*   (((((   ((((((((((((((((    *,@@
@@@,   (((((     (((((((((((((((((   , @
@@,*   (((((     (((((((((((((((((   **@
@@,,  (((((((    (((((((((((((((((   ,,@
@@**   ((((((((     ((((   (((((((   **@
@@@*   (##########           ####   **@@
@@@ *.   ##############/  ######   *, @@
@@@@*   ######################    ,,@@@@
@@@,,  (       ###########     **,@@@@@@
@@,*      **,,             *,**%@@@@@@@@
@@*,,,, @@@@@@@,,,****,**.@@@@@@@@@@@@@@ github.com/gitzoomer
"""

print(ascii_text)

contact = input('Please enter the Contact Name or Phone Number of the Contact: ') 
message = input('Please enter the message that you will be sending: ')  
messageCount = input('Please enter the amount of message you want to send: ')

messageCount = int(messageCount)

class spammer:


    def start(self):
        print("Click F to open Whatsapp, login through the QR Code, then come back to this screen.")
        while True:
            #if keyboard.is_pressed("F"):
                url = "https://web.whatsapp.com/"
                webbrowser.open(url, new=0, autoraise=True)
                input("Press Enter to continue when you're logged in and on the homepage of whatsapp...")
                time.sleep(10)
                break

    def main(self):
        #if keyboard.is_pressed("F"):
        keyboard.press(Key.alt_l)
        keyboard.press('k')
        keyboard.release('k')
        keyboard.release(Key.alt_l)
        time.sleep(1)
        keyboard.type(contact)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(1)
        for x in range(messageCount):
            keyboard.type(message)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(0.05)

obj = spammer()
obj.start()
obj.main()

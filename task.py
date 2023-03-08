"""Class that models the tasks the assistant can do"""

from util import terminal_print
from AppOpener import run

from pynput.keyboard import Key, Controller
from time import sleep
import os
from pywinauto import Desktop
import win32gui, win32com.client
import pyautogui


class Task():

    def __init__(self, assistant_name):
        self.task_list = [assistant_name, "open presentation", "next", "previous", "temperature", "time", "date", 'thank you', "open new", "minimise", "close", "new word file", "open", "active", "maximise", "mode"]
        self.assistant_name = assistant_name
        self.keyboard = Controller()
        

    def identify_task(self, text: str) -> int:
        terminal_print("I am here")
        terminal_print(text)
        terminal_print(self.task_list)
        for task_index, task in enumerate(self.task_list):
            if task in text:
                return task_index
        
        return -127
    
            
    def loadwindowslist(self, hwnd, topwindows):
        topwindows.append((hwnd, win32gui.GetWindowText(hwnd)))
        
    
    def findandshowwindow(self, swinname, bshow, bbreak):
        topwindows = []

        win32gui.EnumWindows(self.loadwindowslist, topwindows)

        for hwin in topwindows:
            sappname = str(hwin[1])
            if swinname in sappname.lower():
                nhwnd = hwin[0]
                print(type(nhwnd))
                print(">>> Found: " + str(nhwnd) + ": " + sappname)
                if(bshow):
                    win32gui.ShowWindow(nhwnd, 5)
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shell.SendKeys('%')
                    win32gui.SetForegroundWindow(nhwnd)
                if(bbreak):
                    break


    def focus(self, string):
        string = string.split(" ")[-1]
        lista = []

        windows = Desktop(backend="uia").windows()

        for w in windows:
            lista.append(w.window_text().lower())
            print(w.window_text())

        print(f"{lista} nr 1")
        print(string)

        # ---------- change the name of word and powerpoint -----------
        i=0

        while i < len(lista):
            print("a intrat in while")
            if("powerpoint" in lista[i]):
                lista[i] = "powerpoint"
                print("am gasit powerpoint")

            if("word" in lista[i]):
                lista[i] = "word"
                print("am gasit word")
        
            i=i+1

        # ---------------------------------------------------

        print(f"{lista} nr 2")

        if string in lista:
            self.findandshowwindow(string, True, True)
            print(f"{string} exist")

        else:
            print("doesn't exist")

    
    def open(self, string):
        
        string = string.split(" ")[-1]
        print("se executa functia open")

        if(string == "powerpoint"):
            print("a intrat in powerpoint")
            os.system("start powerpnt")

        if(string == "word"):
            print("a intrat in word")
            os.system("start winword")

        else:
            print(f"a intrat in {string}")
            run(string)


    def open_new_file(self, string):
        string = string.split(" ")[-1]

        if(string == "powerpoint"):
            os.system("start powerpnt /B")

        if(string == "word"):
            os.system("start winword /w")

     
    def minimise(self):
        pyautogui.keyDown("win")
        pyautogui.keyDown("down")
        pyautogui.keyUp("down")
        pyautogui.keyUp("win")   
    

    def maximise(self):
        pyautogui.keyDown("win")
        pyautogui.keyDown("up")
        pyautogui.keyUp("up")
        pyautogui.keyUp("win")

        
    def open_presentation(self, string):

        string = string.split(" ")[-1]

        leter = "C"
        path = "C:\projectsPowerPoint"
        file = f"{string}.pptx"
        print(file)

        # descoperire NOUA !!!
        os.system(f"start powerpnt /{leter} {path}/{file}")


    def presentation_mode(self):
        pyautogui.keyDown("win")
        pyautogui.keyDown("f5")
        pyautogui.keyUp("f5")
        pyautogui.keyUp("win") 

    
    def close_file(self):
        terminal_print("Se executa functia close_file")
        sleep(1)

        # combination = {Key.alt, Key.f4}
        print("se inchide")
        self.keyboard.press(Key.alt)
        self.keyboard.press(Key.f4)
        self.keyboard.release(Key.alt)
        self.keyboard.release(Key.f4)
        print("s-a inchis")

    
    def next_slide(self):
        terminal_print("Se executa functia next_slide")
        sleep(1)
        
        self.keyboard.press(Key.down)
        self.keyboard.release(Key.down)


    def previous_slide(self):
        terminal_print("Se executa functia previous_slide")
        sleep(1)
        self.keyboard.press(Key.up)
        self.keyboard.release(Key.up)

    def get_temperature(self):
        terminal_print("Se executa functia get_temperature")
    

    def time(self):
        terminal_print("Se executa functia time")
    

    def date(self, data):
        terminal_print("Se executa functia date")
        terminal_print(data)

    
    def thank_you(self):
        terminal_print("Se executa functia thank you")
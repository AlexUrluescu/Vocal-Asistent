"""Class that models the tasks the assistant can do"""

from util import terminal_print
from AppOpener import run

from pynput.keyboard import Key, Controller
from time import sleep
import os
from pywinauto import Desktop
import win32gui, win32com.client


class Task():

    def __init__(self, assistant_name):
        self.task_list = [assistant_name, "powerpoint", "next", "previous", "temperature", "time", "date", 'thank you', "open word", "open new", "close", "new word file", "open", "active"]
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
            print("a intrat 1")
            sappname = str(hwin[1])
            if swinname in sappname.lower():
                print("a intrat 2")
                nhwnd = hwin[0]
                print(type(nhwnd))
                print(">>> Found: " + str(nhwnd) + ": " + sappname)
                if(bshow):
                    print("a intrat 3")
                    win32gui.ShowWindow(nhwnd, 5)
                    print("a intrat 4")
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shell.SendKeys('%')
                    win32gui.SetForegroundWindow(nhwnd)
                    print("a intrat 5")
                if(bbreak):
                    break


    def focus(self, string):
        string = string.split(" ")[-1]
        lista = []

        windows = Desktop(backend="uia").windows()

        for w in windows:
            lista.append(w.window_text().lower())
            print(w.window_text())

        print(lista)
        print(string)

        if string in lista:
            self.findandshowwindow(string, True, True)
            print(f"{string} exist")

        else:
            print("doesn't exist")
    

    def open_word(self):
        os.system("start winword")

    
    def new_word_file(self):
        os.system("start winword /w")


    def open_app(self, string):
        string = string.split(" ")[-1]
        terminal_print(f"se deschide {string}")

        os.system("start powerpnt")
     
        # run(string)

        
    def open_PowerPointfile(self, string):

        string = string.split(" ")[-1]

        leter = "C"
        path = "C:\projectsPowerPoint"
        file = f"{string}.pptx"
        print(file)

        # descoperire NOUA !!!
        os.system(f"start powerpnt /{leter} {path}/{file}")


    def open_new_project(self):
        os.system("start powerpnt /B")

    
    def close_file(self):
        terminal_print("Se executa functia close_file")
        sleep(2)

        # combination = {Key.alt, Key.f4}
    
        self.keyboard.press(Key.alt)
        self.keyboard.press(Key.f4)
        self.keyboard.release(Key.alt)
        self.keyboard.release(Key.f4)

    
    def next_slide(self):
        terminal_print("Se executa functia next_slide")
        sleep(1)
        # self.keyboard.press("a")
        # self.keyboard.release("a")
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
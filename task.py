"""Class that models the tasks the assistant can do"""

from util import terminal_print
from AppOpener import run

from pynput.keyboard import Key, Controller
from time import sleep
import os
from pywinauto import Desktop
import win32gui, win32com.client
import pyautogui
import requests
import os.path
from datetime import date, datetime

class Task():

    def __init__(self, assistant_name):
        self.task_list = [assistant_name, "open my presentation", "next", "previous", "temperature", "time", "date", 'thank you', "open new", "minimise", "close", "new word file", "open", "active", "maximise", "mode", "finish", "about", "maps", 'weather', 'shopping', 'add', 'directory']
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
    
    def shopping_list(self):
        state = False

        if(os.path.isfile("./shopping_list.txt") == False):
            file = open("shopping_list.txt", "x")
            print("s-a creat")

            file.close()

        elif(os.path.isfile("./shopping_list.txt")):
            state = True
            print("it's ready")

        print('shopping list apelat')
        return state
    

    def add_products(self, text):
        string = text.split(" ")[-1]
                
        file = open("shopping_list.txt", "a")
        file.write(f"{string}\n")

        return string
    
            
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

            if("visual studio code" in lista[i]):
                lista[i] = "code"
                print("am gasit visual studio code")

            if("edge" in lista[i]):
                lista[i] = "microsoft"
                print("am gasit edge")
        
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

        if(string == "microsoft"):
            print("a intrat in microsoft")
            os.system("start msedge")

        else:
            print(f"a intrat in {string}")
            run(string)


    def open_new_file(self, string):
        string = string.split(" ")[-1]

        if(string == "powerpoint"):
            os.system("start powerpnt /B")

        if(string == "word"):
            os.system("start winword /w")

    def new_word_file(self):
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


    def open_my_presentation(self):
        print("open_mt_presentation is activ")

        path = "C:\projectsPowerPoint"
        files = os.listdir(path)
        list = []

        for file in files:
            size = len(file)
            file = file[:size - 5]
            print(file)
            if "_" in file:
                file = file.replace("_", " ")
            list.append(file)

        print(files)
        print(list)

        return list, path, files
    

    def presentation_mode(self):
        pyautogui.keyDown("win")
        pyautogui.keyDown("f5")
        pyautogui.keyUp("f5")
        pyautogui.keyUp("win")

    
    def finish_presentation(self):
        pyautogui.keyDown("esc")
        pyautogui.keyUp("esc")
        print("finish a mers")

    
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

    def get_temperature(self, string):

        string = string.split(" ")[-1]

        terminal_print("Se executa functia get_temperature")

        api_key = "55c8bfaf9fff464f3bf6f3c283186dc6"
        city = string

        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
        
        data = weather_data.json()
        print(data)
        temp = data['main']['temp']
        temp = int(temp) / 3.78
        print(temp)

        return int(temp)
    
    
    def weather(self, string):
        city = string.split(" ")[-1]
        print(f"Weather in {city}")

        api_key = "55c8bfaf9fff464f3bf6f3c283186dc6"

        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

        weather_data = weather_data.json()

        temperature = round(int(((weather_data['main']['temp'])-32) * 5) / 9)
        main = weather_data['weather'][0]['main']

        print(weather_data)
        print(main)
        print(temperature)
    
        return main, temperature

    # def weather(self, text):
    #     self.task_weather_manager()

    def get_country(self, string):
        string = string.split(" ")[-1]
        print("se activeaza get_country")

        # country_data = requests.get(
        #     f"https://restcountries.com/v3.1/name/{string}?fullText=true")
        
        # country_data = country_data.json()
        # print(country_data)

        # population = str(country_data[0]['population'])
        # if(len(population) == 9):
        #     population = population[0:3]
        # elif(len(population) == 8):
        #     population = population[0:2]
        
        # elif(len(population) == 7):
        #     population = population[0:1]

        # name = country_data[0]['name']['common']
        # capital = country_data[0]['capital'][0]
       
        # subregion = country_data[0]['subregion']
 
        # print(country_data)
        # print(population)
        # print(name)
        # print(capital)
        # print(region)
        # print(subregion)

        # return population, capital, region, subregion
    

    def open_maps(self, string):
        string = string.split(" ")[-1]

        country_data = requests.get(
            f"https://restcountries.com/v3.1/name/{string}?fullText=true")
        
        country_data = country_data.json()

        country_maps = country_data[0]['maps']['googleMaps']

        print(country_maps)

        return country_maps
    

    def time(self):
        terminal_print("Se executa functia time")
        now = datetime.now()
        ora = now.strftime("%H:%M:%S")

        return ora
    

    def date(self):
        terminal_print("Se executa functia date")
        data = date.today()

        return data

    
    def thank_you(self):
        terminal_print("Se executa functia thank you")
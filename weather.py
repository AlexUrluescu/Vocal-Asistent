
from util import terminal_print
from AppOpener import run

from pynput.keyboard import Key, Controller
from time import sleep
import os
from pywinauto import Desktop
import win32gui, win32com.client
import pyautogui
import requests

class Weather():
        def __init__(self, assistant_name):
            # self.task_list = [assistant_name, "open presentation", "next", "previous", "temperature", "time", "date", 'thank you', "open new", "minimise", "close", "new word file", "open", "active", "maximise", "mode", "finish", "about", "maps", 'weather']

            self.task_weather = [assistant_name,'hello', "temperature", "details", "wind"]
            self.assistant_name = assistant_name
            # self.keyboard = Controller()

        def identify_weather_task(self, text: str) -> int:
            terminal_print("I am here")
            terminal_print(text)
            terminal_print(self.task_weather)
            for task_index, task in enumerate(self.task_weather):
                if task in text:
                    return task_index
            
            return -127
        

        def hello_weather(self):
             print("Hello from weather.py")
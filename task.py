"""Class that models the tasks the assistant can do"""

from util import terminal_print
from AppOpener import run

from pynput.keyboard import Key, Controller
from time import sleep
import os

class Task():

    def __init__(self, assistant_name):
        self.task_list = [assistant_name, "open", "next", "previous slide", "temperature", "time", "date", 'thank you']
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



    def open_app(self, string):
        string = string.split(" ")[-1]
        terminal_print(f"se deschide {string}")

        leter = "C"
        path = "C:\projectsPowerPoint"
        file = "prezentare.pptx"

        # descoperire NOUA !!!
        os.system(f"start powerpnt /{leter} {path}/{file}")
     
        # run(string)
        


    
    def next_slide(self):
        terminal_print("Se executa functia next_slide")
        sleep(5)
        self.keyboard.press("a")
        self.keyboard.release("a")
        self.keyboard.press(Key.right)
        self.keyboard.release(Key.right)


    def previous_slide(self):
        terminal_print("Se executa functia previous_slide")
        sleep(5)
        self.keyboard.press(Key.left)
        self.keyboard.release(Key.left)

    def get_temperature(self):
        terminal_print("Se executa functia get_temperature")
    

    def time(self):
        terminal_print("Se executa functia time")
    

    def date(self, data):
        terminal_print("Se executa functia date")
        terminal_print(data)

    
    def thank_you(self):
        terminal_print("Se executa functia thank you")
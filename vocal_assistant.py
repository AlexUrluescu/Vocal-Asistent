"""File that contains the vocal assitant class"""
from time import sleep
import speech_recognition as sr
import pyttsx3
import os
from pynput.keyboard import Key, Controller
from AppOpener import run
from util import terminal_print
import task 
from datetime import date, datetime

class Assistent():
    def __init__(self, name: str, gender: str, speech_speed: int = 125):
        self.name = name
        self.gender = gender
        self.speech_speed = speech_speed
        self.engine_speak = pyttsx3.init()
        self.engine_speak.setProperty('rate', self.speech_speed)
        self.engine_keyboard = Controller()
        self.task_manager = task.Task(self.name.lower())

    
    def write(self, text):
        """function that writes a text on the screen"""
        sleep(2)
        self.engine_keyboard.type(text)


    def speak(self, text: str) -> None:
        """ Function that converts a text to speak """
        self.engine_speak.say(text)
        self.engine_speak.runAndWait()


    def get_audio(self):
        """Function that get the audio"""
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                terminal_print(said)
            except Exception as e:
                print("Exception: " + str(e))
                said = "Sorry, could not undersand you"

        return said

        
    def change_name(self, new_name):
        self.name = new_name
        return "Now the assistent's name it's " + new_name
    
    
    def get_name(self):
        return self.name
    
    
    def change_gender(self, new_gender):
        self.gender = new_gender
        terminal_print(f"The gender of the assitent was changed to {new_gender}")
    
    
    def get_gender(self):
        terminal_print(f"The gender of the assistent {self.name} is {self.gender}")
        return self.gender
    
    
    def change_speech_speed(self, new_speed):
        self.speech_speed = new_speed
        self.engine_speak.setProperty('rate', self.speech_speed)
        terminal_print(f"The speed was changet to  + {new_speed}")
    
    
    def get_speech_speed(self):
        terminal_print(f"The speed is {self.speech_speed}")
        return self.speech_speed
    

    def run_task(self, task_index, text):
        if task_index == 0:
            self.speak('What can I do for you?')
        
        if task_index == 1:
            self.task_manager.open_app(text)

            sleep(2)
            self.speak("Your App was open successfully")
        
        if task_index == 2:
            self.task_manager.next_slide()
        
        if task_index == 3:
            self.task_manager.previous_slide()

        if task_index == 4:
            self.task_manager.get_temperature()

        if task_index == 5:
            now = datetime.now()
            ora = now.strftime("%H:%M:%S")
            self.speak(ora)
            self.task_manager.time()

        if task_index == 6:
            data = date.today()
            self.speak(data)
            self.task_manager.date(data)

        if task_index == 7:
            self.speak('You welcome')

        if task_index == 8:
            self.speak("I will open a new file")
            self.task_manager.open_new_file(text)

        if task_index == 9:
            self.speak("I will minimize the window")
            self.task_manager.minimise()

        if task_index == 10:
            self.speak("I will close the file")
            self.task_manager.close_file()

        if task_index == 11:
            self.speak("I will open a new word file")
            self.task_manager.new_word_file()

      
        if task_index == 12:
            # self.task_manager.open_PowerPointfile(text)
            self.speak("I will open the file")
            self.task_manager.open(text)


        if task_index == 13:
            self.speak("Focus active")
            self.task_manager.focus(text)


        if task_index == 14:
            self.speak("I will maximize the window")
            self.task_manager.maximise()     
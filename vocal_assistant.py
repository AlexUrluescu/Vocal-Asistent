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
import webbrowser
# import weather

class Assistent():
    def __init__(self, name: str, gender: str, speech_speed: int = 100):
        self.name = name
        self.gender = gender
        self.speech_speed = speech_speed
        self.engine_speak = pyttsx3.init()
        self.engine_speak.setProperty('rate', self.speech_speed)
        self.engine_keyboard = Controller()
        self.task_manager = task.Task(self.name.lower())
        # self.task_weather_manager = weather.Weather(self.name.lower())

    
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
            list, path, files = self.task_manager.open_my_presentation()
            size = len(list)
            leter = "C"

            if size == 1:
                file = list[0]
                self.speak(f"You have {size} file in the folder")
                self.speak(f"{file}")
                os.system(f"start powerpnt /{leter} {path}/{files[0]}")

            else:
                i=1
                self.speak(f"You have {size} files in the folder")
                for project in list:
                    self.speak(f"Say {i} for open {project}")
                    i = i + 1

            text = self.get_audio()
            print(type(text))
            
            if text == "1":
                self.speak(f"I will open {list[0]}")
                os.system(f"start powerpnt /{leter} {path}/{files[0]}")
            
            if text == "2":
                self.speak(f"I will open {list[1]}")
                os.system(f"start powerpnt /{leter} {path}/{files[1]}")

        
        if task_index == 2:
            self.task_manager.next_slide()
        
        if task_index == 3:
            self.task_manager.previous_slide()

        if task_index == 4:
            string = text.split(" ")[-1]

            temp = self.task_manager.get_temperature(text)

            self.speak(f"In {string} are {temp} degrees")

        if task_index == 5:
            ora = self.task_manager.time()
            self.speak(ora)


        if task_index == 6:
            data = self.task_manager.date()
            self.speak(data)


        if task_index == 7:
            self.speak('You welcome')

        if task_index == 8:
            self.speak("I will open a new file")
            self.task_manager.open_new_file(text)

        if task_index == 9:
            self.speak("I will minimize the window")
            self.task_manager.minimise()

        if task_index == 10:
            self.speak("I will close the window")
            self.task_manager.close_file()

        if task_index == 11:
            # say "create a new word file"
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

        if task_index == 15:
            self.speak("I will active the presentation mode")
            self.task_manager.presentation_mode() 

        if task_index == 16:
            self.speak("I will deactivate the presentation mode")
            self.task_manager.finish_presentation()

        if task_index == 17:
            string = text.split(" ")[-1]
            print(string)
            self.speak(f"Details about {string}")
            self.task_manager.get_country(text)

            # population, capital, region, subregion = self.task_manager.get_country(text)

            # self.speak(f"{string} is in {region}, exacty in {subregion}")
            # sleep(0.3)
            # self.speak(f"{string} has {population} milion of people, and the capital is {capital}")

        
        if task_index == 18:
            string = text.split(" ")[-1]

            self.speak(f"I will open maps for {string}")

            country_maps = self.task_manager.open_maps(text)

            webbrowser.open(country_maps)

        if task_index == 19:
            string = text.split(" ")[-1]

            main, temperature = self.task_manager.weather(text)

            if(main == "Clouds"):
                main = "cloudy"

            elif(main == "Mist"):
                main = "misty"

            elif(main == "Fog"):
                main = "fogy"

            self.speak(f"In {string} the weather is {main} and are {temperature} degrees")

        
        if task_index == 20:
            state = self.task_manager.shopping_list()

            if(state):
                self.speak("The shopping list it's ready")
            
            else:
                self.speak("The shopping list was created")

            sleep(0.2)
            self.speak("What do you want to add?")

        
        if task_index == 21:
            string = self.task_manager.add_products(text)

            print(string)
            self.speak(f"{string} was added in your shopping list")

        if task_index == 22:
            files = self.task_manager.get_files()
            size = len(files)

            self.speak(f"You have {size} projects in the folder")
   

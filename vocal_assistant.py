"""File that contains the vocal assitant class"""
from time import sleep
import speech_recognition as sr
import pyttsx3
import os
from AppOpener import run

class Assistent():
    def __init__(self, name: str, gender: str, speech_speed: int = 1.25):
        self.name = name
        self.gender = gender
        self.speech_speed = speech_speed


    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def get_audio():

        
    def change_name(self, new_name):
        self.name = new_name
        return "Now the assistent's name it's " + new_name
    
    
    def get_name(self):
        return "Hello there ! My name is " + self.name
    
    
    def change_gender(self, new_gender):
        self.gender = new_gender
        return "The gender of the assitent was changed to " + new_gender
    
    
    def get_gender(self):
        return "The gender of the assistent " + self.name + " is " + self.gender
    
    
    def change_speech_speed(self, new_speed):
        self.speech_speed = new_speed
        return "The speed was changet to " + new_speed
    
    
    def get_speech_speed(self):
        return "The speed is " + self.speech_speed
    
    
    def listen_for_request(self):
        return "Hello there ! My name is " + self.name + ", how can I help you ?"
    
    
    def execute_request(self):
        return "Your request will be execute"
   
    
x = Assistent("John", "Ana", 2)

x.speak("Hey there, my name is" + self.name)

x.sleep(0.5)
x.speak("Just say, Hey Helen, and I'll see what I can do for you.")

while True:
    text = get_audio().lower();



# ----------- test ------------------

print(x.change_name("Pedro"))
print(x.change_gender("female"))
print(x.get_gender())
print(x.listen_for_request())
print(x.execute_request())

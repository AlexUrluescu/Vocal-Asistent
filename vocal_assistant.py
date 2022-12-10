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
        self.engine_speak = pyttsx3.init()


    def speak(self, text):
        self.engine_speak.say(text)
        self.engine_speak.runAndWait()

    def get_audio(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
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
   
    
    def welcome(self):
        return "You welcome"

    
    def like(self):
        return "I like to help you and make you life easier"


    def kind_response(self):
        return "This is my job, I will be always with you"
    
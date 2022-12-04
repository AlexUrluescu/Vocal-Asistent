from time import sleep
import speech_recognition as sr
import pyttsx3
import os
from AppOpener import run

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
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

speak("Hello there! I am a computer, and my name is Helen.")
sleep(0.5)
speak("Just say, Hey Helen, and I'll see what I can do for you.")
    
while True:
    text = get_audio().lower()
    if "helen" in text:
        speak("What can I do for you?")
        text = get_audio().lower()
        if "stop" in text:
            speak(f"I will stop now. Bye bye!")
            break
        if "open" in text and "sorry" not in text:
            print(text)
            speak(f"OK, {text}")
            app_to_open = text[5:]
            try:
                run(app_to_open)
            except Exception as e:
                print(e)
                speak(app_to_open)
    


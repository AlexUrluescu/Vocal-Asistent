from vocal_assistant import *

x = Assistent("Helen", "female", 200)

x.speak(f"Hey there, my name is {x.get_name()}" )

sleep(0.5)
x.speak(f"Just say, Hey {x.get_name()}, and I'll see what I can do for you.")

x.write("Welcome Carina")

while True:
    text = x.get_audio().lower()
    if "helen" in text:
        x.speak("What can I do for you")
        text = x.get_audio().lower()
        x.write(text)
        if "gender" in text:
            x.speak({x.get_gender()})
            x.speak("Do you want to know anything else")
            text = x.get_audio().lower()
            if "no" in text and "thank" in text:
                x.speak(x.welcome())
                break
            if "yes" in text:
                x.speak("What can I do for you")
                text = x.get_audio().lower()
        if "like" in text:
            x.speak(x.like())
            text = x.get_audio().lower()
            if "kind" in text and "helen" in text:
                x.speak(x.kind_response())
        if "name" in text:
            x.speak("My names is " + x.get_name())
        if "stop" in text:
            x.speak(f"I will stop now. Bye bye!")
            break
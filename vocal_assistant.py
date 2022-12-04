"""File that contains the vocal assitant class"""


class Assistent():
    def __init__(self, name: str, gender: str, speech_speed: int = 1.25):
        self.name = name
        self.gender = gender
        self.speech_speed = speech_speed
        
    def change_name(self, new_name):
        self.name = new_name
    
    
    def get_name(self):
        return self.name
    
    
    def change_gender(self, new_gender):
        pass
    
    
    def get_gender(self):
        pass
    
    
    def change_speech_speed(self, new_speed):
        pass
    
    
    def get_speech_speed(self):
        pass
    
    
    def listen_for_request(self):
        pass
    
    
    def execute_request(self):
        pass
    
    
x = Assistent("John", "male", 3)

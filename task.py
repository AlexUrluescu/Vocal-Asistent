"""Class that models the tasks the assistant can do"""

from util import terminal_print


class Task():


    def __init__(self, assistant_name):
        self.task_list = [assistant_name, "open", "next slide", "previous slide", "temperature", "time", "date", 'thank you']
        self.assistant_name = assistant_name
        

    def identify_task(self, text: str) -> int:
        terminal_print("I am here")
        terminal_print(text)
        terminal_print(self.task_list)
        for task_index, task in enumerate(self.task_list):
            if task in text:
                return task_index
        
        return -127



    def open_app(self):
        terminal_print("se executa functia open_app")

    
    def next_slide(self):
        terminal_print("Se executa functia next_slide")


    def previous_slide(self):
        terminal_print("Se executa functia previous_slide")
    

    def get_temperature(self):
        terminal_print("Se executa functia get_temperature")
    

    def time(self):
        terminal_print("Se executa functia time")
    

    def date(self, data):
        terminal_print("Se executa functia date")
        terminal_print(data)

    
    def tank_you(self):
        terminal_print("Se executa functia thank you")
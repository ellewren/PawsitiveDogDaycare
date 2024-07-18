import random
from  datetime import datetime

#Parent class holding list of workers and attributes needed by child classes
class Services:

    worker = ["Ashley", "Jeffery", "Collin", "Shelly", "Gabriel", "Amy", "Edward", "Amilia", "Rocko", "Jamal", "Harry"]

    def __init__(self,date=None):
        self.date = date or datetime.now().strftime("%m-%d-%Y")
        self.selected_worker = random.choice(self.worker)


#Child cases defined with shared attributes inherited from Services super class
#static method used because methods do not modify class or require data from an instance

class Grooming(Services):
    def __init__(self):
        super().__init__()
        
    @staticmethod
    def nails_trimmed(selected_dog, selected_worker):
        return f"{selected_worker} has {selected_dog.name}'s nails short and proper."
    
    @staticmethod
    def haircut(selected_dog, selected_worker):
        return f"{selected_worker} has {selected_dog.name}'s coat looking great."
    
    @staticmethod
    def bathing(selected_dog, selected_worker):
        return f"{selected_worker} has {selected_dog.name} smelling fresh and clean after a bath."
    

class Training(Services):
    def __init__(self,date=None):
        super().__init__(date)
   
    @staticmethod
    def obedience_training(selected_dog, selected_worker, date):
        return f"{selected_dog.name} is learning to sit, stay, and lay with trainer {selected_worker} on {date}"


class Boarding(Services):
    def __init__(self,date=None):
        super().__init__(date)

    @staticmethod
    def check_in(selected_dog, selected_worker, date):
        return f"{selected_dog.name} has been checked in on {date} by {selected_dog.owner_fname} {selected_dog.owner_lname} and is being attended to by {selected_worker}"
    
    @staticmethod
    def check_out(selected_dog, date):
        return f"{selected_dog.name} had been checked out by {selected_dog.owner_fname} {selected_dog.owner_lname} on {date}"
    
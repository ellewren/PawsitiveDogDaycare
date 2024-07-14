import random
from  datetime import datetime

#Parent class displaying general services offered at Pawsitive Stay Dog Daycare
class Services:

    worker = ["Ashley", "Jeffery", "Collin", "Shelly", "Gabriel", "Amy", "Edward", "Amilia", "Rocko", "Jamal", "Harry"]

    def __init__(self,date=None):
        self.date = date or datetime.now().strftime("%m-%d-%Y")
        self.selected_worker = random.choice(self.worker)


#Child classes used to share common attributes and demonstrate inheritance 
       
# Child class of Services with specific attributes and methods for Grooming
class Grooming(Services):
    def __init__(self, service_type, dog, date, selected_worker):
        super().__init__(service_type, dog, date, selected_worker)
        

    def nails_trimmed(selected_dog, selected_worker):
        return f"{selected_worker} has {selected_dog.dog_name}'s nails short and proper."
    
    def haircut(selected_dog, selected_worker):
        return f"{selected_worker} has {selected_dog.dog_name}'s coat looking great."
    
    def bathing(selected_dog, selected_worker):
        return f"{selected_worker} has {selected_dog.dog_name} smelling fresh and clean after a bath."
    
# Child class of Services with specific attributes and methods for Training
class Training(Services):
    def __init__(self, service_type, dog, date, trainer):
        super().__init__(service_type, dog, date)
   
    def obedience_training(selected_dog, selected_worker, date):
        return f"{selected_dog.dog_name} is learning to sit, stay, and lay with trainer {selected_worker} on {date}"

# Child class of Services with specific attributes and methods for Boarding
class Boarding(Services):
    def __init__(self, service_type, dog, date):
        super().__init__(service_type, dog, date)

    def check_in(selected_dog, selected_worker, date):
        return f"{selected_dog.dog_name} has been checked in on {date} by {selected_dog.fname} {selected_dog.lname} and is being attended to by {selected_worker}"
    
    def check_out(selected_dog, date):
        return f"{selected_dog.dog_name} had been checked out by {selected_dog.fname} {selected_dog.lname} on {date}"
    
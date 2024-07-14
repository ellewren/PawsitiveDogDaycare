


class Dog:
    def __init__(self, name, breed, age, gender, vaccination_status):
        self.name = name
        self.breed = breed
        self.age = age
        self.gender = gender
        self.vaccination_status = vaccination_status

    def to_dict(self):
        return {
            "name": self.name,
            "breed": self.breed,
            "age": self.age,
            "gender": self.gender,
            "vaccination_status": self.vaccination_status
        }
    
    

    def displaydoginfo(self):
        return f"Name: {self.name} \nBreed: {self.breed} \nAge: {self.age} \nGender: {self.gender} \nVaccination Status: {self.vaccination_status}"



        


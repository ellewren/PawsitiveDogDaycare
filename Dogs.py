


class Dog:
    def __init__(self, name, breed, age, gender, vaccination_status, owner_fname, owner_lname):
        self.name = name
        self.breed = breed
        self.age = age
        self.gender = gender
        self.vaccination_status = vaccination_status
        self.owner_fname = owner_fname
        self.owner_lname = owner_lname

    def to_dict(self):
        return {
            "name": self.name,
            "breed": self.breed,
            "age": self.age,
            "gender": self.gender,
            "vaccination_status": self.vaccination_status,
            "owner_fname": self.owner_fname,
            "owner_lname": self.owner_lname
        }
    
    

    def displaydoginfo(self):
        return f"Name: {self.name} \nBreed: {self.breed} \nAge: {self.age} \nGender: {self.gender} \nVaccination Status: {self.vaccination_status}"



        


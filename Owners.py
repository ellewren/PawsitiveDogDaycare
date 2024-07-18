from Dogs import Dog
import json 
import re

class Owner:

    # Private attribute used to maintain data integrity preventing unauthorized changes to owners
    
    __owners_dict = {}

    def __init__(self, fname, lname, email,dogs):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.dogs = dogs

    def email_validation(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b' 
        return re.fullmatch(regex, email) is not None

    # @classmethod used to manage class level data such as owners and dogs to ensure they're consistent across all instances
    # while loops used through file for data validation, user are prompter for correct response until system receives valid input 

    @classmethod
    def add_owner(cls):
        while True:
            fname = input("Enter owner's first name: ")
            if fname.isalpha():
                break
            else:
                print("Invalid input for first name. First name can only be letters")
        while True:
                lname = input("Enter owner's last name: ")
                if lname.isalpha():
                    break
                else:
                    print("Invalid input for last name. Last name can only be letters")
        while True:
            cls.load_owners()
            email = input("Enter owner's email: ")
            if not cls.email_validation(email):
                print("Invalid email format. Please enter a valid email.")
            elif email in cls.__owners_dict:
                print(f"Owner with email '{email}' already exists in the records. Please enter a different email.")
            else:
                break

        dogs = []
        while True:
                while True:
                    dog_name = input("Enter the dog's name: ")
                    if all(c.isalpha() or c.isspace() for c in dog_name) and dog_name.strip():
                        break
                    else:
                        print("Invalid input for dog's name. Name can only contain letters and spaces, and cannot be empty.")

                while True:
                    dog_breed = input("Enter the dog's breed: ")
                    if all(c.isalpha() or c.isspace() for c in dog_breed) and dog_breed.strip():
                        break
                    else:
                        print("Invalid input for dog's breed. Breed can only contain letters and spaces, and cannot be empty.")

                while True:
                    try:
                        dog_age = int(input("Enter the dog's age: "))
                        break
                    except ValueError:
                        print("Invalid input for dog's age. Please enter a valid age.")
                while True:
                    gender = input("Enter the gender of the dog (male / female): ").strip().lower()
                    if gender == "male" or gender == "female":
                        break
                    else:
                        print("Invalid input. Please enter male or female.")
                while True:        
                    vaccination_status = input("Are vaccinations current? (current/not current): ")
                    if vaccination_status == "current" or vaccination_status == "not current":
                        break
                    else:
                        print("Invalid input. Please enter current or not current")

                dogs.append(Dog(dog_name, dog_breed, dog_age, gender, vaccination_status, fname, lname))
                more_dogs = input("Do you want to add another dog? (yes/no): ").strip().lower()
                if more_dogs != "yes":
                    break


        new_owner = cls(fname, lname, email, dogs)
        cls.__owners_dict[email] = new_owner
        cls.save_owners()

        dog_names = ', '.join([dog.name for dog in dogs])
        return f"{fname} {lname}, and their pet(s) {dog_names} have been added to daycare records."
    
    # save new owner entries to json file to persist data 
    
    @classmethod
    def save_owners(cls):
        with open("daycaredata.json", "w") as json_file:
            json.dump(
                [
                    {
                        "fname": owner.fname,
                        "lname": owner.lname,
                        "email": owner.email,
                        "dogs": [dog.to_dict() for dog in owner.dogs]
                    }
                    for owner in cls.__owners_dict.values()
                ],
                json_file,
                indent=2
            )

    # load existing owners to prevent duplicates and retrieve owners and pets for services 

    @classmethod
    def load_owners(cls):
        try:
            with open("daycaredata.json", "r") as json_file:
                owners_data = json.load(json_file)
                cls.__owners_dict = {
                    owner['email']: cls(
                        owner['fname'],
                        owner['lname'],
                        owner['email'],
                        [Dog(**dog) for dog in owner['dogs']]
                    )
                    for owner in owners_data
                }
        except FileNotFoundError:
            cls.__owners_dict = {}

    # owner look up, returns owners information and registered pets 


    @classmethod
    def find_and_display_owner(cls, email):
        cls.load_owners()
        if email in cls.__owners_dict:
            owner = cls.__owners_dict[email]
            dogs_info = '\n'.join([dog.displaydoginfo() for dog in owner.dogs])
            return f"Name: {owner.fname} {owner.lname}\nContact: {owner.email}\nPets:\n{dogs_info}"
        else:
            return "Owner not found."

    # add new dog to existing owner
    
    @classmethod
    def add_dog(cls):
        cls.load_owners()
        while True:
            try:
                email = input("Enter email of the owner: ")
                if email not in cls.__owners_dict:
                    print(f"No owner found with email '{email}'.")
                else:
                    owner = cls.__owners_dict[email]
                    break  # Exit the loop once a valid owner is found
            except ValueError:
                print("Invalid email format. Please enter a valid email.")

        owner = cls.__owners_dict[email]
        while True:
                while True:
                    dog_name = input("Enter the dog's name: ")
                    if all(c.isalpha() or c.isspace() for c in dog_name) and dog_name.strip():
                        break
                    else:
                        print("Invalid input for dog's name. Name can only contain letters and spaces, and cannot be empty.")

                while True:
                    dog_breed = input("Enter the dog's breed: ")
                    if all(c.isalpha() or c.isspace() for c in dog_breed) and dog_breed.strip():
                        break
                    else:
                        print("Invalid input for dog's breed. Breed can only contain letters and spaces, and cannot be empty.")

                while True:
                    try:
                        dog_age = int(input("Enter the dog's age: "))
                        break
                    except ValueError:
                        print("Invalid input for dog's age. Please enter a valid age.")
                while True:
                    gender = input("Enter the gender of the dog (male / female): ").strip().lower()
                    if gender == "male" or gender == "female":
                        break
                    else:
                        print("Invalid input. Please enter male or female.")
                while True:        
                    vaccination_status = input("Are vaccinations current? (current/not current): ")
                    if vaccination_status == "current" or vaccination_status == "not current":
                        break
                    else:
                        print("Invalid input. Please enter current or not current")
        
                dog = Dog(dog_name, dog_breed, dog_age, gender, vaccination_status, owner.fname, owner.lname)
                owner.dogs.append(dog)
                cls.save_owners()
                
                print(f"{dog_name} added to owner {owner.fname} {owner.lname} and daycare records.")

    # retrieve owners pet/pets to select which dog will receive service 
        
    @classmethod
    def select_dog_for_service(cls):
        Owner.load_owners()
        email = input("Enter owner's email: ")

        owner = cls.__owners_dict.get(email)
        if not owner:
            print("Owner not found.")
            return None

        if not owner.dogs:
            print("No dogs found for this owner.")
            return None

        print("Select a dog for service:")
        for idx, dog in enumerate(owner.dogs):
            print(f"{idx + 1}. {dog.name} - {dog.breed} {dog.age}")

        dog_index = int(input("Enter the number of the dog: ")) - 1
        if 0 <= dog_index < len(owner.dogs):
            return owner.dogs[dog_index]
        else:
            print("Invalid selection.")
            return None
        
    












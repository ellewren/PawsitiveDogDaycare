
from Owners import Owner
from Services import Grooming, Training, Boarding, Services

def display_menu():
    print("Welcome to Pawsitive Stay Dog Daycare Management System")
    print("1. Add New Owner")
    print("2. Register For Services")
    print("3. Add New Dog to Existing Owner")
    print("4. Owner Lookup")
    print("5. Exit")

def grooming_menu():
    print("1. Grooming")
    print("2. Training")
    print("3. Boarding")
    print("4. Exit")

def register_for_services():
    Owner.load_owners()
    selected_dog = Owner.select_dog_for_service()
    if selected_dog:
        print(f"{selected_dog.dog_name} has been selected for service.")
    else:
        print("Owner or dog not found.")
        return
    
    services_instance = Services()
    selected_worker = services_instance.selected_worker
    date = services_instance.date
    
    while True:
        grooming_menu()

        choice = input("Enter your selection: ")

        if choice == "1":
            print("Select your grooming service:")
            print("1. Nail Trimming")
            print("2. Haircut")
            print("3. Bath")
            print("4. Exit")
            grooming_choice = input("Enter your grooming selection: ")

            if grooming_choice == "1":
                result = Grooming.nails_trimmed(selected_dog, selected_worker)
            elif grooming_choice == "2":
                result = Grooming.haircut(selected_dog, selected_worker)
            elif grooming_choice == "3":
                result = Grooming.bathing(selected_dog, selected_worker)
            else:
                print("Invalid grooming selection.")
                continue
            
            print(result)

        elif choice == "2":
            result = Training.obedience_training(selected_dog, selected_worker, date)
            print(result)

        elif choice == "3":
            print("1. Check-In for boarding")
            print("2. Check-out of boarding")
            boarding_choice = input("Enter boarding selection: ")
            
            if boarding_choice == "1":
                result = Boarding.check_in(selected_dog, selected_worker, date)
                print(result)
            elif boarding_choice == "2":
                result = Boarding.check_out(selected_dog, date)
                print(result)

        elif choice == "4":
            print("Exiting service registration.")
            break

        else:
            print("Invalid selection. Please select a number from the menu.")

def owner_lookup():
    email = input("Enter owner's email: ")
    Owner.load_owners()
    result = Owner.find_and_display_owner(email)
    print(result)


if __name__ == "__main__":



    while True:
        display_menu()
        choice = input("Enter your selection: ")
        if choice == "1":
            result = Owner.add_owner()
            print(result)
        elif choice == "2":
            result = register_for_services()
            print(result)
        elif choice == "3":
            Owner.add_dog()
        elif choice == "4":
            owner_lookup()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please enter a number from the menu.")

        
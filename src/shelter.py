import os
import json


base = os.path.dirname(__file__)
def get_path(filename):
    return os.path.join(base, "..", "data" , filename)
def line():
    print("-"*70)
def heading(a):
    print(a.center(30))
def pause():
    print("\n Enter To Continue ........")
def positive(x):
    while True:
        try:
            n = int(input(x))
            if n > 0: return n
        except ValueError:
            pass
        print("Enter Valid Number!")
def check_id(data, id):
    if id > max(x["id"] for x in data):
        print("No ID Found!")
        return False
    return True



def shelter():
    print('''
    1). VIEW SHELTER 
    2). REGISTER SHELTER
    3). UPDATE SHELTER STATUS
    4). ALLOCATE PERSON TO SHELTER
    ''')
    choice=int(input("Enter The Option You Want To Choose :  "))
    match choice:
        case 1:
            line(); heading("VIEW SHELTER") ; line()
            with open(get_path("shelter.json") , "r") as f:
                shelters=json.load(f)
            for s in shelters:
                print(f'''
                Shelter ID:  {s["id"]}
                Name:  {s["name"]}
                Location:  {s["location"]}
                Capacity:  {s["capacity"]}
                Occupied:  {s["occupied"]}
                Available:  {s["available"]}
                Facilities:  {s["facilities"]}
                Contact:  {s["contact"]}
                Status:  {s["status"]}
                ''')


        case 2:
            line(); heading("REGISTER SHELTER") ; line()
                       
            name = input("Enter Shelter Name: ")
            location = input("Enter Location: ")
            capacity = positive("Enter Capacity: ")
            while True:
                occupied = positive("Occupied: ")
                if occupied<=capacity:
                    break
                print("Occupied cannot be greater than capacity!")

            available = capacity - occupied
            facilities = input("Facilities : ")
            contact = input("Contact : ")
            status = input("Enter Status: ")

            with open(get_path("shelter.json"), "r") as f:
                shelter = json.load(f)

            if shelter:
                new_id = max(s["id"] for s in shelter) + 1
            else:
                new_id = 1

            new_shelter = {
                "id": new_id,
                "name": name,
                "location": location,
                "status": status,
                "capacity": capacity,
                "available": available,
                "occupied": occupied,
                "facilities": facilities,
                "contact": contact,
            }

            shelter.append(new_shelter)

            with open(get_path("shelter.json"), "w") as f:
                json.dump(shelter, f, indent=4)

            print("\nShelter Registered Successfully!")



        case 3:
            with open(get_path("shelter.json"), "r") as f:
                shelter = json.load(f)

            id = positive("Enter Shelter ID: ")
            if not check_id(shelter, id):
                return
            choice = positive("Enter Status\n\t1). Close\n\t2). Open\n: ")
            for s in shelter:
                if s["id"] == id:
                    if choice == 1:
                        s["status"] = "Close"
                    elif choice == 2:
                        s["status"] = "Open"
                    else:
                        print("Invalid choice.")
                        return            

            with open(get_path("shelter.json"), "w") as f:
                json.dump(shelter, f, indent=4)
            print("Status Updated!")


        case 4:
            line(); heading("ALLOCATE PERSON TO SHELTER"); line()

            with open(get_path("shelter.json"), "r") as f:
                shelters = json.load(f)

            id = positive("Enter Shelter ID: ")
            if not check_id(shelters, id):
                return
            for s in shelters:
                if s["id"] == id:
                    if s["available"] > 0:
                        s["occupied"] += 1
                        s["available"] -= 1
                        print("allocated successfully!")
                    else:
                        print("Shelter is full.")

            with open(get_path("shelter.json"), "w") as f:
                json.dump(shelters, f, indent=4)
    line()
    pause()
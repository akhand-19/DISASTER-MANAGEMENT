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
                Shelter ID:  {s["Id"]}
                Name:  {s["Name"]}
                Location:  {s["Location"]}
                Capacity:  {s["Capacity"]}
                Occupied:  {s["Occupied"]}
                Available:  {s["Available"]}
                Contact:  {s["Contact"]}
                Facilities:  {s["Facilities"]}
                Status:  {s["Status"]}
                ''')
        case 2:
            line(); heading("REGISTER SHELTER") ; line()
                       
            name = input("Enter Shelter Name: ")
            location = input("Enter Location: ")
            status = input("Enter Status: ")
            capacity = int(input("Enter Capacity: "))
            occupied = int(input("Occupied: "))
            available = capacity - occupied
            facilities = input("Facilities : ")
            contact = int(input("Contact : "))

            with open(get_path("shelter.json"), "r") as f:
                shelter = json.load(f)

            if shelter:
                new_id = max(v["Id"] for v in shelter) + 1
            else:
                new_id = 1

            new_shelter = {
                "Id": new_id,
                "Name": name,
                "Location": location,
                "Status": status,
                "Capacity": capacity,
                "Available": available,
                "Occupied": occupied,
                "Facilities": facilities,
                "Contact": contact,
            }

            shelter.append(new_shelter)

            with open(get_path("shelter.json"), "w") as f:
                json.dump(shelter, f, indent=4)

            print("\nShelter Registered Successfully!")

        case 3:
            with open(get_path("shelter.json"), "r") as f:
                shelter = json.load(f)

            id = int(input("Enter Shelter ID: "))
            status = input("Enter Status\n\tclose\n\topen\n: ")

            for s in shelter:
                if s["Id"] == id:
                    s["Status"] = status

            with open(get_path("shelter.json"), "w") as f:
                json.dump(shelter, f, indent=4)
        case 4:
            line(); heading("ALLOCATE PERSON TO SHELTER"); line()

            with open(get_path("shelter.json"), "r") as f:
                shelters = json.load(f)

            id = int(input("Enter Shelter ID: "))

            for s in shelters:
                if s["Id"] == id:
                    if s["Available"] > 0:
                        s["Occupied"] += 1
                        s["Available"] -= 1
                        print("allocated successfully!")
                    else:
                        print("Shelter is full.")

            with open(get_path("shelter.json"), "w") as f:
                json.dump(shelters, f, indent=4)

            
     
    print("Status Updated!")
    line()
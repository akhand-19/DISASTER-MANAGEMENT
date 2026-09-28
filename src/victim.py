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




def victim():
    print('''
    1). VIEW VICTIM 
    2). REGISTER VICTIM
    3). UPDATE VICTIM STATUS
    ''')
    choice=positive("Enter The Option You Want To Choose :  ")
    match choice:
        case 1:
            line(); heading("VIEW VICTIM") ; line()
            with open(get_path("victim.json") , "r") as f:
                victim=json.load(f)
            for d in victim:
                print(f'''
                Id:  {d["id"]} 
                Victim Name:  {d["name"]} 
                Age:  {d["age"]}
                Emergency:  {d["emergency"]}
                Phone number : {d["phone number"]}
                Location:  {d["location"]}
                Status:  {d["status"]}
                ''')
            pause()

                
        case 2:
            line(); heading("REGISTER VICTIM") ; line()
                       
            name = input("Enter Victim Name: ")
            age = positive("Age: ")
            emergency = input("Enter Emergency: ")
            phone_number = input("Phone number : ")
            location = input("Enter Location: ")
            status = input("Enter Status (Need Help/Rescued/Hospitalised/Safe):  ")

            with open(get_path("victim.json"), "r") as f:
                victim = json.load(f)

            if victim:
                new_id = max(v["id"] for v in victim) + 1
            else:
                new_id = 1
            new_victim = {
                "id": new_id,
                "name": name,
                "location": location,
                "status": status,
                "emergency": emergency,
                "age": age,
                "phone number": phone_number
            }
            victim.append(new_victim)

            with open(get_path("victim.json"), "w") as f:
                json.dump(victim, f, indent=4)

            print("\nVictim Registered Successfully!")
            pause()


        case 3:
            with open(get_path("victim.json"), "r") as f:
                victim = json.load(f)

            id = positive("Enter Victim ID: ")
            if not check_id(victim, id):
                return
            choice = positive("Enter Status\n\t1). Need Help\n\t2). Rescued\n\t3). Hospitalized\n\t4). Safe\n: ")
            for v in victim:
                if v["id"] == id:
                    if choice == 1:
                        v["status"] = "Need Help"
                    elif choice == 2:
                        v["status"] = "Rescued"
                    elif choice == 3:
                        v["status"] = "Hospitalized"
                    elif choice == 4:
                        v["status"] = "Safe"
                    else:
                        print("Invalid choice.")
                        return            
            with open(get_path("victim.json"), "w") as f:
                json.dump(victim, f, indent=4)

            print("Status Updated!")
            pause()
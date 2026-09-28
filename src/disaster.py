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
            n=int(input(x))
            if n>0: return n
        except ValueError:
            pass
        print("Enter Valid Number!")
def check_id(data, id):
    if id > max(x["id"] for x in data):
        print("No ID Found!")
        return False
    return True


def disaster():
    line()
    print('''
    1). VIEW DISASTER 
    2). REGISTER DISASTER
    3). UPDATE DISASTER STATUS
    ''');line()
    choice=positive("Enter The Option You Want To Choose :  ")
    match choice:

        case 1:
            line(); heading("VIEW DISASTER") ; line()
            with open(get_path("disaster.json") , "r") as f:
                disaster=json.load(f)
            for d in disaster:
                print(f'''
                Id:  {d["id"]} 
                Name:  {d["name"]} 
                Location:  {d["location"]}
                Affected People:  {d["affected people"]}
                Severity:  {d["severity"]}
                Sheltered Required: {d["sheltered required"]}
                Status:  {d["status"]}
                ''')
            pause()



        case 2:
            line(); heading("REGISTER DISASTER") ; line()
                       
            name = input("Enter Disaster Name: ")
            location = input("Enter Location: ")
            affected_people = positive("Enter Number of Affected People: ")
            severity = input("Enter Severity: ")
            sheltered_required = input("Shelter Required? (true/false): ").lower()
            status = input("Enter Status: ")

            with open(get_path("disaster.json"), "r") as f:
                disasters = json.load(f)
            if disasters:
                new_id = max(d["id"] for d in disasters) + 1
            else:
                new_id = 1

            new_disaster = {
                "id": new_id,
                "name": name,
                "location": location,
                "affected people": affected_people,
                "sheltered required": sheltered_required,
                "severity": severity,
                "status": status,
            }            
            disasters.append(new_disaster)
            with open(get_path("disaster.json"), "w") as f:
                json.dump(disasters, f, indent=4)
            print("\nDisaster Registered Successfully!")
            pause()

        case 3:
            with open(get_path("disaster.json"), "r") as f:
                disasters = json.load(f)

            id = positive("Enter Disaster ID: ")
            if not check_id(disasters, id):
                return
            print("Enter Status\n\t1). Active\n\t2). Under Control\n\t3). Resolved\n: ")
            choice = positive("Choose Status: ")
            for d in disasters:
                if d["id"] == id:
                    if choice == 1:
                        d["status"] = "Active"
                    elif choice == 2:
                        d["status"] = "Under Control"
                    elif choice == 3:
                        d["status"] = "Resolved"
                    else:
                        print("Invalid choice.")
                        return
                    with open(get_path("disaster.json"), "w") as f:
                        json.dump(disasters, f, indent=4)
                    print("Status Updated!")
            pause()

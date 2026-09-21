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





def victim():
    print('''
    1). VIEW VICTIM 
    2). REGISTER VICTIM
    3). UPDATE VICTIM STATUS
    ''')
    choice=int(input("Enter The Option You Want To Choose :  "))
    match choice:
        case 1:
            line(); heading("VIEW VICTIM") ; line()
            with open(get_path("victim.json") , "r") as f:
                victim=json.load(f)
            for d in victim:
                print(f'''
                Id:  {d["Id"]} 
                Victim Name:  {d["Name"]} 
                Location:  {d["Location"]}
                Status:  {d["Status"]}
                Emergency:  {d["Emergency"]}
                Age:  {d["Age"]}
                Phone number : {d["Phone number"]}
                ''')
        case 2:
            line(); heading("REGISTER VICTIM") ; line()
                       
            name = input("Enter Victim Name: ")
            location = input("Enter Location: ")
            status = input("Enter Status: ")
            emergency = input("Enter Emergency: ")
            age = int(input("Age: "))
            phone_number = input("Phone number : ")

            with open(get_path("victim.json"), "r") as f:
                victim = json.load(f)

            if victim:
                new_id = max(v["Id"] for v in victim) + 1
            else:
                new_id = 1

            new_victim = {
                "Id": new_id,
                "Name": name,
                "Location": location,
                "Status": status,
                "Emergency": emergency,
                "Age": age,
                "Phone number": phone_number
            }

            victim.append(new_victim)

            with open(get_path("victim.json"), "w") as f:
                json.dump(victim, f, indent=4)

            print("\nVictim Registered Successfully!")

        case 3:
            with open(get_path("victim.json"), "r") as f:
                victim = json.load(f)

            id = int(input("Enter Victim ID: "))
            status = input("Enter Status\n\tNeeds Help\n\tRescued\n\tHospitalized\n\tSafe\n: ")

            for d in victim:
                if d["Id"] == id:
                    d["Status"] = status

            with open(get_path("victim.json"), "w") as f:
                json.dump(victim, f, indent=4)

    print("Status Updated!")
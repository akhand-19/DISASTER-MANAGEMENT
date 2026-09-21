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





def disaster():
    print('''
    1). VIEW DISASTER 
    2). REGISTER DISASTER
    3). UPDATE DISASTER STATUS
    ''')
    choice=int(input("Enter The Option You Want To Choose :  "))
    match choice:
        case 1:
            line(); heading("VIEW DISASTER") ; line()
            with open(get_path("disaster.json") , "r") as f:
                disaster=json.load(f)
            for d in disaster:
                print(f'''
                Id:  {d["Id"]} 
                Name:  {d["Name"]} 
                Location:  {d["Location"]}
                Status:  {d["Status"]}
                Severity:  {d["Severity"]}
                Affected People:  {d["Affected People"]}
                Sheltered Required: {d["Sheltered Required"]}
                ''')
        case 2:
            line(); heading("REGISTER DISASTER") ; line()
                       
            name = input("Enter Disaster Name: ")
            location = input("Enter Location: ")
            status = input("Enter Status: ")
            severity = input("Enter Severity: ")
            affected_people = int(input("Enter Number of Affected People: "))
            sheltered_required = input("Shelter Required? (true/false): ").lower()

           
            with open(get_path("disaster.json"), "r") as f:
                disasters = json.load(f)

            
            if disasters:
                new_id = max(d["Id"] for d in disasters) + 1
            else:
                new_id = 1

            
            new_disaster = {
                "Id": new_id,
                "Name": name,
                "Location": location,
                "Status": status,
                "Severity": severity,
                "Affected People": affected_people,
                "Sheltered Required": sheltered_required == "true"
            }

            
            disasters.append(new_disaster)

           
            with open(get_path("disaster.json"), "w") as f:
                json.dump(disasters, f, indent=4)

            print("\nDisaster Registered Successfully!")

        case 3:
            with open(get_path("disaster.json"), "r") as f:
                disasters = json.load(f)

            id = int(input("Enter Disaster ID: "))
            status = input("Enter Status\n\tActive\n\tUnder Control\n\tResolved\n: ")

            for d in disasters:
                if d["Id"] == id:
                    d["Status"] = status

            with open(get_path("disaster.json"), "w") as f:
                json.dump(disasters, f, indent=4)

    print("Status Updated!")





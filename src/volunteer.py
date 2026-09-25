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



def volunteer():
    print('''
    1. VIEW VOLUNTEERS
    2. REGISTER VOLUNTEER
    3. UPDATE VOLUNTEER STATUS
    4. ASSIGN  VOLUNTEER
    ''')
    choice=positive("Enter The Option You Want To Choose :  ")
    match choice:
        case 1:
            line(); heading("VIEW VOLUNTEER") ; line()
            with open(get_path("volunteer.json") , "r") as f:
                volunteer=json.load(f)
            for v in volunteer:
                print(f'''
                Volunteer ID: {v["id"]}
                Name: {v["name"]}
                Age: {v["age"]}
                Contact: {v["contact"]}
                Skill: {v["skill"]}
                Location: {v["location"]}
                Availability: {v["availability"]}
                Status: {v["status"]}
                Assigned To: {v["assigned to"]}
                ''')


        case 2:
            line(); heading("REGISTER VOLUNTEER") ; line()
            volunteer_name = input("Enter Volunteer Name: ")
            age = positive("Enter Volunteer's Age : ")
            contact = input("Enter Contact : ")
            location = input("Enter Location : ")
            skill = input("Enter Skill : ")
            availability = input("Enter availability : ")
            status = input("Enter Status : ")
            with open(get_path("volunteer.json"), "r") as f:
                volunteer = json.load(f)
            if volunteer:
                new_id = max(v["id"] for v in volunteer) + 1
            else:
                new_id = 1
            assigned=""
            new_volunteer = {
                "id": new_id,
                "name": volunteer_name,
                "contact": contact,
                "age": age,
                "skill": skill,
                "location": location,
                "status": status,
                "availability": availability,
                "assigned to": assigned
            }
            volunteer.append(new_volunteer)

            with open(get_path("volunteer.json"), "w") as f:
                json.dump(volunteer, f, indent=4)
            print("\nVolunteer Registered Successfully!")



        case 3:
            line(); heading("UPDATE VOLUNTEER STATUS"); line()
            with open(get_path("volunteer.json"), "r") as f:
                volunteer = json.load(f)
            id = positive("Enter Volunteer ID: ")
            status = positive("Enter Choice\n\t1.) Available\n\t2). Not Available\n: ")
            for v in volunteer:
                if v["id"] == id:
                    if choice == 1:
                        v["status"] = "Available"
                    elif choice == 2:
                        v["status"] = "Not Available"
                    else:
                        print("Invalid choice.")
                        return            

            with open(get_path("volunteer.json"), "w") as f:
                json.dump(volunteer, f, indent=4)
            print("Status Updated!")



        case 4:
            line();heading("ASSIGN VOLUNTEER");line()
            with open(get_path("disaster.json"), "r") as j:
                disaster=json.load(j)
            max_id=max(d["id"] for d in disaster)
            disaster_id=positive("Enter The Disaster Id : ")
            if disaster_id>max_id:
                print("No Id Found !")
                return

            with open(get_path("volunteer.json"), "r") as f:
                volunteer = json.load(f)
            volunteer_id=int(input("Enter Volunteer's Id : "))
            for v in volunteer:
                if volunteer_id==v["id"]:
                    v["assigned to"]=disaster_id
            with open(get_path("volunteer.json"), "w") as f:
                json.dump(volunteer,f,indent=4)
            print("Volunteer Assigned Successfully")
    line()
    pause()
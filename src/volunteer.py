import os
import json


base = os.path.dirname(__file__)
def get_path(filename):
    return os.path.join(base, "..", "data" , filename)



# DEFINING SOME BASIC FUNCTIONS FOR FURTHER NEED  
def line():
    print("-"*70)
def heading(a):
    print(a.center(30))
def pause():
    print("\n Enter To Continue ........")




# FUNCTIONS FOR OPTIONS

def volunteer():
    print('''
    1. VIEW VOLUNTEERS
    2. REGISTER VOLUNTEER
    3. UPDATE VOLUNTEER STATUS
    4. ASSIGN  VOLUNTEER
    ''')
    choice=int(input("Enter The Option You Want To Choose :  "))
    match choice:
        case 1:
            line(); heading("VIEW VOLUNTEER") ; line()
            with open(get_path("volunteer.json") , "r") as f:
                volunteer=json.load(f)
            for v in volunteer:
                print(f'''
                Volunteer ID: {v["Id"]}
                Name: {v["Name"]}
                Age: {v["Age"]}
                Contact: {v["Contact"]}
                Skill: {v["skill"]}
                Location: {v["location"]}
                Availability: {v["Availability"]}
                Status: {v["Status"]}
                Assigned To: {v["Assigned to"]}
                ''')
        case 2:
            line(); heading("REGISTER VOLUNTEER") ; line()
                       
            # Take input from user
            volunteer_name = input("Enter Volunteer Name: ")
            age = input("Enter Volunteer's Age : ")
            contact = input("Enter Contact : ")
            location = input("Enter Location : ")
            skill = input("Enter Skill : ")
            availability = input("Enter availabilty : ")
            status = input("Enter Status : ")
            
            # Open JSON file and load existing victims
            with open(get_path("volunteer.json"), "r") as f:
                volunteer = json.load(f)

            # Generate new ID
            if volunteer:
                new_id = max(v["Id"] for v in volunteer) + 1
            else:
                new_id = 1
            assigned=""
            # Create new volunteer
            new_victim = {
                "Id": new_id,
                "Name": volunteer_name,
                "Contact": contact,
                "Age": age,
                "Skill": skill,
                "Location": location,
                "Status": status,
                "Availabilty": availability,
                "Assigned To": assigned
            }

            # Add new volunteer to list
            volunteer.append(new_victim)

            # Save updated list to JSON
            with open(get_path("volunteer.json"), "w") as f:
                json.dump(volunteer, f, indent=4)

            print("\nVolunteer Registered Successfully!")

        case 3:
            line(); heading("UPDATE VOLUNTEER STATUS"); line()
            with open(get_path("volunteer.json"), "r") as f:
                volunteer = json.load(f)

            id = int(input("Enter Volunteer ID: "))
            status = input("Enter Status\n\tAvailable\n\tNot Available\n: ")

            for v in volunteer:
                if v["Id"] == id:
                    v["Status"] = status

            with open(get_path("volunteer.json"), "w") as f:
                json.dump(volunteer, f, indent=4)

        case 4:
            line();heading("ASSIGN VOLUNTEER");line()
            with open(get_path("disaster.json"), "r") as j:
                disaster=json.load(j)
            max_id=max(d["Id"] for d in disaster)
            disaster_id=int(input("Enter The Disaster Id : "))
            if disaster_id>max_id :
                print("No Id Found !")
                return

            with open(get_path("volunteer.json"), "r") as f:
                volunteer = json.load(f)
            volunteer_id=int(input("Enter Volunteer's Id : "))
            for v in volunteer:
                if volunteer_id==v["Id"]:
                    v["Assigned To"]=disaster_id
            with open(get_path("volunteer.json"), "w") as f:
                json.dump(volunteer,f,indent=4)
            print("Volunteer Assigned Successfully")
                
    print("Status Updated!")

            


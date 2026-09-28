import os
import json

base = os.path.dirname(__file__)

def get_path(filename):
    return os.path.join(base, "..", "data", filename)
def line():
    print("-" * 70)
def heading(a):
    print(a.center(30))
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
    
def activities():
    with open(get_path("activities.json"), "r") as f:
        data = json.load(f)
    print('''
    1. ALERTS
    2. REQUEST
    3. DONATION
    4. TASK
    ''')
    choice = positive("Enter Option: ")
    match choice:
        case 1:
            print('''
            1. Create Alert
            2. View Alerts
            3. Close Alert
            ''')
            option = positive("Enter Option: ")
            match option:
                case 1:
                    alert = {
                    "id": len(data["alerts"]) + 1,
                    "message": input("Enter Alert Message: "),
                    "location": input("Enter Location: "),
                    "status": "Active"
                    }
                    data["alerts"].append(alert)
                    with open(get_path("activities.json"), "w") as f:
                        json.dump(data, f, indent=4)
                    print("Alert Created!")


                case 2:
                    for a in data["alerts"]:
                        print(f'''
                    Id:  {a["id"]} 
                    Message:  {a["message"]} 
                    Location:  {a["location"]}
                    Status:  {a["status"]}
                    ''')    

                case 3:
                    alert_id = positive("Enter Alert ID: ")
                    for a in data["alerts"]:
                        if a["id"] == alert_id:
                            a["status"] = "Closed"
                    with open(get_path("activities.json"), "w") as f:
                        json.dump(data, f, indent=4)
                    print("Alert Closed!")
        
        
        case 2:
            print('''
            1. Create Rescue Request
            2. View Rescue Requests
            3. Update Rescue Request
            ''')

            option = positive("Enter Option: ")

            match option:

                case 1:
                    request = {
                        "id": len(data["requests"]) + 1,
                        "name": input("Enter Name: "),
                        "location": input("Enter Location: "),
                        "description": input("Enter Request: "),
                        "status": "Pending"
                    }

                    data["requests"].append(request)
                    with open(get_path("activities.json"), "w") as f:
                        json.dump(data, f, indent=4)
                    print("Request Created!")

                case 2:
                    for r in data["requests"]:
                        print(r)

                case 3:
                    request_id = positive("Enter Request ID: ")
                    status = input("Enter Status:  ")

                    for r in data["requests"]:
                        if r["id"] == request_id:
                            r["status"] = status
                    with open(get_path("activities.json"), "w") as f:
                        json.dump(data, f, indent=4)
                    print("Request Updated!")
        case 3:
            print('''
            1. Record Donation
            2. View Donations
            ''')

            option = positive("Enter Option: ")
            match option:
                case 1:
                    donation = {
                        "id": len(data["donations"]) + 1,
                        "donor": input("Enter Donor Name: "),
                        "resource": input("Enter Resource: "),
                        "quantity": positive("Enter Quantity: ")
                    }
                    data["donations"].append(donation)
                    with open(get_path("activities.json"), "w") as f:
                        json.dump(data, f, indent=4)
                    print("Donation Recorded!")

                case 2:
                    for d in data["donations"]:
                        print(d)
        
        case 4:
            print('''
            1. Create Task
            2. View Tasks
            3. Update Task
            ''')
            option = positive("Enter Option: ")
            match option:
                case 1:
                    task = {
                        "id": len(data["tasks"]) + 1,
                        "task": input("Enter Task: "),
                        "status": "Pending"
                    }

                    data["tasks"].append(task)
                    with open(get_path("activities.json"), "w") as f:
                        json.dump(data, f, indent=4)
                    print("Task Created!")

                case 2:
                    for t in data["tasks"]:
                        print(t)

                case 3:
                    task_id = positive("Enter Task ID: ")
                    status =input("Enter Status: ")
                    for t in data["tasks"]:
                        if t["id"] == task_id:
                            t["status"] = status
                    with open(get_path("activities.json"), "w") as f:
                        json.dump(data, f, indent=4)
                    print("Task Updated!")

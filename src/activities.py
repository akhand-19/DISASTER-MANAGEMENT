import os
import json

base = os.path.dirname(__file__)

def get_path(filename):
    return os.path.join(base, "..", "data", filename)


def line():
    print("-" * 70)


def heading(a):
    print(a.center(30))


def activities():

    with open(get_path("activities.json"), "r") as f:
        data = json.load(f)

    print('''
    1. ALERTS
    2. REQUEST
    3. DONATION
    4. TASK
    ''')

    choice = int(input("Enter Option: "))

    
    match choice:

        case 1:
            print('''
            1. Create Alert
            2. View Alerts
            3. Close Alert
            ''')

            option = int(input("Enter Option: "))

            match option:

                case 1:
                    alert = {
                    "Id": len(data["alerts"]) + 1,
                    "Message": input("Enter Alert Message: "),
                    "Location": input("Enter Location: "),
                    "Status": "Active"
                    }

                    data["alerts"].append(alert)
                    with open(get_path("activities.json"), "w") as f:
                        json.dump(data, f, indent=4)
                    print("Alert Created!")

                case 2:
                    for a in data["alerts"]:
                        print(a)

                case 3:
                    alert_id = int(input("Enter Alert ID: "))

                    for a in data["alerts"]:
                        if a["Id"] == alert_id:
                            a["Status"] = "Closed"
                    with open(get_path("activities.json"), "w") as f:
                        json.dump(data, f, indent=4)
                    print("Alert Closed!")

      
        case 2:
            print('''
            1. Create Rescue Request
            2. View Rescue Requests
            3. Update Rescue Request
            ''')

            option = int(input("Enter Option: "))

            match option:

                case 1:
                    request = {
                        "Id": len(data["requests"]) + 1,
                        "Name": input("Enter Name: "),
                        "Location": input("Enter Location: "),
                        "Description": input("Enter Request: "),
                        "Status": "Pending"
                    }

                    data["requests"].append(request)
                    with open(get_path("activities.json"), "w") as f:
                        json.dump(data, f, indent=4)
                    print("Request Created!")

                case 2:
                    for r in data["requests"]:
                        print(r)

                case 3:
                    request_id = int(input("Enter Request ID: "))
                    status = input("Enter Status: ")

                    for r in data["requests"]:
                        if r["Id"] == request_id:
                            r["Status"] = status
                    with open(get_path("activities.json"), "w") as f:
                        json.dump(data, f, indent=4)
                    print("Request Updated!")

        

        case 3:
            print('''
            1. Record Donation
            2. View Donations
            ''')

            option = int(input("Enter Option: "))

            match option:

                case 1:
                    donation = {
                        "Id": len(data["donations"]) + 1,
                        "Donor": input("Enter Donor Name: "),
                        "Resource": input("Enter Resource: "),
                        "Quantity": int(input("Enter Quantity: "))
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

            option = int(input("Enter Option: "))

            match option:

                case 1:
                    task = {
                        "Id": len(data["tasks"]) + 1,
                        "Task": input("Enter Task: "),
                        "Status": "Pending"
                    }

                    data["tasks"].append(task)
                    with open(get_path("activities.json"), "w") as f:
                        json.dump(data, f, indent=4)
                    print("Task Created!")

                case 2:
                    for t in data["tasks"]:
                        print(t)

                case 3:
                    task_id = int(input("Enter Task ID: "))
                    status = input("Enter Status: ")

                    for t in data["tasks"]:
                        if t["Id"] == task_id:
                            t["Status"] = status

                    with open(get_path("activities.json"), "w") as f:
                        json.dump(data, f, indent=4)

                    print("Task Updated!")

    
    
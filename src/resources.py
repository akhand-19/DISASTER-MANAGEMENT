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

def resources():
    print('''
    1). VIEW RESOURCES 
    2). ADD RESOURCES
    3). DISTRIBUTE RESOURCES
    ''')
    choice=positive("Enter The Option You Want To Choose :  ")
    match choice:
        case 1:
            line(); heading("VIEW RESOURCES") ; line()
            with open(get_path("resources.json") , "r") as f:
                resources=json.load(f)
            for r in resources:
                print(f'''
                Resource ID:  {r["id"]}
                Name:  {r["name"]}
                Location:  {r["location"]}
                Catogery:  {r["catogery"]}
                Condition:  {r["condition"]}
                Quantity:  {r["quantity"]}
                ''')
        case 2:
            line(); heading("ADD RESOURCES") ; line()
                       
            name = input("Enter Resource Name: ")
            location = input("Enter Location: ")
            Catogery = input("Enter Catogery: ")
            condition = (input("Condition: ")) 
            quantity = positive("Quantity : ")

            with open(get_path("resources.json"), "r") as f:
                resources = json.load(f)

            if resources:
                new_id = max(v["id"] for v in resources) + 1
            else:
                new_id = 1

            new_resource = {
                "id": new_id,
                "name": name,
                "location": location,
                "catogery": Catogery,
                "condition": condition,
                "quantity": quantity,
            }

            resources.append(new_resource)

            with open(get_path("resources.json"), "w") as f:
                json.dump(resources, f, indent=4)
            print("\nResource Registered Successfully!")

        case 3:
            line(); heading("DISTRIBUTE RESOURCES"); line()

            with open(get_path("resources.json"), "r") as f:
                resources = json.load(f)

            resource_id = positive("Enter Resource Id: ")
            amount = positive("Enter Quantity To Distribute: ")

            for r in resources:
                if r["id"] == resource_id:
                    if amount <= r["quantity"]:
                        r["quantity"] -= amount
                        print("Resource Distributed Successfully!")
                    else:
                        print("Not Enough Resources!")

            with open(get_path("resources.json"), "w") as f:
                json.dump(resources, f, indent=4)
    line()
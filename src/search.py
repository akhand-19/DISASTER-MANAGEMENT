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

def search_disaster():
    search=input("Enter Id / Name / Location :  ")
    if search.isnumeric()==True:
        search=int(search)
    with open(get_path("disaster.json"), "r") as f:
        disaster=json.load(f)
    for d in disaster:
        if search==d["id"] or search==d["name"] or search==d["location"]:
            print(f'''
            Id:  {d["id"]} 
            Name:  {d["name"]} 
            Location:  {d["location"]}
            Status:  {d["status"]}
            Severity:  {d["severity"]}
            Affected People:  {d["affected people"]}
            Sheltered Required: {d["sheltered required"]}
            ''')

    
def search_volunteer():
    search=input("Enter Id / Name / Skill :  ")
    if search.isnumeric()==True:
        search=int(search)
    with open(get_path("volunteer.json"), "r") as f:
        volunteer=json.load(f)
    for v in volunteer:
        if search==v["id"] or search==v["name"] or search==v["skill"]:
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


def search_victim():
    search=input("Enter Id / Name / Location  :  ")
    if search.isnumeric()==True:
        search=int(search)
    with open(get_path("victim.json"), "r") as f:
        victim=json.load(f)
    for v in victim:
        if search==v["id"] or search==v["name"] or search==v["location"]:
            print(f'''
            Id:  {v["id"]} 
            Victim Name:  {v["name"]} 
            Location:  {v["location"]}
            Status:  {v["status"]}
            Emergency:  {v["emergency"]}
            Age:  {v["age"]}
            Phone number : {v["phone number"]}
            ''')


def search_shelter():
    search=input("Enter Id / Name / Location  :  ")
    if search.isnumeric()==True:
        search=int(search)
    with open(get_path("shelter.json"), "r") as f:
        shelter=json.load(f)
    for s in shelter:
        if search==s["id"] or search==s["name"] or search==s["location"]:
            print(f'''
            Shelter ID:  {s["id"]}
            Name:  {s["name"]}
            Location:  {s["location"]}
            Capacity:  {s["capacity"]}
            Occupied:  {s["occupied"]}
            Available:  {s["available"]}
            Contact:  {s["contact"]}
            Facilities:  {s["facilities"]}
            Status:  {s["status"]}
            ''')


def search_resources():
    search=input("Enter Id / Name / Location  :  ")
    if search.isnumeric()==True:
        search=int(search)
    with open(get_path("resources.json"), "r") as f:
        resources=json.load(f)
    for r in resources:
        if search==r["id"] or search==r["name"] or search==r["location"]:
            print(f'''
            Resource ID:  {r["id"]}
            Name:  {r["name"]}
            Location:  {r["location"]}
            Catogery:  {r["catogery"]}
            Condition:  {r["condition"]}
            Quantity:  {r["quantity"]}
            ''')






def search():
    line();heading("SEARCH");line()

    print('''
    1.) Search Disaster
    2.) Search Victim
    3.) Search Shelter
    4.) Search Volunteer
    5.) Search Resource
    ''')
    choice=int(input("Choose an Option : "))
    match choice:
        case 1:
            search_disaster()
        case 2:
            search_victim()
        case 3:
            search_shelter()
        case 4:
            search_volunteer()
        case 5:
            search_resources()
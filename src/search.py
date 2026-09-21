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


def search_disaster():
    search=input("Enter Id / Name / Location :  ")
    if search.isnumeric()==True:
        search=int(search)
    with open(get_path("disaster.json"), "r") as f:
        disaster=json.load(f)
    for d in disaster:
     if search==d["Id"] or search==d["Name"] or search==d["Location"]:
            print(f'''
            Id:  {d["Id"]} 
            Name:  {d["Name"]} 
            Location:  {d["Location"]}
            Status:  {d["Status"]}
            Severity:  {d["Severity"]}
            Affected People:  {d["Affected People"]}
            Sheltered Required: {d["Sheltered Required"]}
            ''')

    
def search_volunteer():
    search=input("Enter Id / Name / Skill :  ")
    if search.isnumeric()==True:
        search=int(search)
    with open(get_path("volunteer.json"), "r") as f:
        volunteer=json.load(f)
    for v in volunteer:
        if search==v["Id"] or search==v["Name"] or search==v["Skill"]:
            print(f'''
            Volunteer ID: {v["Id"]}
            Name: {v["Name"]}
            Age: {v["Age"]}
            Contact: {v["Contact"]}
            Skill: {v["Skill"]}
            Location: {v["Location"]}
            Availability: {v["Availability"]}
            Status: {v["Status"]}
            Assigned To: {v["Assigned To"]}
            ''') 


def search_victim():
    search=input("Enter Id / Name / Location  :  ")
    if search.isnumeric()==True:
        search=int(search)
    with open(get_path("victim.json"), "r") as f:
        victim=json.load(f)
    for v in victim:
        if search==v["Id"] or search==v["Name"] or search==v["Location"]:
            print(f'''
            Id:  {v["Id"]} 
            Victim Name:  {v["Name"]} 
            Location:  {v["Location"]}
            Status:  {v["Status"]}
            Emergency:  {v["Emergency"]}
            Age:  {v["Age"]}
            Phone number : {v["Phone number"]}
            ''')


def search_shelter():
    search=input("Enter Id / Name / Location  :  ")
    if search.isnumeric()==True:
        search=int(search)
    with open(get_path("shelter.json"), "r") as f:
        shelter=json.load(f)
    for s in shelter:
        if search==s["Id"] or search==s["Name"] or search==s["Location"]:
            print(f'''
            Shelter ID:  {s["Id"]}
            Name:  {s["Name"]}
            Location:  {s["Location"]}
            Capacity:  {s["Capacity"]}
            Occupied:  {s["Occupied"]}
            Available:  {s["Available"]}
            Contact:  {s["Contact"]}
            Facilities:  {s["Facilities"]}
            Status:  {s["Status"]}
            ''')


def search_resources():
    search=input("Enter Id / Name / Location  :  ")
    if search.isnumeric()==True:
        search=int(search)
    with open(get_path("resources.json"), "r") as f:
        resources=json.load(f)
    for r in resources:
        if search==r["Id"] or search==r["Name"] or search==r["Location"]:
            print(f'''
            Resource ID:  {r["Id"]}
            Name:  {r["Name"]}
            Location:  {r["Location"]}
            Catogery:  {r["Catogery"]}
            Condition:  {r["Condition"]}
            Quantity:  {r["Quantity"]}
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


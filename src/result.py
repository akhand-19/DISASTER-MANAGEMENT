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

def statistic():
    line();heading("DISASTER MANAGEMENT STATISTICS");line()
    with open(get_path("disaster.json"), "r") as f:
        disaster=json.load(f)
    with open(get_path("victim.json"), "r") as f:
        victim=json.load(f)
    with open(get_path("shelter.json"), "r") as f:
        shelter=json.load(f)
    with open(get_path("volunteer.json"), "r") as f:
        volunteer=json.load(f)
    with open(get_path("resources.json"), "r") as f:
        resources=json.load(f)
    with open(get_path("activities.json"), "r") as f:
        activities=json.load(f)
    print("Total Disaster : ", max(d["Id"] for d in disaster ))
    print("Total Victims  : ", max(v["Id"] for v in victim ))
    print("Total Shelter  : ", max(s["Id"] for s in shelter ))
    print("Total Volunteeer : ", max(v["Id"] for v in volunteer ))
    print("Total Resources : ", max(r["Id"] for r in resources ))
    print("Total Alerts : ", max(d["Id"] for d in activities["alerts"] ))
    print("Total Rescue Requests : ", max(d["Id"] for d in activities["requests"] ))
    print("Total Donation : ", max(d["Id"] for d in activities["donations"] ))
    print("Total Tasks : ", max(d["Id"] for d in activities["tasks"] ))
    line()
    safe=sum(1 for v in victim if v["Status"]=="safe")
    rescued=sum(1 for v in victim if v["Status"]=="rescued")
    needing_help=sum(1 for v in victim if v["Status"]=="needing help")
    print(f"Victim Safe: {safe}\nVictim Rescued: {rescued}\nVictim Needing Help: {needing_help}")





def result():
    print('''
    1). STATISTICS
    # 2). RESULT
    ''')
    choice=int(input("Enter The Option : "))
    match choice:
        case 1:
            statistic()
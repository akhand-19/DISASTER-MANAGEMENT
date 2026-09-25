import disaster
import victim
import shelter
import volunteer
import resources
import activities
import search
import result

while True:
    print("""
1. Disaster
2. Victim
3. Shelter
4. Volunteer
5. Resource
6. Activities
7. Search
8. Result
9. Exit
""")

    choice = disaster.positive("Enter choice: ")
    if choice == 1:
        disaster.disaster()
    elif choice == 2:
        victim.victim()
    elif choice == 3:
        shelter.shelter()
    elif choice == 4:
        volunteer.volunteer()
    elif choice == 5:
        resources.resources()
    elif choice == 6:
        activities.activities()
    elif choice == 7:
        search.search()
    elif choice == 8:
        result.result()
    elif choice == 9:
        break

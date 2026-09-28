<div align="center">
<h1>
<img width="25" alt="Image" src="https://github.com/user-attachments/assets/ffe877ed-e57a-42f4-a7b4-21cdfc5df7bb" />
 Disaster Management System
</h1>
<h2>
<img width="25" alt="Image" src="https://github.com/user-attachments/assets/120c59f2-f631-45be-9840-58af4308391f" />
Python-based Disaster Management System
</h2>

<br>

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/Storage-JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)
![License](https://img.shields.io/badge/License-MIT-2ea44f?style=for-the-badge)

<br>

**Manage • Organize • Respond • Recover**

</div>

---

## ❓ What is this?

The **Disaster Management System** is a menu-driven Python application created for managing information during disaster management situations. 

It can manage:

> 🌪️ Disasters  
> 👥 Victims  
> 🏠 Shelters  
> 🦸 Volunteers  
> 📦 Resources  
> 🔔 Alerts  
> 🆘 Rescue Requests  
> 💝 Donations  
> 📋 Tasks  
> 🔍 Search

The **Disaster Management System** uses the programming language **Python** to implement the logic of the program, while the data is stored in **JSON** files.

---

# ✨ Features

<table>
<tr>
<td width="50%">

### 🌪️ Disaster Management

- Register disasters
- View disaster records
- Update disaster status
- Track affected people
- Track severity
- Track shelter requirements

</td>

<td width="50%">

### 👥 Victim Management

- Register victims
- View victim information
- Update victim status
- Store emergency information
- Track victim location

</td>
</tr>

<tr>
<td>

### 🏠 Shelter Management

- Register shelters
- Track capacity
- Track occupied spaces
- Track available spaces
- Update shelter status (open/close)
- Allocate people to shelter

</td>

<td>

### 🦸 Volunteer Management

- Register volunteers
- View volunteers
- Track skills
- Track availability
- Update status
- Assign volunteers to disasters

</td>
</tr>

<tr>
<td>

### 📦 Resource Management

- Add resources
- View resources
- Track quantities
- Track condition
- Distribute resources
- Prevent over-distribution

</td>

<td>

### 📋 Activity Management

- 🔔 Alerts
- 🆘 Rescue Requests
- 💝 Donations
- 📋 Tasks

All are managed by centralized activity module.

</td>
</tr>

<tr>
<td>

### 📃 Result Management

- Displays disaster statistics
- Shows victim status counts
- Tracks resources and shelters
- Summarizes alerts, requests, donations & tasks 

</td>
<td>

### 🔍 Search Feature

- Search by ID, name, or location
- Supports 5 record types
- Displays matching details
- Uses JSON data
</table>

---

# ⚙️ System Overview

```text
                      🚨 DISASTER MANAGEMENT
                                 │
                                 ▼
                           🖥️ MAIN MENU
                                 │
       ┌──────────────┬──────────┼──────────┬──────────────┐
       │              │          │          │              │
       ▼              ▼          ▼          ▼              ▼
      🌪️             👥        🏠         🦸             📦
   Disaster        Victim     Shelter    Volunteer     Resources
       │              │          │          │              │
       └──────────────┴──────────┴──────────┴──────────────┘
                                 │
                                 ▼
                          📋 ACTIVITIES
                                 │
         ┌────────────────┬──────┼─────────┬────────────────┐
         ▼                ▼                ▼                ▼
     🔔 Alerts      🆘 Requests    💝 Donations       📝 Tasks
```

---
# 🏗️ Project Structure
```text
DISASTER MANAGEMENT
│
├── 📁 data/
│   ├── disaster.json
│   ├── victim.json
│   ├── shelter.json
│   ├── volunteer.json
│   ├── resources.json
│   └── activities.json
│
├── 📁 src/
│   ├── main.py
│   ├── disaster.py
│   ├── victim.py
│   ├── shelter.py
│   ├── volunteer.py
│   ├── resources.py
│   ├── activities.py
│   ├── search.py
│   └── result.py
│
├── 📄 .gitignore
├── 📄 LICENSE
└── 📄 README.md
```
---
# 📚 Concepts Used
```text
Python
│
├── Variables
├── Data Types
│   ├── int
│   ├── str
│   ├── bool
│   └── list / dictionary
│
├── Input / Output
│   ├── input()
│   └── print()
│
├── Operators
│   ├── Arithmetic
│   ├── Comparison
│   └── Logical
│
├── Conditional Statements
│   ├── if
│   ├── elif
│   └── else
│
├── Loops
│   ├── for
│   └── while
│
├── Functions
│   ├── Function Definition
│   ├── Parameters
│   └── Return Values
│
├── Lists
├── Dictionaries
├── List Comprehension
├── String Methods
│   └── strip(), lower(), etc.
│
├── File Handling
│   ├── open()
│   ├── read
│   └── write
│
├── JSON
│   ├── json.load()
│   └── json.dump()
│
├── Exception Handling
│   └── try / except
│
├── Match-Case
│
├── Modular Programming
│   └── import / separate modules
│
├── OS Module
│   └── File Paths
│
└── Data Validation
    └── Input Validation
```
---
# 🚀 How to Run

## Follow these steps to run the Disaster Management System on your computer.

###  1. Clone the Repository
```
git clone https://github.com/akhand-19/DISASTER-MANAGEMENT.git
```
### 2. Open the Project Folder
```
cd Disaster-Management-System
```
### 3. Check Python Installation
Make sure Python 3.10 or higher is installed:
```
python --version
```
### 4. Run the Program
Run the main Python file:
```
python main.py
```
Note: Make sure the data folder containing the JSON files is present in the correct project directory.
### ⚠️ Important
* No external Python libraries are required.
* The program uses JSON files for data storage.
* Run main.py from the main project directory.
* Do not rename or move the data folder unless you also update the file paths in the Python code.
---
# Author
**Akhand Pratap Singh**





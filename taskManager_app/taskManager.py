
import json
import os
import uuid
from datetime import datetime
import time
from style import *

FILE_TASKS = "taskManager_app/tasks.json"
uuid = uuid.uuid4().hex[:8]

def read(FILE_TASKS):
    """if not exsist make tasks,json and read the file."""
    # make file
    if not os.path.exists(FILE_TASKS):
        with open(FILE_TASKS, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)
    #read file
    with open(FILE_TASKS, "r", encoding="utf-8") as file:
        return json.load(file)

def save(tasks, FILE_TASKS):
    """save tasks.json"""
    # save file
    with open(FILE_TASKS, "w", encoding="utf-8") as file:
        return json.dump(tasks, file, indent=4, ensure_ascii=False)

def time_date_stamp():
    """Print timestamp"""
    date_time = datetime.now()
    return f"Date: {date_time.strftime("%d-%m-%Y")} Time: {date_time.strftime("%H:%M")}"
    
def read_anim():
    """Reading tasks animation"""
    print("Reading tasks", end="", flush=True)
    for i in range(9):
        time.sleep(0.06)
        print(".", end="", flush=True)
    time.sleep(0.06)
    print(".")

def main_menu(tasks):
    """Showing main menu"""
    if tasks:
        print("─" * 53)
        print(f"{CYAN_BOLD}1. {RESET}{BOLD}Exit{RESET}")  
        print(f"{CYAN_BOLD}2. {RESET}{BOLD}Ad task{RESET}")
        print(f"{CYAN_BOLD}3. {RESET}{BOLD}Edit task{RESET}")
        print(f"{CYAN_BOLD}4. {RESET}{BOLD}Delete task{RESET}")
        print(f"{CYAN_BOLD}5. {RESET}{BOLD}Show tasks{RESET}")
        print(f"{CYAN_BOLD}6. {RESET}{BOLD}Change status{RESET}")
        print("─" * 53)
    else:
        print("─" * 53)
        print(f"{CYAN_BOLD}1. {RESET}{BOLD}Exit{RESET}")  
        print(f"{CYAN_BOLD}2. {RESET}{BOLD}Ad task{RESET}")
        print("─" * 53)

def choice_main_menu(tasks):
    """Make choice in main menu"""
    print()
    choice_mainMenu = int(input("Make a choice, type a nr: "))   
    if tasks:
        while choice_mainMenu < 1 or choice_mainMenu > 6:
            choice_mainMenu = int(input("Type nr 1 to 6: "))
    else:
        while choice_mainMenu < 1 or choice_mainMenu > 2:
            choice_mainMenu = int(input("Type nr 1 or 2: "))
    return choice_mainMenu

def create_task(tasks, FILE_TASKS):
    """Create task"""
    # Task id
    task_id = uuid
    
    print("\n" * 25)
    print(f"{BOLD}Add task{RESET}")
    print("─" * 53)

    # Task title
    task_title = input("Title: ")
    while len(task_title) > 25:
        task_title = input("To long title, max 25 characters: ")

    # Task description
    task_description = input("Description: ")
    while len(task_description) > 80:
        task_description = input("To long description, max 80 characters: ")
    
    # Time stamp created ad
    task_created_ad = time_date_stamp()
    
    # Task status
    task_status = "not completed"

    # Time stamp completed ad
    task_completed_ad = None

    new_task = {
        "id": task_id,
        "title": task_title,
        "description": task_description,
        "created_ad": task_created_ad,
        "status": task_status,
        "completed_ad": task_completed_ad
    }

    tasks.append(new_task)
    save(tasks=tasks, FILE_TASKS=FILE_TASKS)
    print(f"Task {new_task["title"]} is saved.")
    time.sleep(1)

def status_color(tasks):
    """Color status output"""
    status_color = None
    for index, task in enumerate(tasks):
        if task["status"] == "Not completed":
            status_color = RED_BOLD + task["status"] + RESET
        elif task["status"] == "In progress":
            status_color = YELLOW_BOLD + task["status"] + RESET
        elif task["status"] == "Completed":
            status_color = GREEN_BOLD + task["status"] + RESET
        print(f"{CYAN_BOLD}{index}. {RESET}{task["title"]}: {task["description"]} {status_color}")

def edit_task(tasks, FILE_TASKS):
    """Edit tasks"""
    
    # Header
    print("\n" * 25)
    print(f"{BOLD}Edit task{RESET}")
    print("─" * 53)
    status_color(tasks=tasks)
    print("─" * 53)
    print()
    
    # Edit choise, what task to change
    edit_choice = int(input(f"Wich task you want to edit, type 0 to {len(tasks)-1}: "))
    while edit_choice < 0 or edit_choice >= len(tasks):
        edit_choice = int(input(f"Invalid index, type 0 to {len(tasks)-1}: "))
    
    edit = tasks[edit_choice]

    print("\n" * 25)
    print(f"{BOLD}Edit{RESET}")
    print("─" * 53)
    print(f"Title: {edit["title"]}")
    print(f"Description: {edit["description"]}")
    color_status = None
    if edit["status"] == "Not completed":
        color_status = RED_BOLD + edit["status"] + RESET
    elif edit["status"] == "In progress":
        color_status = YELLOW_BOLD + edit["status"] + RESET
    elif edit["status"] == "Completed":
        color_status = GREEN_BOLD + edit["status"] + RESET
    print(f"Status: {color_status}")
    print("─" * 53)
    print()
    print("Leave empty if you dont want to change")
    print()

     # Edit task title
    edit_title = input("Edit title: ")
    while len(edit_title) > 25:
        edit_title = input("To long title, max 25 characters: ")

    # Edit task description
    edit_description = input("Edit description: ")
    while len(edit_description) > 80:
        edit_description = input("To long description, max 80 characters: ")
    
    # Edit task status
    edit_status = int(input("Edit status:\n"
                            f"{CYAN_BOLD}1. {RESET}Not completed\n"
                            f"{CYAN_BOLD}2. {RESET}In progress\n"
                            f"{CYAN_BOLD}3. {RESET}Completed\n"
                            "Make youre choise type 1 to 3: "))
    while edit_status < 1 or edit_status > 3:
        edit_status = int(input("Invalid choice, type 1, 2 or 3: "))
    if edit_status == 1:
        edit_status = "Not completed"
    elif edit_status == 2:
        edit_status = "In progress"
    elif edit_status == 3:
        edit_status = "Completed"
    
    # Change edit
    if edit_title:
        edit["title"] = edit_title
    if edit_description:
        edit["description"] = edit_description
    if edit_status:
        edit["status"] = edit_status
    
    # Save edit
    save(tasks=tasks, FILE_TASKS=FILE_TASKS)
    print(f"Task: {edit_title} is changed.")
    time.sleep(1)





def taskManager(tasks, FILE_TASKS):
    Exit = False
    read_anim()
    
    while Exit is False:
        print("\n" * 25)
        print(logo)
        main_menu(tasks)
        choice_mainMenu = choice_main_menu(tasks)
       
        if choice_mainMenu == 1:
            print()
            print("Exit taskmanager.\n" \
            "Have a great day.")
            Exit = True
            break
        elif choice_mainMenu == 2:
            create_task(tasks=tasks, FILE_TASKS=FILE_TASKS)
        elif choice_mainMenu == 3:
            edit_task(tasks=tasks, FILE_TASKS=FILE_TASKS)
            


tasks = read(FILE_TASKS)
taskManager(tasks=tasks, FILE_TASKS=FILE_TASKS)

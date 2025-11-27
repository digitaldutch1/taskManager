
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
    task_status = "Not completed"

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

def taskManager(tasks, FILE_TASKS):
    Exit = False
    read_anim()
    
    while Exit is False:
        print("\n" * 25)
        print(logo)
        main_menu(tasks)
        choice_mainMenu = choice_main_menu(tasks)
       
        if choice_mainMenu == 1:
            print("Exit taskmanager.\n" \
            "Have a great day.")
            Exit = True
            break
        elif choice_mainMenu == 2:
            create_task(tasks=tasks, FILE_TASKS=FILE_TASKS)
        
            
    


tasks = read(FILE_TASKS)
taskManager(tasks=tasks, FILE_TASKS=FILE_TASKS)

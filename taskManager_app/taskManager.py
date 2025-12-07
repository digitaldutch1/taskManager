
import json
import os
import uuid
from datetime import datetime
import time
from style import *

FILE_TASKS = "tasks.json"
uuid = uuid.uuid4().hex[:8]
clean_screen = 50
separate_line = 53

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
        print("─" * separate_line)
        print(f"{CYAN_BOLD}1. {RESET}{BOLD}Exit{RESET}")  
        print(f"{CYAN_BOLD}2. {RESET}{BOLD}Ad task{RESET}")
        print(f"{CYAN_BOLD}3. {RESET}{BOLD}Edit task{RESET}")
        print(f"{CYAN_BOLD}4. {RESET}{BOLD}Delete task{RESET}")
        print(f"{CYAN_BOLD}5. {RESET}{BOLD}Show tasks{RESET}")
        print(f"{CYAN_BOLD}6. {RESET}{BOLD}Change status{RESET}")
        print("─" * separate_line)
    else:
        print("─" * separate_line)
        print(f"{CYAN_BOLD}1. {RESET}{BOLD}Exit{RESET}")  
        print(f"{CYAN_BOLD}2. {RESET}{BOLD}Ad task{RESET}")
        print("─" * separate_line)

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
    
    print("\n" * clean_screen)
    print(f"{BOLD}Add task{RESET}")
    print("─" * separate_line)

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
    print("\n" * clean_screen)

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
    print("\n" * clean_screen)
    print(f"{BOLD}Edit task{RESET}")
    print("─" * separate_line)
    status_color(tasks=tasks)
    print("─" * separate_line)
    print()
    
    # Edit choise, what task to change
    edit_choice = int(input(f"Wich task you want to edit, type 0 to {len(tasks)-1}: "))
    while edit_choice < 0 or edit_choice >= len(tasks):
        edit_choice = int(input(f"Invalid index, type 0 to {len(tasks)-1}: "))
    
    edit = tasks[edit_choice]

    print("\n" * clean_screen)
    print(f"{BOLD}Edit{RESET}")
    print("─" * separate_line)
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
    print("─" * separate_line)
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
        edit["completed_ad"] = time_date_stamp()
    
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
    print("\n" * clean_screen)

def delete_task(tasks, FILE_TASKS):
    # Header
    print("\n" * clean_screen)
    print(f"{BOLD}Delete task{RESET}")
    print("─" * separate_line)
    status_color(tasks=tasks)
    print("─" * separate_line)
    print()

    # Edit choise, what task to delete
    delete_choice = int(input(f"Wich task you want to delete, type 0 to {len(tasks)-1}: "))
    while delete_choice < 0 or delete_choice >= len(tasks):
        delete_choice = int(input(f"Invalid index, type 0 to {len(tasks)-1}: "))
    
    delete = tasks[delete_choice]

    print("\n" * clean_screen)
    print(f"{BOLD}Edit{RESET}")
    print("─" * separate_line)
    print(f"Title: {delete["title"]}")
    print(f"Description: {delete["description"]}")
    color_status = None
    if delete["status"] == "Not completed":
        color_status = RED_BOLD + delete["status"] + RESET
    elif delete["status"] == "In progress":
        color_status = YELLOW_BOLD + delete["status"] + RESET
    elif delete["status"] == "Completed":
        color_status = GREEN_BOLD +delete["status"] + RESET
    print(f"Status: {color_status}")
    print("─" * separate_line)
    print()
    
    # Confirm delete
    confirm = input("Are you sure you want to delete this task y/n: ").strip().lower()
    while not (confirm == "y" or confirm == "n"):
        confirm = input("Invalid input, type y or n: ").strip().lower()
    
    # Delete task
    if confirm == "y":
        print(f"Task: {delete["title"]} is deleted.")
        time.sleep(1)
        del tasks[delete_choice]
        save(tasks=tasks, FILE_TASKS=FILE_TASKS)
    else:
        print(f"Nothing is deleted.")
        time.sleep(1)
    print("\n" * clean_screen)

def show_tasks(tasks):
    print("\n" * clean_screen)
    print("─" * separate_line)

    for index, task in enumerate(tasks):
        print(f"{CYAN_BOLD}{index}.{RESET}")
        print(f"{BOLD}Id: {RESET}{task["id"]}")
        print(f"{BOLD}Title: {RESET}{task["title"]}")
        print(f"{BOLD}Description: {RESET}{task["description"]}")
        print(f"{BOLD}Created_ad: {RESET}{task["created_ad"]}")
        show_color_status = None
        if task["status"] == "Not completed":
            show_color_status = RED_BOLD + task["status"] + RESET
        elif task["status"] == "In progress":
            show_color_status = YELLOW_BOLD + task["status"] + RESET
        elif task["status"] == "Completed":
            show_color_status = GREEN_BOLD + task["status"] + RESET
        
        print(f"{BOLD}Status: {RESET}{show_color_status}")
        print(f"{BOLD}Completed_ad: {RESET}{task["completed_ad"]}")
        print("─" * separate_line)

def change_status(tasks, FILE_TASKS):
    """Change status"""
    # Header
    print("\n" * clean_screen)
    print(f"{BOLD}Change status{RESET}")
    print("─" * separate_line)
    status_color(tasks=tasks)
    print("─" * separate_line)
    print()
    
    # Edit choise, what task to delete
    change_status_choice = int(input(f"Wich task you want to change, type 0 to {len(tasks)-1}: "))
    while change_status_choice < 0 or change_status_choice >= len(tasks):
        change_status_choice = int(input(f"Invalid index, type 0 to {len(tasks)-1}: "))
    
    change_status = tasks[change_status_choice]
    
    print("\n" * clean_screen)
    print(f"{BOLD}Change status{RESET}")
    print("─" * separate_line)
    print(f"Title: {change_status["title"]}")
    print(f"Description: {change_status["description"]}")
    show_task_color_status = None
    if change_status["status"] == "Not completed":
        show_task_color_status = RED_BOLD + change_status["status"] + RESET
    elif change_status["status"] == "In progress":
        show_task_color_status = YELLOW_BOLD + change_status["status"] + RESET
    elif change_status["status"] == "Completed":
        show_task_color_status = GREEN_BOLD +change_status["status"] + RESET
    print(f"Status: {show_task_color_status}")
    print("─" * separate_line)
    print()

    # Change status
    change_task_status = int(input("Change status:\n"
                            f"{CYAN_BOLD}1. {RESET}Not completed\n"
                            f"{CYAN_BOLD}2. {RESET}In progress\n"
                            f"{CYAN_BOLD}3. {RESET}Completed\n\n"
                            "Make youre choise type 1 to 3: "))
    print()
    while change_task_status < 1 or change_task_status > 3:
        change_task_status = int(input("Invalid choice, type 1, 2 or 3: "))
    if change_task_status == 1:
        change_task_status = "Not completed"
    elif change_task_status == 2:
        change_task_status = "In progress"
    elif change_task_status == 3:
        change_task_status = "Completed"
        change_status["completed_ad"] = time_date_stamp()

    if change_task_status:
        change_status["status"] = change_task_status
    
    # Save status
    save(tasks=tasks, FILE_TASKS=FILE_TASKS)
    print(f"{change_status["title"]} Status is changed to: {BOLD}{change_status["status"]}{RESET}.")
    time.sleep(1)
    print("\n" * clean_screen)
    




def taskManager(tasks, FILE_TASKS):
    Exit = False
    read_anim()
    print("\n" * clean_screen)

    while Exit is False:

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
        elif choice_mainMenu == 4:
            delete_task(tasks=tasks, FILE_TASKS=FILE_TASKS)
        elif choice_mainMenu == 5:
            show_tasks(tasks=tasks)
        elif choice_mainMenu == 6:
            change_status(tasks=tasks, FILE_TASKS=FILE_TASKS)
            


tasks = read(FILE_TASKS)
taskManager(tasks=tasks, FILE_TASKS=FILE_TASKS)


Taskmanager

This is a simple console taskmanager.
python version 3.13.2 is used to create this app

Instructions to use the taskmanager:
download python version 3.9 or higher: https://www.python.org/downloads/
download rootmap taskManager on github

start taskmanager:
- open cmd
- navigate to the rootmap taskManager
- python taskManager_app/taskManager.py



I chose simple design.
I used a small logo.
The logo and color codes are imported from the style.py page.
Titles are straigh forward.
I used continues lines as separator.
There are different colors used on incomplete, in progress and completed to make them stand out

Main menu:
* Exit (Exit taskmanager)
* Ad_task (Adding a task)
* Edit_task (Edit excisting tasks)
* Delete_task (Delete tasks)
* Show_tasks (Showing all tasks)
* Change_status (Change status tasks)

The status you can change in both edit or change status.
All tasks are timestamped with date and time on when they are created and timestamped again with date and time when you change the status to completed.
The tasks are being saved in the file tasks.json
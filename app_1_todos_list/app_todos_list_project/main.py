"""
Project: App daily todo list
Author: Kien Nguyen
"""
import os

def print_out_list_of_task(lines_list):
    if lines_list != []:
        print("--- List of existing task ---")
        for index, element in enumerate(lines_list):
            print(f"\t{index+1}. {element.capitalize()}", end="")
        print("-------- End of List --------")
    else: 
        print("--- There is no task for now ---")
        
# Output folder path.
output_folder_path = r"./output"

# Create output if it doesn't exist.
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

while True:
    user_action = input("Type add, show, edit, completed or exit: ").lower().strip()

    if "add" in user_action:
        lines = []
        
        # When the file wasn't created yet
        try:
            with open(r"./output/file_todo_list.txt", "r", encoding = "utf-8    ") as file:
                lines = file.readlines() 
        except FileNotFoundError:
            lines = []

        # new_task = input("Enter new task: ").capitalize().strip() + "\n"
        if user_action.strip().lower() == 'add':
            new_task = input("Enter new task: ").capitalize().strip() + "\n"
        else:
            new_task = user_action.replace('add', '').strip() + "\n" 
        
        # Add new task to the list    
        lines.append(new_task)
        
        # Write to file
        with open(r"./output/file_todo_list.txt", "w", encoding = "utf-8    ") as file:
            file.writelines(lines)              

        # Show the list of task        
        print_out_list_of_task(lines)

    elif "show" in user_action:
        try: 
            with open("./output/file_todo_list.txt","r") as file:
                todo_list = file.readlines()
            print_out_list_of_task(todo_list)
        except:
            print("--- There is no task for now ---")

    elif "edit" in user_action:
        
        todo_list = []
        try:
            with open("./output/file_todo_list.txt", "r") as file:
                todo_list = file.readlines()
                for index , item in enumerate(todo_list):
                    print("\t",index + 1, ". ", item.capitalize(), end = '')
        except:
            print("--- There is no task for now ---")
            continue
            
        num = int(input("select the number you want to edit: "))
        
        with open("./output/file_todo_list.txt", "w") as file:
            todo_list[num- 1] = (input("Enter new thing todo: ") + "\n")
            file.writelines(todo_list)

    elif "completed" in user_action:
        with open("./output/file_todo_list.txt", "r") as file:
            todo_list = file.readlines()
            if todo_list == []:
                print("--- There is nothing to do now ---")
                continue
            print_out_list_of_task(todo_list)
        done = int(input("Enter number of completed task: "))
        thing_completed = todo_list.pop(done-1)[:-1]
        with open("./output/file_todo_list.txt", "w") as file:
            file.writelines(todo_list)
        message = f"The task '{thing_completed}' was done."
        print(message)

    elif "exit" in user_action:
        break





         
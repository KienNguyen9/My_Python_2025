"""
Project: App daily todo list
Author: Kien Nguyen
"""
import os

current_file_path = os.path.abspath(__file__)
current_path = os.path.dirname(current_file_path)

# File and folder paths
ABS_OUTPUT_PATH = current_path + "\\output\\file_todo_list.txt"
output_folder_path = current_path + "\\output"


def print_out_list_of_task(lines_list):
    if lines_list != []:
        print("--- List of existing task ---")
        for index, element in enumerate(lines_list):
            print(f"\t{index+1}. {element.capitalize()}", end="")
        print("-------- End of List --------")
    else: 
        print("--- There is no task for now ---")

def get_todos_list(output_file_path = ABS_OUTPUT_PATH):    
    with open(output_file_path, 'r') as file_local:
        todos_local = file_local.readlines()  
    return todos_local 



# Create output if it doesn't exist.
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)
while True:
    user_action = input("Type add, show, edit, completed or exit: ").lower().strip()
    
    # Option 1
    if user_action.startswith("add"):
        lines = []
        # When the file wasn't created yet
        try:
            lines = get_todos_list()
        except FileNotFoundError:
            lines = []

        if user_action.strip().lower() == 'add':
            new_task = input("Enter new task: ").capitalize().strip() + "\n"
        elif user_action.strip().lower().startswith("add "):
            new_task = user_action[4:].strip().capitalize() + "\n" 
            
        # Add new task to the list    
        lines.append(new_task)
        print(f"'{new_task} was written to the list.")

        # Write to file
        with open(ABS_OUTPUT_PATH, "w", encoding = "utf-8") as file:
            file.writelines(lines)              
        # Show the list of task        
        print_out_list_of_task(lines)

    # Option 2
    elif user_action.startswith("show"):
        try: 
            todos = get_todos_list()
            print_out_list_of_task(todos)
        except:
            print("--- There is no task for now ---")

    # Option 3
    elif user_action.startswith("edit"):
        try:
            index_num = int(user_action[5:]) - 1        
            try:
                todos = get_todos_list()
                if todos == []:
                    print("--- There is no task for edit ---")
                    continue
            except:
                print("--- There is no task for now ---")
                continue

            print(index_num)
            new_todo = input("Enter you new todo: ")    
            todos[index_num] = new_todo + "\n"        
            with open(ABS_OUTPUT_PATH, "w", encoding="UTF-8") as file:
                file.writelines(todos) 
        except ValueError:
            print("Your command is not valid.")
            continue

    # Option 4
    elif user_action.startswith("completed"):
        try:
            index_number = int(user_action[10:]) - 1
            todos  = get_todos_list()
            todos.pop(index_number)

            with open(ABS_OUTPUT_PATH, "w", encoding="UTF-8") as file:
                file.writelines(todos)
        except IndexError as e:
            print("Your command is not valid: ", e)
            continue           
        except ValueError as e:
            print("Your command is not valid: ", e )
            continue           

    # Option 5
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print('Good bye, see you later!')




         
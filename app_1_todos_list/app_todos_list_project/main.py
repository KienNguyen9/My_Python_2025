"""
Project: App daily todo list
Author: Kien Nguyen
"""
import os
OUTPUT_PATH = "//output//file_todo_list.txt"
current_file_path = os.path.abspath(__file__)
current_path = os.path.dirname(current_file_path)
abs_output_path = current_path + OUTPUT_PATH

def print_out_list_of_task(lines_list):
    if lines_list != []:
        print("--- List of existing task ---")
        for index, element in enumerate(lines_list):
            print(f"\t{index+1}. {element.capitalize()}", end="")
        print("-------- End of List --------")
    else: 
        print("--- There is no task for now ---")

# Output folder path.
abs_output_dir_path = current_path + "\\output"

# Create output if it doesn't exist.
if not os.path.exists(abs_output_dir_path):
    os.makedirs(abs_output_dir_path)

while True:
    user_action = input("Type add, show, edit, completed or exit: ").lower().strip()

    if user_action.startswith("add ") or user_action.startswith("add"):
        lines = []
        # When the file wasn't created yet
        try:
            with open(abs_output_path, "r", encoding = "utf-8") as file:
                lines = file.readlines() 
        except FileNotFoundError:
            lines = []

        # new_task = input("Enter new task: ").capitalize().strip() + "\n"
        if user_action.strip().lower() == 'add':
            new_task = input("Enter new task: ").capitalize().strip() + "\n"
        elif user_action.strip().lower().startswith("add "):
            new_task = user_action[4:].strip().capitalize() + "\n" 
            
        # Add new task to the list    
        lines.append(new_task)
        print(f"'{new_task} was written to the list.")

        # Write to file
        with open(abs_output_path, "w", encoding = "utf-8") as file:
            file.writelines(lines)              
        # Show the list of task        
        print_out_list_of_task(lines)
    elif user_action.startswith("show"):
        try: 
            with open(abs_output_path, "r", encoding="utf-8") as file:
                todo_list = file.readlines()
            print_out_list_of_task(todo_list)
        except:
            print("--- There is no task for now ---")
    elif user_action.startswith("edit"):
        try:
            index_num = int(user_action[5:]) - 1        
            try:
                with open(abs_output_path, "r", encoding="utf-8") as file:
                    todos = file.readlines()
                    if todo_list == []:
                        print("--- There is no task for edit ---")
                        continue
                    # for index , item in enumerate(todo_list):
                    #     print("\t",index + 1, ". ", item.capitalize(), end = '')
            except:
                print("--- There is no task for now ---")
                continue
            print(index_num)
            # with open("./output/file_todo_list.txt", "r", encoding="UTF-8") as file:
            #     todos = file.readlines()        
            new_todo = input("Enter you new todo: ")    
            todos[index_num] = new_todo + "\n"        
            with open(abs_output_path, "w", encoding="UTF-8") as file:
                file.writelines(todos) 
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("completed"):
        try:
            index_number = int(user_action[10:]) - 1
            with open(abs_output_path, "r", encoding="UTF-8") as file:
                todos  = file.readlines()
            todos.pop(index_number)
            with open(abs_output_path, "w", encoding="UTF-8") as file:
                file.writelines(todos)
        except IndexError as e:
            print("Your command is not valid: ", e)
            continue           
        except ValueError as e:
            print("Your command is not valid: ", e )
            continue           

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print('Good bye, see you later!')




         
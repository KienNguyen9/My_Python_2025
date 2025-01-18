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
        
current_path = os.path.abspath(__file__)
print(current_path)

# Output folder path.
output_folder_path = r"./output/"

# Create output if it doesn't exist.
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

while True:
    user_action = input("Type add, show, edit, completed or exit: ").lower().strip()

    if user_action.startswith("add "):
        lines = []
        # When the file wasn't created yet
        try:
            with open(r"./output/file_todo_list.txt", "r", encoding = "utf-8") as file:
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
        with open(r"./output/file_todo_list.txt", "w", encoding = "utf-8") as file:
            file.writelines(lines)              
        # Show the list of task        
        print_out_list_of_task(lines)

    elif user_action.startswith("show"):
        try: 
            with open("./output/file_todo_list.txt", "r", encoding="utf-8") as file:
                todo_list = file.readlines()
            print_out_list_of_task(todo_list)
        except:
            print("--- There is no task for now ---")
    elif user_action.startswith("edit"):
        # todo_list = []
        # try:
        #     with open("./output/file_todo_list.txt", "r", encoding="utf-8") as file:
        #         todo_list = file.readlines()
        #         if todo_list == []:
        #             print("--- There is no task for edit ---")
        #             continue
        #         for index , item in enumerate(todo_list):
        #             print("\t",index + 1, ". ", item.capitalize(), end = '')
        # except:
        #     print("--- There is no task for now ---")
        #     continue
        # if user_action.lower().strip().startswith("edit"):
        #     task_edit = user_action[:4] 
        #     with open("./output/file_todo_list.txt", "w", encoding="utf-8") as file:
        #         old_task = todo_list[num- 1]
        #         todo_list[num- 1] = task_edit
        #         file.writelines(todo_list)
        #         print(f"'{old_task}' was updated by '{task_edit}'.")
        # else:
        #     num = int(input("Select the number you want to edit: "))
        # with open("./output/file_todo_list.txt", "w", encoding="UTF-8") as file:
        #     todo_list[num- 1] = (input("Enter new thing todo: ") + "\n")
        #     file.writelines(todo_list)
        index_num = int(user_action[5:]) - 1        
        
        try:
            with open("./output/file_todo_list.txt", "r", encoding="utf-8") as file:
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
        with open("./output/file_todo_list.txt", "w", encoding="UTF-8") as file:
            file.writelines(todos) 
    elif user_action.startswith("completed"):
        # try: 
        #     with open("./output/file_todo_list.txt", "r", encoding="UTF-8") as file:
        #         todo_list = file.readlines()
        #         if todo_list == []:
        #             print("--- There is nothing to do now ---")
        #             continue
        #         print_out_list_of_task(todo_list)
        # except:
        #     print("--- There is no task for now ---")
        #     continue
        # done = int(input("Enter number of completed task: "))
        # thing_completed = todo_list.pop(done-1)[:-1]
        # with open("./output/file_todo_list.txt", "w", encoding="utf-8") as file:
        #     file.writelines(todo_list)
        # message = f"The task '{thing_completed}' was done."
        # print(message)

        index_number = int(user_action[10:]) - 1
        with open("./output/file_todo_list.txt", "r", encoding="UTF-8") as file:
            todos  = file.readlines()
        todos.pop(index_number)
        with open("./output/file_todo_list.txt", "w", encoding="UTF-8") as file:
            file.writelines(todos)

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print('Good bye, see you later!')




         
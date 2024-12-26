"""
Project: App daily todo list
Author: Kien Nguyen
"""

while True:
    user_action = input("Type add, show, edit, completed or exit.").strip()
    match user_action:
        case "add":
            try:
                lines = []
                with open(r"./output/file_todo_list.txt", "r", encoding = "utf-8    ") as file:
                    lines = file.readlines() 
                new_task = input("Enter new task: ").capitalize().strip() + "\n"
                lines.append(new_task)
                with open(r"./output/file_todo_list.txt", "w", encoding = "utf-8    ") as file:
                    file.writelines(lines)              
            except Exception as e:
                print(f"An error occurred: {e}")

        case "show":
            with open("./output/file_todo_list.txt","r") as file:
                todo_list = file.readlines()
                for index , item in enumerate(todo_list):
                    print("\t",index + 1, ". ", item.capitalize(), end = '')

        case "edit":
            todo_list = []
            with open("./output/file_todo_list.txt", "r") as file:
                todo_list = file.readlines()
                for index , item in enumerate(todo_list):
                    print("\t",index + 1, ". ", item.capitalize(), end = '')

            num = int(input("select the number you want to edit: "))
            
            with open("./output/file_todo_list.txt", "w") as file:
                todo_list[num- 1] = (input("Enter new thing todo: ") + "\n")
                file.writelines(todo_list)

        case "completed":
            pass
        case "exit":
            break
            pass





         
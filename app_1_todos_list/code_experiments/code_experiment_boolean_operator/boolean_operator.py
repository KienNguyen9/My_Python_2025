# Boolean operator
# "and", "or", "not"

while True:
    user_action  = input("Enter your action: ")
    if "add" in user_action and "." in user_action:
        print("added")
    if user_action == "exit":
        break

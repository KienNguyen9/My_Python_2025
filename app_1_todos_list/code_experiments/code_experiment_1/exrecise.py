while True:
    new_member = input("Enter new member or exit: ") 

    if new_member == "exit":
        break
    
    with open("./members.txt", "a+", encoding = "UTF-8") as file:
        lines = ''.join(file.readlines()) + "\n"
        lines += (new_member)
        file.writelines(lines)


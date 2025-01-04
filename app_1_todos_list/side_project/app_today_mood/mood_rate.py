import os
date = input("What the day today? (yyyy-mm-dd)\nEnter the day today please: ")
mood = input("How do you rate your mood today 0-10?\nEnter your anwser please: ")
journal = input("Let your thoughts flow:\n")

out_put_path = "./journal"
if not os.path.exists(out_put_path):
    os.mkdir(out_put_path)

with open(f"./journal/{date}.txt", "w") as file:
    file.write(journal)
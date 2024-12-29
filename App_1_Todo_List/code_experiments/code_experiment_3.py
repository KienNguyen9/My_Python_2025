countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]

for item in countries:
    file_name = f"{item}.txt"
    with open(file_name, "w", encoding = "UTF-8") as file:
        file.write(item)
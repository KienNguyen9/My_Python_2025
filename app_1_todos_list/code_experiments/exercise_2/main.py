import os

current_path = os.path.abspath(__file__)

# data_folder_path = current_path.replace("main.py","data")
data_folder_path = r"data"

# easy way 
for file_name in os.listdir(data_folder_path):  
    # file_path = f"{data_folder_path}\\{file_name}" 
    file_path = f"./data/{file_name}" 
    with open(file_path, "r") as file:
        content = file.read()
        print(content)


# detail way
# for root, dirs, files in os.walk(folder_path):

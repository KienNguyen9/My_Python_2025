import sys
import os

current_script_path = os.path.abspath(__file__)
file_name = os.path.basename(__file__)
current_folder_path = current_script_path.split(file_name)[0].replace("\\","/")

def write_to_files():
    contents = ["How to aaa", "learn", "Python"]
    file_names = ["doc.txt", "report.txt", "presentation.txt"]

    for content, file_name in zip(contents, file_names):
        with    open(f"{current_folder_path}../output/{file_name}", "w") as file:
            file.writelines(content)

    a = "every things "\
        "Done"
    print(a)


if __name__ == "__main__":
    write_to_files()
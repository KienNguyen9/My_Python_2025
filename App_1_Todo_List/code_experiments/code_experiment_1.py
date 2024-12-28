contents = ["How to aaa", "learn", "Python"]
file_names = ["doc.txt", "report.txt", "presentation.txt"]

for content, file_name in zip(contents, file_names):
    with open(f"./../output/{file_name}", "w") as file:
        file.writelines(content)

print("Done!")
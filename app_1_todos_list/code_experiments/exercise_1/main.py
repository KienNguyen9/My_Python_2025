filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# first try
for file_name in filenames:
    file = open(file_name, "w")
    file.write("Hello")
    file.close()

# Second try
# for file_name in filenames:
    # with open(file, "w", encoding="UTF-8") as f:
    #     f.write("Hello")
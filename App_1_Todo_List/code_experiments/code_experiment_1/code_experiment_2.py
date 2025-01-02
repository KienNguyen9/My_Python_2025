countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']

# for country, file_name in zip(countries,filenames):
#     with open("file_name", 'w') as file:
#         file.write(country)

with open("file.txt", 'w') as file:
    file.write("abc")
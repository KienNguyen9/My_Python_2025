filenames = ['1.doc', '1.report', '1.presentation']
filenames = [filename.replace(".", "-") + ".txt" for filename in  filenames ]
print(filenames)


# multiples 2
numbers = [10, 20, 30]
numbers_multiplies = [number*2 for number in numbers]
print(numbers_multiplies)
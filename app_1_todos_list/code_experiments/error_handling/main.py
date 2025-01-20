try:
    width = int(input("Enter retangle width: "))
    length = int(input("Enter retangle length: "))
    
    if width == length:
        exit("It's a square.")
    
    area = width*length
    print(area)
except ValueError:
    print("Please enter a number.")
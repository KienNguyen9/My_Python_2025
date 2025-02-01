try:
    # Prompt the user to enter the total value and convert it to a float
    total = float(input("Enter total value: "))
 
    # Prompt the user to enter the value and convert it to a float
    value = float(input("Enter value: "))
    # Calculate the percentage using the formula value/total_value * 100
    percentage = value / total * 100 
    # Print the calculated percentage
    print(f"That is {percentage}%")
except ValueError:
    print("You need to enter a number, Run program again.")

try:
    # Prompt the user to enter the total value and convert it to a float
    total_value = float(input("Enter total value: "))
 
    # Prompt the user to enter the value and convert it to a float
    value = float(input("Enter value: "))
 
    # Calculate the percentage using the formula value/total_value * 100
    percentage = value / total_value * 100
 
    # Print the calculated percentage
    print(f"That is {percentage}%")
except ValueError:
    # Handle the case when the user doesn't enter a number
    print("You need to enter a number. Run the program again.")

'''
Convert feet inches to meter
'''
lenth_in_feet = input("Enter a feet and inches: ")


def convert_feet_inch_to_meter(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    # The cecipe in converting
    meters = feet*0.3048 + inches*0.0254
    return f"{feet} feet and {inches} inches is equal to {meters} meters."

print(convert_feet_inch_to_meter(lenth_in_feet))




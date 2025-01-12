import re
# code experiment 
prompt_s = "Strong pass word"
prompt_w = "Weak pass word"
prompt_n = "Pass word is not valid"

while True:
    result = {'Length': False, 'Number': False, 'Upper': False}

    pass_word = input("Enter the pass word: ")
    
    # length checking
    if len(pass_word) > 7:
        result["Length"] = True
    
    # Number checking 
    if any(char.isdigit() for char in pass_word):
        result["Number"] = True

    # Upper case checking
    if any(char.isupper() for char in pass_word):
        result["Upper"] = True


    if all(result.values()) == True:
        print(prompt_s)
        break
    else:
        print(prompt_w)
        print("Please, try a stronger pass word!")



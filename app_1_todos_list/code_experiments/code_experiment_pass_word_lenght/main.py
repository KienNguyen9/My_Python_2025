import re
# code experiment 
prompt_s = "Strong pass word"
prompt_w = "Weak pass word"
prompt_n = "Pass word is not valid"

while True:
    
    result = []
    pass_word = input("Enter the pass word: ")
    
    # length checking
    if len(pass_word) < 8:
        result.append(False)
    else:
        result.append(True)
    
    # Number checking 
    if any(char.isdigit() for char in pass_word):
        result.append(True)
    else:
        result.append(False)
    
    # Upper case checking
    if any(char.isupper() for char in pass_word):
        result.append(True)
    else:
        result.append(False)

    print(result)


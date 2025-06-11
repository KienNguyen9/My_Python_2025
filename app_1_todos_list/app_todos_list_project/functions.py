
def print_out_list_of_task(lines_list):
    if lines_list != []:
        print("--- List of existing task ---")
        for index, element in enumerate(lines_list):
            print(f"\t{index+1}. {element.capitalize()}", end="")
        print("-------- End of List --------")
    else: 
        print("--- There is no task for now ---")


def get_todos_list(output_file_path):    
    with open(output_file_path, 'r') as file_local:
        todos_local = file_local.readlines()  
    return todos_local 

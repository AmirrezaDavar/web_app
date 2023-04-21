# It is common practice to use variables repetitively used in the script
# benefit = saving time to modify the filepath name in all places in the code
# dir(functions)
FILEPATH = "todos.txt"


# custom functions => def to avoid repetitive codes
# this is the recipe
# filepath here is called parameter
# whenever you want to create a process, put it in a function => def
# this is a script on top of being a module when it's imported
def get_todos(filepath=FILEPATH):
    """ This is a docstring.
    This function reads a text file and return the list of
    to-do items.
    Use help(get_todos) to see this text.
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


# filepath and todos_arg are parameters since they
# are written in the function definition
# default arguments filepath. the order matters when calling the function


def write_todos(todos, filepath=FILEPATH):
    """ Write the to-do items in list in the text file.
    It is recommended to use docstrings for functions
    """
    with open(filepath, 'w') as file:
        file.writelines(todos)


# if-conditional-block
if __name__ == "__main__":
    # the value of __name__ here is __main__. However, outside of this functions.py
    # the value is functions
    print(type("__name__"))
    print("hello")
    print(get_todos())

# -------------------------------------------------------------------------------
# bonus example (specifying the water state)
# freezing_point = 0
# boiling_point = 100


# def state_water(temperature):
#     if boiling_point < temperature:
#         return "Gas"
#     elif freezing_point < temperature < boiling_point:
#         return "Liquid"
#     elif freezing_point > temperature:
#         return "Solid"
#     elif temperature == freezing_point:
#         return "Solid"
# -------------------------------------------------------------------------------
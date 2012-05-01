from os import getcwd #FOR TESTING
from sys import path #FOR TESTING
path.append(getcwd()) #FOR TESTING
#------------------------------------------------------------------------
from clui import base_clui

def my_condition_test(user_input,looped): #TODO: Move this docstring into actual documentation
    "A test function for a clui."
        
    if looped > 5: #Looped is an integer, that increases by one after each loop
        return (False,'test failed',"I don't want you to run after 5 loops!")
            
    return (True,'Test passed')
    
ui = base_clui()
ui.title = 'Testing'
ui.initial_message = "Doin' some test!"
ui.condition_tests = [my_condition_test] #Defaults to empty list

ui.execute()



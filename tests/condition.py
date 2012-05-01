from os import getcwd #FOR TESTING
from sys import path #FOR TESTING
path.append(getcwd()) #FOR TESTING
#------------------------------------------------------------------------
from clui import base_clui

def my_condition_test(user_input,looped): #TODO: Move this docstring into actual documentation
    "A test function for a clui."
        
    if looped > 3: #Looped is an integer, that increases by one after each loop
        return (False,'test failed',"I don't want you to run after 3 loops!")
            
    return (True,'Test passed')
    
def a_function():
    print "I am useless!"
    
ui = base_clui()
ui.title = 'Testing'
ui.initial_message = "Doin' some test!"
ui.condition_tests = [my_condition_test] #Defaults to empty list

ui.add(display_name='option',callables=[a_function,'dick'])
ui.add(display_name='moar stuff',patterns=['^moar *(stuff)?$'],callables=[a_function])
ui.execute()



from os import getcwd #FOR TESTING
from sys import path #FOR TESTING
path.append(getcwd()) #FOR TESTING

from clui import base_clui

def add_flashcards():
    print "Adding some flashcards..."

def delete_flashcards():
    print "Deleting all of the flashcards..."

class will_not_be_named(object):
    def __init__(self):
        print "This class will not be the name of added menu option, because it was not added first."

def exit_function():
    print "I am doing stuff that should be done when the program exits!"

def exit2():
    print "Tearing down stuff..."
    
def my_condition_test(user_input,looped): #TODO: Move this docstring into actual documentation
    "A test function for a clui."
    
    if looped > 5:
        return (False,'test failed')
    return (True,'Test passed')
    
ui = base_clui() #Create an instance of the base_clui class

#Here we define the interface's global attributes
#------------------------------------------------------------------------------
ui.title = 'Flashcards'
ui.initial_message = 'Welcome!'
ui.exit_words.append('^(goose|geese)$')
ui.exit_message = 'Thank you for using flashcards! Bye!' #Optional
ui.buffer = '^'*72  

ui.start_with_zero = True #Defaults to False
ui.display_exit_words = True #Defaults to False
ui.exit_callables = [exit_function,exit2] 
ui.input_message = 'Next: ' #Redundant - defaults to '> ' anyway
ui.condition_tests = [my_condition_test] #Defaults to empty list
#ui.display_all_callables = True #Defaults to False
#ui.display_all_regex = True #Defaults to False

#Here we add 'options' to the menu interface.
#Each menu option can over-ride the global attributes. #TODO: Implement this
#------------------------------------------------------------------------------
 
        
ui.add(
    callables=[delete_flashcards,will_not_be_named], #These will be called when this menu's patterns are matched.
    patterns=[ #These are regular expressions. clui will try to match them to your user's input.
        '^([Dd]elete|[Rr]emove)( *some)? *flashcards!?$'
    ],
    display_name = 'Delete some flashcards from your set', #What your users will see as the name of this option
    #display_callables = True,
) 

ui.add( #NOTE THERE IS NO DISPLAY_NAME
    callables=[add_flashcards],
    patterns = ['^add *(more|some)? *(flashcards?)?$',],
)

if __name__ == '__main__':
    ui.execute() #Enter mainloop

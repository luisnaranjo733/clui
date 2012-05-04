from os import getcwd #FOR TESTING
from sys import path #FOR TESTING
path.append(getcwd()) #FOR TESTING

from clui import base_clui

#Here are some generic functions - for demonstration only
#------------------------------------------------------------------------------

def add_flashcards():
    print "Adding some flashcards..."

def delete_flashcards():
    print "Deleting all of the flashcards..."

class will_not_be_named(object): #classes work too!
    def __init__(self):
        print "This class will not be the name of added menu option, because it was not added first."

def exit_function():
    print "I am doing stuff that should be done when the program exits!"
#------------------------------------------------------------------------------

#This is a condition test. You can use it to regulate your clui.
#------------------------------------------------------------------------------
def my_condition_test(user_input,looped):
    "A test function for a clui."
    
    max_loops = 5
    
    if looped > max_loops: #The looped variable is increased by one for each time the ui loops
        return (False,'test failed','The loops have exceeded: %d!' % max_loops)
        
    if user_input == 'debug':
        return (True, 'Entering debug mode...') #Enter your debugging code below
        
    else:
        return (True,'Test passed')
#------------------------------------------------------------------------------

ui = base_clui() #Create an instance of the base_clui class

#Here we define the interface's base attributes
#------------------------------------------------------------------------------
ui.title = 'Flashcards'
ui.initial_message = 'Welcome!'
ui.exit_words.append('^(goose|geese)$') #Adding a regex pattern to the default list
ui.exit_message = 'Thank you for using flashcards! Bye!' #Optional
ui.buffer = '^'*72  
ui.exit_callables = [exit_function] 
ui.input_message = 'Next: ' #defaults to '> '
ui.condition_tests = [my_condition_test] #These are used to refine

#Here are some of the other things you might change about your clui
#ui.display_exit_words = True #Defaults to False
#ui.start_with_zero = True #Defaults to False
#ui.display_all_callables = True #Defaults to False
#ui.display_all_regex = True #Defaults to False

#Here we add 'options' to the menu interface.
#------------------------------------------------------------------------------
 
        
ui.add(
    callables=[delete_flashcards,will_not_be_named], #These will be called when this menu's patterns are matched.
    patterns=[ #These are regular expressions. clui will try to match them to your user's input.
        '^([Dd]elete|[Rr]emove)( *some)? *flashcards!?$'
    ],
    display_name = 'Delete some flashcards from your set', #What your users will see as the name of this option
    #display_callables = True,
) 

ui.add( #Note that this 'option' has no display_name
    callables=[add_flashcards],
    patterns = ['^add *(more|some)? *(flashcards?)?$',],
) #It uses the name of the first callable as a display_name

if __name__ == '__main__':
    ui.execute() #Enter mainloop

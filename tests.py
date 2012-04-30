from clui import base_clui

def add_flashcards():
    print "Adding some flashcards..."
    print "All done!"

def delete_flashcards():
    print "Deleting all of the flashcards..."
    print "Done!"

class will_not_be_named(object):
    def __init__(self):
        print "This class will not be the name of added menu option, because it was not added first."

def exit_function():
    print "I am doing stuff that should be done when the program exits!"

def exit2():
    print "TEARDOWN"
    
def my_condition_test(user_input,looped):
    if user_input == 'dick':
        return False
    return True

ui = base_clui() #Create an instance of the base_clui class

#Here we define the interface's global attributes
#------------------------------------------------------------------------------
ui.title = 'Flashcards'
ui.initial_message = 'Welcome!'
ui.exit_words.append('^(goose|geese)$')
ui.exit_message = 'Thank you for using flashcards! Bye!' #Optional
ui.start_with_zero = True #Defaults to False
#ui.display_all_callables = True #Defaults to False
ui.display_all_regex = True #Defaults to False
#ui.display_exit_words = True #Defaults to False
ui.exit_callables = [exit_function,exit2] 
ui.input_message = ': ' #Defaults to '> '
ui.condition_tests = [my_condition_test] #Defaults to empty list

#Here we add 'options' to the menu interface.
#Each menu option can over-ride the global attributes. #TODO: Implement this
#------------------------------------------------------------------------------
"""
        callables = kwargs.pop('callables',None)
        patterns = kwargs.pop('patterns',None)
        display_name = kwargs.pop('display_name',None)
        display_callables = kwargs.pop('display_callables',False)
        display_regex = kwargs.pop('display_regex',False)"""
        
ui.add(
    callables=[delete_flashcards,will_not_be_named], #These will be called when this menu's patterns are matched.
    patterns=[ #These are regular expressions. clui will try to match them to your user's input.
        '^[Rr]emove flashcards$',
        '^[Dd]elete flashcards!?$'
    ],
    display_name = 'Delete some flashcards from your set', #What your users will see as the name of this option
) 

ui.add(
    callables=[add_flashcards],
    display_name='Add some flashcards!',
    display_regex = True,
    display_callables = True
)

ui.execute()

from clui import base_clui

def add_flashcards():
    print "Adding some flashcards..."
    print "All done!"

def delete_flashcards():
    print "Deleting all of the flashcards..."
    print "Done!"

class will_not_be_named(object):
    def __init__(self):
        print "This function will not be the name of added menu option, because it was not added first."

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
ui.exit_words.append('^(goose|geese)$')
ui.exit_message = 'Thank you for using flashcards! Bye!' #Optional
ui.start_with_zero = True #Defaults to False
ui.display_all_callables = True #Defaults to False
ui.display_all_regex = True #Defaults to False
ui.display_exit_words = True #Defaults to False
ui.exit_callables = [exit_function,exit2] 
ui.input_message = ': ' #Defaults to '> '
ui.condition_tests = [my_condition_test] #Defaults to empty list

#Here we add 'options' to the menu interface.
#Each menu option can over-ride the global attributes. #TODO: Implement this
#------------------------------------------------------------------------------
ui.add(
    callables=[delete_flashcards,will_not_be_named],
    patterns=[
        '[Rr]emove flashcards',
        '[Dd]elete flashcards!?'
    ],
    display_callables = True,
) 

ui.add(
    callables=[add_flashcards],
    patterns=['[Aa]dd ?(flashcards)?','(moar|more)'],
    display_name='Add some flashcards!',
    display_regex = True,
)

ui.execute()

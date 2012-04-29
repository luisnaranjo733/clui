from clui import base_clui
import random

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
    
def test_condition(looped):
    val = 4#random.randint(1,2)
    if val == 1: return True
    if val == 2: return False
    if looped == 5: return False
    return True

title = 'Flashcards'
initial_message = 'Flashcards is a python utility designed to help you know your stuff!'
exit_message = 'Bye! I hope you enjoyed your stay.'

ui = base_clui()
ui.title = title
ui.initial_message = initial_message
ui.exit_message = exit_message
ui.exit_words.append('precise *(pangolin)?')
#ui.start_with_zero=True #DOCUMENT
#ui.display_all_callables = True
ui.exit_callables = [exit_function,exit2] #A list of callables that will called
ui.condition_tests = [test_condition]
#recursively, and in order.

ui.input_message = 'Next: '

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

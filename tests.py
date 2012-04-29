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

title = 'Flashcards'
initial_message = 'Flashcards is a python utility designed to help you know your stuff!'
exit_message = 'Bye! I hope you enjoyed your stay.'
exit_words = ['end','exit','leave','bye','idgaf']

ui = base_clui()
ui.title = title
ui.initial_message = initial_message
ui.exit_message = exit_message
ui.exit_words = exit_words
#ui.start_with_zero=True #DOCUMENT
#ui.display_all_callables = True

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
    #display_callables = True,
)

ui.execute()

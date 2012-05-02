Additional control
==================

Condition tests
----------------

You can pass :term:`condition tests` to clui, if you need more fine tuned control over your clui.

The default :term:`condition` is **True**, but you can change that to *any thing you want*.

*Make sure you can match that value*.

Requirements of condition tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1) **Must** take *two* positional arguments.

   The first positional argument is the last string that the user entered.
   
   The second positional argument is an integer representation of the number
   of loops the clui has gone through.
      
2) **Must** return a *condition*, **or** a list/tuple with a *condition* in it.

   If a list or tuple is used, the *condition* **must be the first item** in the list.
   
   Everything value in the container *after that* will be printed to the screen!
   
An example
^^^^^^^^^^
::

    from clui import base_clui

    def my_condition_test(user_input,looped):
        "A condition test function for a clui."
            
        if looped > 3: #Looped is an integer, that increases by one after each loop
            return (False,'test failed',"I don't want you to run after 3 loops!")
                
        return (True,'Test passed') #IMPORTANT - without returning the set condition, your loop would fail.
            
    def a_function(): #This is a generic callable. Just for fun.
        print "I am useless!"
        
    ui = base_clui()
    ui.title = 'Testing'
    ui.initial_message = "Doin' some test!"
    ui.condition_tests = [my_condition_test]

    ui.add(display_name='option',callables=[a_function,'Wheee!'])
    ui.add(display_name='moar stuff',patterns=['^moar *(stuff)?$'],callables=[a_function])
    ui.execute()


Would give you this:

.. image:: condition.png

Exit callables
--------------

Clui lets you define :term:`exit callables`, which are called before your clui terminates.

They are defined in the BASE_CLUI(link) attributes, but can also be passed as named arguments

base_clui (link) attributes/parameters
---------------------------------------

title (**string**):
   The title of your :term:`clui`

initial_message (**string**):
   Use this for any additional information you want to display (usage, author, license, version, homepage, etc...)
 
exit_words (**list**):
   A list of regex strings. It matches the user's input to these and exits the :term:`clui` if it finds a match.
   
   The **defaults** are ['^end$','^exit$','^leave$','^bye'$]

exit_message (**string**):
   This is the message that :term:`clui` displays when the user exits the interface.

start_with_zero (**boolean**):
   This toggles the start of the menu's index between 0 and 1.
   
   This affects the menu options' pattern as well.
   
display_all_callables (**boolean**):
   If activated, a string representation of the list which contains the callables for each menu option will be displayed.
   
display_all_regex (**boolean**):
    

display_exit_words (**boolean**):

exit_callables (**list**):

input_message (**string**):

condition (**BOOLEAN**):

condition_tests (**list of callables**):

enable_clear (**boolean**):

base_clui.add parameters (link) 
-------------------------------

It has the following parameters:

callables (positional)
   This is a **list** of callable functions/classes that :term:`clui` will execute
   for that menu option (in the order that they were defined).
   These callables **do not take any positional parameters** at this time.

patterns (defaults to the name of the first callable)
   A **list** of regex strings that :term:`clui` will use to match to user input (in order).
   If a match is found, the corresponding callables will executed.

display_name (defaults to the name of the first callable)
   This is the **string** that will actually be displayed to the user for
   this option in the menu.

display_callables (defaults to False)
   This boolean defines controls whether or not an additional list of callables is
   added for *each* menu option.
            
display_regex (bool - defaults to False)
   This toggles the display of the list of regex strings that correspond to each menu option.s

Clear
-----

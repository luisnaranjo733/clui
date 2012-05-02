Additional control
==================

Condition tests
---------------

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

They are defined in the BASE_CLUI attributes, but can also be passed as named arguments



Boolean Logic
-------------


Extended attributes
--------------------

Clear
-----

Additional control
==================

Condition tests
---------------

1) **Must** take *two* positional arguments.

   The first positional argument is the last string that the user entered.
   
   The second positional argument is an integer representation of the number
   of loops the clui has gone through.
      
2) **Must** return a *boolean*.

   You can return a single boolean.
   
   *You can also return a tuple or list*, with the **boolean listed first**.
   *Everything listed after that boolean*, will be seperated by newlines,
   and then printed to the screen.
   
   For example, this::

    from clui import base_clui

    def my_condition_test(user_input,looped):
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

    ui.add(display_name='option',callables=[a_function,'Wheee!'])
    ui.add(display_name='moar stuff',patterns=['^moar *(stuff)?$'],callables=[a_function])
    ui.execute()

Would give you this:

.. image:: condition.png

Exit callables
--------------


Boolean Logic
-------------


Extended attributes
--------------------

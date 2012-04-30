#-------------------------------------------------------------------------------
# Name:        clui
# Purpose: Command Line User Interface
#
# Author:      Jose Luis Naranjo
#
# Created:     25/04/2012
# Copyright:   (c) jnaranjo 2012
# Licence:     GNU GPL3
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import re
import subprocess
from sys import platform
from colorama import Fore, Back, Style,init,deinit

init() #required for x-platform support by colorama

TODO = """
Resolve dependency issues - what to do if colorama is unavailable?
UPDATE DOCUMENTATION
    Minimalistic "Hello, World clui?" (3-4 lines)
function.func_name for classes?

customize colors in colorama

recursive message?
s
"""


class base_clui(object):
    """This is the base class for a command line user interface.
    
You can control the style of the interface with the attributes **AND OR** parameters
provided in this class. *All are optional.* Some more than others.

title (**string**):
   The title of your :term:`clui`

initial_message (**string**):
   Use this for any additional information you want to display (usage, author, license, version, homepage, etc...)
 
exit_words (**list**):
   A list of `regex`_ strings. It matches the user's input to these and exits the :term:`clui` if it finds a match.
   
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

"""

    def __init__(self,**kwargs):
        """The menu attribute is key here. All the 'add' method really does
        is add dictionaries to the options method, which are used to
        generate the :term:`clui`."""

        self.title = kwargs.pop('title', None)
        self.initial_message = kwargs.pop('initial_message', None)
        self.exit_words = kwargs.pop('exit_words', '^quit$ ^end$ ^exit$ ^leave$ ^bye$'.split())
        self.exit_message = kwargs.pop('exit_message', None)
        self.start_with_zero = kwargs.pop('start_with_zero',False)
        self.display_all_callables = kwargs.pop('display_all_callables',False)
        self.display_all_regex = kwargs.pop('display_all_regex',False)
        self.display_exit_words = kwargs.pop('display_exit_words',False)
        self.exit_callables = kwargs.pop('exit_callables',[])
        self.input_message = kwargs.pop('input_message','> ')
        self.condition = kwargs.pop('condition',True)
        self.condition_tests = kwargs.pop('condition_tests',[])
        self.enable_clear = kwargs.pop('enable_clear',True)
        self.menu = [] #List of options for the clui to use
        self.looped = 0 #Gets a +1 for each loop. In case tracking the amount of loops is ever important.

    def __menu__(self):
        """Returns a string representation of what the menu should look like.
        
        Uses the boolean attributes for it's logic"""

        line = ''

        for option in self.menu: #List of options
            colored = Fore.MAGENTA + option['display_name'] + Fore.RESET
            line += "{index}: {display_name}".format(index=option['index'],display_name=colored)

            if option['display_callables'] or self.display_all_callables: #
            
                callables = []

                for function in option['callables']:
                    try:
                        callable_name = function.func_name #Only works for functions, unless specified attribute of a class
                    except AttributeError:
                        callable_name = str(function) #This will probably happen to classes
                    callables.append(callable_name)
                    #callables.append(str(function))
                    #line += '{callable_name}'.format(callable_name=callable_name)

                line +=  '\tCallables: ' +Fore.CYAN + str(callables)+ Fore.RESET 

            if option['display_regex'] or self.display_all_regex:
                #option['patterns'].append(option['display_name'])
                line += '\tPatterns: ' + Fore.CYAN + str(option['patterns']) + Fore.RESET
            line += "\n"

        return line

    def __call__(self,callables): #callables is a list of callables. Who would've guessed?
        buff = '-'*72
        for function in callables:
            try:
                callable_name = function.func_name #Only works for functions
            except AttributeError:
                callable_name = str(function) #This will probably happen to classes
            if callable(function):
                print buff
                print Fore.GREEN + "\tEXECUTING '%s'...\n" % callable_name + Fore.RESET
                function()
                print buff

    def __chexit__(self,user_input,exit=False):
            
            for pattern in self.exit_words:#checking for exit words
                match = re.search(pattern,user_input)
                if match or exit:
                    self.condition=False
                    #to break it
                    self.__call__(self.exit_callables)
                    if self.exit_message:
                        print Fore.RED + Style.BRIGHT + self.exit_message + Fore.RESET + Style.RESET_ALL


    def __clear__(self):
        if platform == 'win32':
            command = 'cls'
        if platform == 'linux2' or platform == 'darwin':
            command = 'clear'
            
        subprocess.call(command)

    def add(self,**kwargs):
        """This method adds menu options to the menu.
        
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
   This toggles the display of the list of regex strings that correspond to each menu option.
        """
        callables = kwargs.pop('callables',None)
        patterns = kwargs.pop('patterns',None)
        display_name = kwargs.pop('display_name',None)
        display_callables = kwargs.pop('display_callables',False)
        display_regex = kwargs.pop('display_regex',False)

        try:
            backup_name = callables[0].func_name #The name of the first function defined in the list of callables.
        except AttributeError:
            backup_name = str(callables[0])

        if not display_name:
            display_name = backup_name

        if not patterns:
            patterns = ['^'+backup_name+'$']

        if self.start_with_zero:
            offset = 0

        if not self.start_with_zero:
            offset = 1
            
        index = len(self.menu)+offset # +1 to start menu with zero
        patterns.append('^'+str(index)+'$') # To make it regex-y


        option = {'callables':callables,
        'display_name':display_name,
        'patterns':patterns,
        'display_callables':display_callables,
        'display_regex':display_regex,
        'index':index}

        self.menu.append(option)

    def execute(self): #Playing with the idea of uesr defined while loop conditions, and callable tests for said conditions
        """Mainloop of the :term:`clui`. 
        
Only hit this after you have added all of the options for your menu.
It will enter a loop, and it will break in only three scenarios:

1) The user's input matches one of the :ref:`exit words <customization>` patterns. 

2) One of the user defined :ref:`condition tests <customization>` returns False

3) The user exists the terminal/shell

"""
        width = 70

        if self.title:
            #print Back.WHITE + Fore.BLACK + self.title.center(width) + Back.RESET+Fore.RESET #Title in white bg with black text
            print Style.BRIGHT + self.title.center(width) + Style.RESET_ALL #Bright text for the title!
            print '='*72+"\n"

        if self.initial_message:

            print Fore.YELLOW + self.initial_message.center(width) + Fore.RESET
            print ''

        if self.display_exit_words:
            print "Enter one of the following words to escape: " + Fore.RED + str(self.exit_words) + Fore.RESET
            print ''
            
        for option in self.menu:
            display_name = option['display_name']
            option['patterns'].append('^'+display_name+'$')

        while self.condition:
            self.looped += 1

            #print '*'*72+"\n"
            print self.__menu__() #gen menu as string
            user_input = raw_input(self.input_message)

            if (user_input == 'clear' or user_input == 'cls') and self.enable_clear:
                self.__clear__() #makes os call to clear the screen

                
            if self.condition_tests: #user defined tests
                for condition_test in self.condition_tests:
                    self.condition = condition_test(user_input,self.looped)
                    if not self.condition:
                        print Fore.RED + Style.BRIGHT + self.exit_message + Fore.RESET + Style.RESET_ALL #FIXME: This is copy and paste from the __chexit__ method.
                                                                                                         #For some reason this was double printing when I ran chexit

            print '' #Buffer line
            


            for option in self.menu: #checking menu option patterns
                for pattern in option['patterns']:
                    match = re.search(pattern,user_input)

                    if match:
                        self.__call__(option['callables'])
            
            self.__chexit__(user_input) #Check for exit words

deinit() #required for x-platform support by colorama

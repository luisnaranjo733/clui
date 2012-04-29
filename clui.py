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

init()

TODO = """
Resolve dependency issues - what to do if colorama is unavailable?
UPDATE DOCUMENTATION
    Minimalistic "Hello, World clui?" (3-4 lines)
function.func_name for classes?
figure out what the correct way of adding images to readthedocs is!
exit_callable attribute and functionality! DOCS
exit_words regex matching DOCS

"""

class base_clui(object):
    """
    This is the base class for a command line user interface.
    You can control the style of the interface with the attributes
    provided in this class. *All attributes are optional*.

    Kwargs:

      title (str): The title of your clui

      initial_message (str):  Use this for any additional information you want to display (usage, author, license, version, homepage, etc...)

      exit_words (list): A list of regex strings. It matches the user's input to these and exits the programs if it finds a match.
        The **defaults** are ['^end$','^exit$','^leave$','^bye'$]

      exit_message (str): This is the message that clui displays when the user exits the interface.

      start_with_zero (bool): This controls the index values of the 

    """

    def __init__(self,**kwargs):
        """The menu attribute is key here. All the 'add' method really does
        is add dictionaries to the options method, which are used to
        generate the clui."""

        self.title = kwargs.pop('title', None)
        self.initial_message = kwargs.pop('initial_message', None)
        self.exit_words = kwargs.pop('exit_words', 'end exit leave bye'.split())
        self.exit_message = kwargs.pop('exit_message', None)
        self.start_with_zero = kwargs.pop('start_with_zero',False)
        self.display_all_callables = kwargs.pop('display_all_callables',False)
        self.display_all_regex = kwargs.pop('display_all_regex',False)
        self.display_exit_words = kwargs.pop('display_exit_words',True)
        self.menu = [] #List of options for the clui to use
        self.looped = 0 #Gets a +1 for each loop. In case tracking the amount of loops is ever important.

    def __menu__(self):

        line = ''

        for option in self.menu:
            colored = Fore.MAGENTA + option['display_name'] + Fore.RESET
            line += "{index}: {display_name}".format(index=option['index'],display_name=colored)

            if option['display_callables'] or self.display_all_callables:
                #line += '\n\t' + ','.join([function.func_name for function in option['callables']])

                callables = []

                for function in option['callables']:
                    try:
                        callable_name = function.func_name #Only works for functions
                    except AttributeError:
                        callable_name = str(function) #This will probably happen to classes
                    #callables.append(callable_name)
                    callables.append(str(function))
                    #line += '{callable_name}'.format(callable_name=callable_name)

                line +=  '\tCallables: ' +Fore.CYAN + str(callables)+ Fore.RESET 

            if option['display_regex'] or self.display_all_regex:
                line += '\tPatterns: ' + Fore.CYAN + str(option['patterns']) + Fore.RESET
            line += "\n"

        return line

    def __patterns__(self):

        for option in self.menu:
            patterns = option['patterns']#.append(self.menu.index(option)) #Deprecated? Moved this into the initial add method.
            callables = option['callables']
            yield(patterns,callables)

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

    def add(self,callables,patterns=None,display_name=None,synopsis=None,display_callables=False,display_regex=False):
        """
        This method adds commands to the self.menu list, which is used to gen
        erate the clui.

        It has the following parameters:

        callables (positional)
            This is a **list** of callable functions/classes that clui will execute
            for that menu option (in the order that they were defined).
            **These callables *will not* take any positional parameters**.

        patterns (defaults to the name of the first callable)
            A **list** of regex strings that clui will use to match to user input (in order).
            If a match is found, the corresponding callable will executed.

        display_name (defaults to the name of the first callable)
            This is the **string** that will actually be displayed to the user for
            this option in the menu.

        synopsis (defaults to None)
            This is a brief summation of what each command does, it is shown to
            the right of its' corresponding command.

        display_callables (defaults to False)
            This boolean defines controls whether or not an additional list of callables is
            added for *each* menu option.
        """
        

        try:
            backup_name = callables[0].func_name #The name of the first function defined in the list of callables.
        except AttributeError:
            backup_name = str(callables[0])

        if not display_name:
            display_name = backup_name

        if not patterns:
            patterns = [backup_name]

        if self.start_with_zero:
            offset = 0

        if not self.start_with_zero:
            offset = 1

        patterns.append(str(len(self.menu)+offset)) # +1 to start menu with zero
        index = len(self.menu)+offset # +1 to start menu with zero

        option = {'callables':callables,
        'display_name':display_name,
        'patterns':patterns,
        'synopsis':synopsis,
        'display_callables':display_callables,
        'display_regex':display_regex,
        'index':index}

        self.menu.append(option)

    def execute(self): #Playing with the idea of uesr defined while loop conditions, and callable tests for said conditions
        """
        This is the mainloop of the clui. Only hit this after you have added all
        of the options for your menu, because it will enter a loop, and it won't exit
        until the user's input is in the exit_words list (defined in __init__).
        """
        condition = True
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

        while condition:
            #print Back.BLACK #Optional?
            print '*'*72+"\n"
            print self.__menu__()
            user_input = raw_input("> ")

            print '' #Buffer line
            
            for patterns,callables in self.__patterns__():
                for pattern in patterns:
                    #print "Trying: ",pattern
                    match = re.search(pattern,user_input)

                    if match:
                        buff = '='*72
                        #print buff
                        self.__call__(callables)
                        #print buff+'\n'
            self.looped += 1

            if user_input in self.exit_words: #Breaks the loop if the keywords are met
                condition=False
                if self.exit_message:
                    print Fore.RED + Style.BRIGHT + self.exit_message + Fore.RESET + Style.RESET_ALL
                #print Back.RESET #Optional?

deinit()
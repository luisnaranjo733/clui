CLUI - Command Line User Interface
**********************************

.. toctree::
   :maxdepth: 2

**An open source python object-ooriented API for creating command line user interfaces on the fly.**
   Created by *Luis Naranjo*

Installation
============

As *always*, you should use to pip to install.

>>> pip install clui

Usage
=====

.. automodule:: clui
   :platform: Linux, Mac, Windows
   :synopsis: An open source python object-ooriented API for creating command line user interfaces on the fly.

.. autoclass:: base_clui
   :members:



Example Code
============

>>> from clui import base_clui
>>> 
>>> def add_flashcards():
...     print "Adding some flashcards..."
...     print "All done!"
... 
>>> def delete_flashcards():
...     print "Deleting all of the flashcards..."
...     print "Done!"
... 
>>> class will_not_be_named(object):
...     def __init__(self):
...         print "This function will not be the name of added menu option, because it was not added first."
... 
>>> ui = base_clui(
...     title = 'Flashcards',
...     initial_message = 'Flashcards is a python utility designed to help you know your stuff!',
...     exit_message = 'Bye! I hope you enjoyed your stay.',
... )
>>> ui.exit_words.append('idgaf')
>>> ui.add(
...     callables=[delete_flashcards,will_not_be_named],
...     patterns=[
...         '[Rr]emove flashcards',
...         '[Dd]elete flashcards!?'
...     ],
...     #display_callables = True,
... ) 
>>> 
>>> ui.add(
...     callables=[add_flashcards],
...     patterns=['[Aa]dd flashcards','add'],
...     display_name='Add some flashcards!',
...     #display_callables = True,
... )
>>> 

Example Output
===============

This is what the CLUI might look like!

.. image:: sample_output.png

Dependencies
============

`colorama`_

.. _colorama: http://pypi.python.org/pypi/colorama

Indices and tables
*******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


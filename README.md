ezpy
====
Design Document: https://docs.google.com/document/d/1fG_cwTUzZ71FXs4oJEjvDGy868W8BRb8Yjc150ecHVI/edit?usp=sharing

PA6 Report: https://docs.google.com/document/d/1fxfKOydkB5lANoOoOyih5CQJ7_eh-0HeKO9XRAe4myc/edit?usp=sharing

PA6 Proposal: https://docs.google.com/document/d/10O4aIrVzdiIUdnejtldlfw71U4Gx-dGPmrCxm_sZjpM/edit

Demo Presentation Slides: https://docs.google.com/presentation/d/1_TUsPb0kEYmxy632u0_vCaETlqGcC1sZBmw_gUDlmz0/edit#slide=id.p

Final Demo: http://youtu.be/Rq5Vgb4h6No

====

Tutorial:

*Reference https://docs.python.org/2/c-api/arg.html for format strings to convert Python-C data types.

Configuration File

You can use a configuration file to define the interface between your importable module in C and Python. Remember that you can define multiple functions for each module.

First name the module. As an example, we will create a module named “foo”.
The syntax is as follows:
name:foo

Then define a new function. We want a function called add_three that takes in three integers as arguments and returns the sum of the three arguments. In Python we want to call it like: add_three(34,6,1), which would return 41.

The syntax is as follows:
function:foo (to name the function)
For each argument and its respective data type, refer to the included “Format String Documentation”. The most commonly used primitive data types such as integer, double, and float are highlighted. The integer data type corresponds to the “i” format string. 
Use the syntax “format string”:”argument name” to define every argument, data type pair.
In our case for variable names arg1, arg2, and arg3, it would look like:

i:arg1
i:arg2
i:arg3

Finally, we can define a return type. This is strictly optional. Your custom C function will return Python’s None value by default if the return statement is absent.

Once again, the return statement also uses the previously used format string to define the data type of the returned value. Refer to the included format string documentation for return statements.

Use the syntax:
return:”format string”
In our case, we want to return an integer as the sum of the three arguments, which results in:
return:i

In summary, the configuration file would look like:

name:foo

function:add_three
i:arg1
i:arg2
i:arg3
return:i

Save to disk, and run “ezpy generate *your_config_file*” to generate the boilerplate C code and the Python setup script that will install the module on your system. Run the setup script by running “sudo python *your_new_module*_setup.py install”.

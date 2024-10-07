"""

5.
Understand Python’s scope rules and how they affect variable lookup and access in different contexts.
Task:
Explain the LEGB rule: Local, Enclosing, Global, Built-in.
Describe what happens to a variable when it is defined:
Inside a function (local)
Inside a function within another function (enclosing)
In the main body of the program (global)
As a built-in function (built-in)

------
ANSWER:

Local - refers to variables that are defined inside a function. Inside a function, Python first checks for local scope.
Enclosing - refers to variables defined in a nested function's outer function, where the inner function can access variables from the outer function.
Global - refers to variables defined at the top level of a script or module. Global variables can be accessed from anywhere in the module
Built-In - refers to the built-in functions and variables provided by Python

The LEGB rule dictates the order in which Python searches for variable names when resolving a reference, and the order is as follows:

Local (L) — Python first looks in the local scope (the innermost function).
Enclosing (E) — If not found locally, Python checks the enclosing scope (the outer function in case of nested functions).
Global (G) — If the variable isn’t found in the local or enclosing scopes, Python looks in the global scope (top-level of the module).
Built-in (B) — If the variable isn’t found in the previous three scopes, Python checks the built-in scope, which contains Python’s built-in functions and variables.
------

Example:
Imagine you have a variable called x that exists in the global scope and is also redefined inside a function.
Explain how Python resolves which value of x to use at different points in the
 program.

"""

x = 1

def new_scope():
    x = 5
    print('x in the function is equal to ',x) # checks local scope first

new_scope() # calls local scope of function first, so x will be 5
print('x in global is equal to ',x) # calls global scope here, not referencing the function scope so x will be 1


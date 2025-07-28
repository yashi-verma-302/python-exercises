What is Scope in Python?
Scope refers to the region of code where a variable is recognized or can be accessed.

When you create a variable, where you define it determines who can see or use it.

--> Types of Scope (LEGB Rule)
Python follows the LEGB rule to look up variables:

Scope Type	Description	Example
L - Local	Inside a function or block	Function variables
E - Enclosing	In enclosing (outer) functions for nested functions	Nested function scope
G - Global	At the top level of a module (outside all functions)	Global variables
B - Built-in	Python’s built-in names (like print(), len(), etc.)	Built-in scope

Any outside variable can refer to outside only it cannot refer to inside variable. 
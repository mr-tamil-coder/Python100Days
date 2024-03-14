'''
DAY 1
#printing,commenting,debugging,String manipulation and variables
project: Band Name Generator
'''

#printing
print("hello world ")

"""
inside the print its can be single or double quotes

Eg error :
    print("Hello world ) #syntax error EQL while scanning string literal {u can refer stack overflow to find the solution}
    This error message usually suggests that there's a missing comma, parenthesis, or quotation mark somewhere in your code
    
"""

#String Manipulation
print("Helo" + " " + "Vinoth")
print(f"Hi Mohanraj I know")
text="Myself vinoth and find name of my friend is Mohan raj yeah! absolutely"
print(text[0:2] + " "+text[23:27] + " " +text[41:43] + " " +text[44:53] + " " +text[54:59])

#Debugging
print("Day 1 - String Manipulation")
print("String Concatenation is done with the \"+\" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#input Functions - used to get input from the user
print("helo Mr." + input("Enter the Name"))
print("Ended print function")

#program to swap the two numbers
a=input("Enter 1st value")
b=input("Enter 2nd value")
c=a
a=b
b=c
print(f"the value of a is {a} and the value of b is {b}")
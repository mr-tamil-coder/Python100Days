'''
print(827_34.34)
#data type

string,integer,float,boolean

#see the data type type()

num=type(len(input("what is ur name")))
print(num) #<class 'int'>

#type conversion  - str(),int(),float()
a=str(123)
print(type(a))
print(type(float(a)))

#mathematical operations => 6/3 returns float eventhough both are integers

Orders -PEMDAS (priority of operator)
P - parantheses -()
E - Exponents - **
M - Multiplication,D -Divison
A - Addition,S - Subtraction

left to right

print(3*3+3/3-3)

'''
#BMI WEIGHT
'''
formula = weight/height**2

def calculate_bmi(bmi):
    if bmi <18.5:
        return "Underweight"
    elif bmi >18.5 and bmi < 25:
        return "Normal weight "
    elif bmi>25 and bmi <30:
        return "Overweight"
    else:
        return "obese"
weight=float(input("Enter the weight "))
height=float(input("Enter the height "))
bmi=weight/height**2
print(bmi)
print(calculate_bmi(bmi))
'''
#calculate the weeks
age=90-int(input("Enter ur age"))
print(f"u have {age*52.14} weeks to die lol")

#error - unable to concatenate the int to str
# print("Your deade age is "+age)
"""
but u can use fstring to concatenate the int to str
"""
print(f"Your deade age is {age}")

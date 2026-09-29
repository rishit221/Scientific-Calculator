from math import *
def change_values():
    numbers=[]
    n= int(input("Enter the amount of numbers you want to operate on"))
    for i in range (1,n+1):
        numbers.append(float(input(f"Enter your number {i}:")))
    return numbers    
def addition (numbers):
    a=0
    for i in numbers:
        a+=i
    return a
def subtract(numbers):
    a=numbers[0]
    for i in numbers[1:]:
        a-=i
    return a
def multiplication(numbers):
    a = 1
    for i in numbers:
        a*=i
    return a
def division(numbers):
    return numbers[0]/numbers[1]
def floor_division(numbers):
    return numbers[0]//numbers[1]
def remainder(numbers):
    return numbers[0]%numbers[1]
def square_root(numbers):
    for i in numbers:
        return sqrt(i)
def base_e_log(numbers):
    for i in numbers:
        return log(i)
def custom_base_log(numbers,n):
    for i in numbers:
        return log(i,n)
def fact(numbers):
    for i in numbers:
        x = int(i)
        return factorial(x)
def hcf(numbers):
    number=[]
    for i in numbers:
        a = int(i)
        number.append(a)
    return gcd(*number)
def exponential(numbers):
    for i in numbers:
        return exp(i)
def sine(numbers):
    for i in numbers:
        i=radians(i)
        return sin(i)
def cosine(numbers):
    for i in numbers:
        i=radians(i)
        return cos(i)
def tangent(numbers):
    for i in numbers:
        i=radians(i)
        return tan(i)

def secant(numbers):
    for i in numbers:
        i=radians(i)
        return 1/cos(i)
def cosecant(numbers):
    for i in numbers:
        i=radians(i)
        return 1/sin(i)
def cotangent(numbers):
    for i in numbers:
        i=radians(i)
        return 1/tan(i)
def arcsine(numbers): 
    for i in numbers:
        c=asin(i)
        return degrees(c)
def arccosine(numbers):
    for i in numbers:
        c=acos(i)
        return degrees(c)
def arctan(numbers):
    for i in numbers:
        c=atan(i)
        return degrees(c)
print("Hello User")
print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for Division")
print("Enter 5 for floor division of two numbers only")
print("Enter 6 to get remainder of two numbers only")
print("Enter 7 to get square root of one number only")
print("Enter 8 to get natural logarithm of one number only")
print("Enter 9 to get Logarithm of only one number with any custom base(Enter only one number initially)")
print("Enter 10 to get factorial of one positive integer only")
print("Enter 11 to get Greatest Common Divisor or Highest Common Factor")
print("Enter 12 to get any one power of exponential function")
print("Enter 13 to get the value of sine function with angle in degrees (not radians)")
print("Enter 14 to get the value of cosine function with angle in degrees(not radians)")
print("Enter 15 to get the value of Tangent function with angle in degrees(not radians)")
print("Enter 16 to get the value of cosecant function with angle in degrees(not radians)")
print("Enter 17 to get the value of secant function with angle in degrees(not radians)")
print("Enter 18 to get the value of cotangent function with angle in degrees(not radians)")
print("Enter 19 to get the value of inverse of sine function of only one value in degrees only")
print("Enter 20 to get the value of inverse of cosine function of only one value in degrees only")
print("Enter 21 to get the value of inverse of tangent function of only one value in degrees only")
print("Enter 22 to change the values you want to operate on")
print("Enter 0 to exit")    
c=change_values()
while True:
    n=int(input("Enter the number of operation you want to operate on(Ex:- 1 for addition)"))
    if n==1:
        print("The addition of the list of numbers", c, "is", addition(c))
    elif n==2:
        print("The subtraction of the list of numbers", c, "is", subtract(c))
    elif n==3:
        print("The multiplication of the list of numbers", c, "is", multiplication(c))
    elif n==4:
        if len(c)!=2:
            print("The division of more than or less than 2 is not possible")
        elif c[1]==0:
            print("Division by zero is not possible")
        else:
            print("The division of the two numbers", c[0],"and", c[1], "is", division(c))
    elif n==5:
        if len(c)!=2:
            print("The floor division of more than or less than 2 is not possible")
        else:
            print("The Floor division of the two numbers", c[0], "and", c[1], "is", floor_division(c))
    elif n==6:
        if len(c)!=2:
            print("The Remainder of more than or less than 2 is not possible")
        else:
            print("The Remainder after the dividing the two numbers", c[0], "and", c[1], "is", remainder(c))
    elif n==7:
        if len(c)!=1:
            print("The square root for more than one number is not possible")
        elif c[0]<0:
            print("Square root of a negative number is not possible")
        else:
            print("The Square root of the number", c[0], "is", square_root(c))
    elif n==8:
        if len(c)!=1:
            print("The logarithm of more than one numbers is not possible")
        elif c[0]<=0:
            print("The natural log of negative numbers is not possible")
        else:
            print("The natural Logarithm of the number", c[0], "is", base_e_log(c))
    elif n==9:
        if len(c)!=1:
            print("The logarithm of more than one number is not possible")
        elif c[0]<=0:
            print("The logarithm of negative number is not possible")
        else:
            n=int(input("Enter the base you want to find log with"))
            if n<=0 or n==1:
                print("Base cannot be negative or 1")
            else:
                print("The logarithm of number", c[0],"with base", n,"is", custom_base_log(c,n))
    elif n==10:
        if len(c)!=1:
            print("The factorial of more than one numbers is not possible")
        elif c[0]<0:
            print("The factorial of negative numbers is not possible")
        else:
            print(fact(c))
    elif n==11:
        print("The HCF of the list of numbers", c, "is", hcf(c))
    elif n==12:
        if len(c)!=1:
            print("The power of exponential is not possible for more than one number")
        else:
            print("The value of power of exponential is:", exponential(c))
    elif n==13:
        if len(c)!=1:
            print("The value of angle cannot be more than one numbers")
        else:
            print("The sine of",c[0],"degrees is", sine(c))
    elif n==14:
        if len(c)!=1:
            print("The value of angle cannot be more than one numbers")
        else:
            print("The cosine of",c[0],"degrees is", cosine(c))
    elif n==15:
        if len(c)!=1:
            print("The value of angle cannot be more than one numbers")
        elif c[0]==90:
            print("the value of Tan 90 is not defined") 
        else:
            print("The tangent of",c[0],"degrees is", tangent(c))
    elif n==16:
        if len(c)!=1:
            print("The value of angle cannot be more than one numbers")
        elif c[0]==0:
            print("Cosecant of 0 is not defined")
        else:
            print("The cosecant of",c[0],"degrees is", cosecant(c))
    elif n==17:
        if len(c)!=1:
            print("The value of angle cannot be more than one numbers")
        else:
            print("The secant of",c[0],"degrees is", secant(c))
    elif n==18:
        if len(c)!=1:
            print("The value of angle cannot be more than one numbers")
        elif c[0]==0:
            print("The value of cot 0 is not defined")
            
        else:
            print("The cot of",c[0],"degrees is", cotangent(c))
    elif n==19:
        if len(c)!=1:
            print("The value cannot be more than one numbers")
        elif c[0]>=-1 and c[0]<=1:
            print("The inverse of sine of",c[0],"is", arcsine(c))
        else:
            print("The value cannot be less than -1 or more than 1")
    elif n==20:
         if len(c)!=1:
            print("The value cannot be more than one numbers")
         elif c[0]>=-1 and c[0]<=1:
            print("The inverse of cosine of",c[0],"is", arccosine(c))
         else:
            print("The value cannot be less than -1 or more than 1")
    elif n==21:
        if len(c)!=1:
            print("The value cannot be more than one numbers")
        else:
            print("The inverse of Tan of",c[0],"is", arctan(c))
    elif n==22:
        c=change_values()
    elif n==0:
        break
    else:
        print("Invalid Input")
print("Thank You")

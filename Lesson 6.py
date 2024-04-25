#FUNCTIONS
'''x=int(input("Enter an Integer : "))

import math
print(math.sin(x))
print(math.cos(x))
print(math.tan(math.pi/2))
print(math.e)
print(math.sqrt(2))'''

#FACTORIAL PROBLEM
def fact(n):
    '''The below program is related to "FUNCTIONS". A sum of factorial is used to understand the use of functions in PYTHON.
    This program is created during a course conducted by our college called "Nuts and Bolts Python Programming on 25th April 2024.'''

    '''p=1
    for i in range(1,n+1):
        p=p*i
    return(p)

n=int(input("Enter the value of n : "))
r=int(input("Enter the value of r : "))
print("The nCr =",fact(n)//(fact(r)*fact(n-r)))'''

#FUNCTION WITHOUT PARAMETER AND RETURN VALUE
def f_without_para_return():
    '''The following program is based on the concept of the functions without parameter and return value.'''

    '''print("Welcome to the world of Programming.")
f_without_para_return()'''

#FUNCTION WITHOUT PARAMETER BUT WITH RETURN VALUE.
#FOR 99
def fixed_prime_check():
    '''The below program is based on the concept of the functions without parameter but with return value.'''
    '''isprime=True
    for i in range(2,int(99*(0.5)+1)):
        if (99%i==0):
            isprime=False
            break
    return isprime

if(fixed_prime_check()==True):
    print("99 is a prime number.")
else:
    print("99 is a composite number.")'''

#FOR N-value
def fixed_prime_check(n):
    '''The below program is based on the concept of the functions without parameter but with return value.'''
    '''isprime=True
    for i in range(2,int(n*(0.5)+1)):
        if (n%i==0):
            isprime=False
            break
    return isprime
n=int(input("Enter an Integer : "))
if(fixed_prime_check(n)==True):
    print(n,"is a prime number.")
else:
    print(n,"is a composite number.")'''

#FUNCTION WITH TWO PARAMETERS AND WITHOUT RETURN
def printinfo(name,age=20):
    '''The below program is based on the concept of the functions with two parameters and without return value.'''
    '''print("Name is : ",name)
    print("Age is : ",age)
name=input("Enter your name : ")
age=int(input("Enter your age : "))
printinfo(name)
printinfo(name,age)'''

#FUNCTION WITH MORE THAN ONE RETURN VALUE
'''s1=int(input("Enter the marks of Mathematics : "))
s2=int(input("Enter the marks of Statistics : "))
s3=int(input("Enter the marks of Economics : "))

def result(s1,s2,s3):
    return s1+s2+s3,s1+s2+s3/3
total,average=result(s1,s2,s3)
print("Total Marks : ",total,"& Average Marks : ",average)'''

#FUNCTION RETURNING LIST VALUE
'''k=input("Enter a string : ")
def returnlist(str):
    return list(str)
print("The list value : ",returnlist(k))'''

#VARIABLE-LENGTH ARGUMENTS
'''def printinfo(arg1,*vartuple):
    print("Result : ")
    print(arg1)
    for var in vartuple:
        print(var)
    return'''

#LAMBDA FUNCTION
square=lambda x: x*x
print(square(5))

oddeven= lambda x: "Even" if(x%2==0) else "Odd"
print(oddeven(99))

minimum= lambda x,z: x if x<z else z
print("Minimum :",minimum(97,54))

prime= lambda x: "Composite number." if(x%2==0) else "Prime number."
print(prime(1234567891234567891234567))

lis= [1,2,3,4,5,6]
mapped = map(lambda x: x*x,lis)
for k in mapped:
    print(k,end = " ")


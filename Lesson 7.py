#RECURSIVE FUNCTION
#FACTORIAL
def fact(n):
    '''The following function shows the recursive nature of the function.'''
'''if(n==1): return (n)
    else:
        return(n*fact(n-1))
n=int(input("Enter an Integer : "))
print("The factorial value of",n,"=",fact(n))'''

#FIBONACCI
def fibona(n):
    '''The following function shows the recursive nature of the function.'''
    '''if(n<=1):
        return (n)
    else:
        return(fibona(n-1)+fibona(n-2))
n=int(input("Enter an Integer : "))
print("The fibonacci value of",n,"=",fibona(n))'''

#GREATEST COMMON DIVISOR
def gcd(a,b):
    '''The following function shows the recursive nature of the function.'''
    r=a%b
    while(r>0):
        a=b
        b=r
        r=a%b
    return(b)
a=int(input("Enter the value of dividend : "))
b=int(input("Enter the value of divisor : "))
print("Remainder of dividend",a,"and divisor",b,"=",gcd(a,b))

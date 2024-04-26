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
    if(n<=1):
        return (n)
    else:
        return(fibona(n-1)+fibona(n-2))
n=int(input("Enter an Integer : "))
print("The fibonacci value of",n,"=",fibona(n))

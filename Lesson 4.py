#WHILE AND FOR LOOPS

#FOR
'''n=int(input("Enter an Integer: "))
for i in range(1,n+1,1):
    print(i)'''

#Q1.Print all natural numbers from 1 to n.
'''n=int(input("Enter an Integer: "))
i=1
while(i<=n):
    print(i,end=' ')
    i=i+1'''
    
#Q2.Print all elements of a list using for loop.
'''list1=[1,2,3,4,5,6,'a','b','c','d']
for i in list1:
    print(i,end=' ')'''

#Q3.Print all natural numbers in reverse(from n to 1), using while loop.
'''n=int(input("Enter an Integer: "))
i=n
while(i>=1):
    print(i,end=' ')
    i=i-1'''

#Q4.Print all alphabets from A to Z, using while loop.
#FOR
'''for i in range(65,91,1):
    print(chr(i),end=" ")'''
#WHILE
'''i=65
while(i<=91):
    print(chr(i),end=" ")
    i=i+1'''

#Q5.Print all even numbers between 1 to 100, using while loop.
'''i=2
while(i<=101):
    print(i,end=" ")
    i=i+2
for i in range(2,101,2):
    print(i,end=" ")'''

#Q6.Print all odd numbers between 1 to 100.
#FOR
'''for i in range(1,101,2):
    print(i,end=" ")'''
#WHILE
'''i=1
while(i<=100):
    print(i)
    i=i+2'''

#Q7.Find sum of all natural numbers between 1 to n.
#FOR
'''sum=0
n=int(input("Enter an Integer: "))
for i in range(n+1):
    sum=sum+i
print(sum)'''
#WHILE
'''n=int(input("Enter an Integer: "))
sum=0
i=1
while(i<=n):
    sum=sum+i
    i=i+1
print("Sum of",n,"=",sum)'''

#Q8.Find sum of all even numbers between 1 to n.
#FOR
'''sum=0
n=int(input("Enter an Integer: "))
for i in range(0,n+1,2):
    sum=sum+i
print("Sum of all even numbers from 1 to",n,"=",sum)'''

#WHILE
'''n=int(input("Enter an Integer: "))
sum=0
i=2
while(i<=n):
    sum=sum+i
    i=i+2
print("Sum of all even numbers from 1 to",n,"=",sum)'''

#Q9.Find sum of all odd numbers between 1 to n.
#FOR
'''sum=0
n=int(input("Enter an Integer: "))
for i in range(1,n+1,2):
    sum=sum+i
print("Sum of all odd numbers from 1 to",n,"=",sum)'''

#WHILE
'''n=int(input("Enter an Integer: "))
sum=0
i=1
while(i<=n):
    sum=sum+i
    i=i+2
print("Sum of all odd numbers from 1 to",n,"=",sum)'''

#Q10.Print multiplication table of any number.
#FOR
'''mul=1
n=int(input("Enter a number: "))
for i in range(1,11):
    print(n,"*",i,"=",n*i)'''

#Q11.Count number of digits in a number.
'''n=int(input("Enter an Integer: "))
i=0
while(n>0):
    r=n%10
    n=n//10
    i=i+1
print(i)'''

#Q12.Find first and last digits of a number.
'''n=int(input("Enter an Integer: "))
k=n
digit=[]
i=0
while(n>0):
    r=n%10
    n=n//10
    digit.append(r)
print("Length of",k,"=",len(digit))
print(digit)
print("First digit of",k,"=",digit[-1])
print("Last digit of",k,"=",digit[0])'''

#Q13.Find sum of first and last digit of a number.
'''n=int(input("Enter an Integer: "))
k=n
digit=[]
i=0
while(n>0):
    r=n%10
    n=n//10
    digit.append(r)
print("The sum of first and last digit of",k,"=",digit[0]+digit[-1])'''

#Q14.Swap first and last digits of a number.
n=int(input("Enter an Integer: "))
k=n
digit=[]
i=0
while(n>0):
    r=n%10
    n=n//10
    digit.append(r)
    digit[0]=digit[0]
    digit[-1]=digit[-1]
first=digit[0]
last=digit[-1]
middle=digit[1:-1]
swap=first+
print("After swapping the first and last digits of",k,"we get",last+middle+first)


    

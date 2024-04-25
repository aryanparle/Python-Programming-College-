#BREAK statement
#Without if else.
'''n=int(input("Enter the number of times to divide : "))
for i in range(1,n+1):
    div=int(input("Dividend = "))
    dis=int(input("Divisor = "))
    print("Quotient = ",div//dis,"Remainder = ",div%dis)'''

#With if else.
'''n=int(input("Enter the number of times to divide : "))
for i in range(1,n+1):
    div=int(input("Dividend = "))
    dis=int(input("Divisor = "))
    if dis==0:
        print("Divisor cannot  be zero.")
        break
    else:
        print("Quotient = ",div//dis,"Remainder = ",div%dis)'''

#CONTINUE statement
'''n=int(input("Enter the number of times to divide : "))
for i in range(1,n+1):
    div=int(input("Dividend = "))
    dis=int(input("Divisor = "))
    if dis==0:
        print("Divisor cannot  be zero.")
        continue    
    else:
        print("Quotient = ",div//dis,"Remainder = ",div%dis)'''

#PRIME NUMBERS
'''isprime=True
n=int(input("Enter an Integer : "))
for i in range(2,int(n**0.5)+1):
    if(n%i==0):
        isprime=False
        break
if(isprime==True):
    print(n,"is a prime number!")
else:
    print(n,"is not a prime number!")'''

#SORTING & NESTED LOOPS
'''num=[]
n=int(input("Number of integers to enter : "))
for i in range(n):
    k=int(input("Enter the Integers : "))
    num.append(k)
print("Original List : ",num)
for i in range(n):
    for j in range(i+1,n):
          if(num[i]>num[j]):
            k=num[i]
            num[i]=num[j]
            num[j]=k
print("Sorted List : ",num)'''

#NESTED LOOPS
'''n=int(input("Number of lines to print: "))
for i in range(n+1):
    for j in range(i):
        print('*',end=" ")
    print("\n")'''

#REVERSE NESTED LOOPS
n=int(input("Number of lines to print: "))
for i in range(n+1):
    for j in range(i,n+1):
        print('*',end=" ")
    print("\n")













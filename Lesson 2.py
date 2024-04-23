#ASSIGNMENT 1
First="Aryan "
Middle="Deepak "
Last="Parle"
Age="19"
Full_name=First+Middle+Last
print(Full_name)
print(Full_name.upper())
print(First*3)
print(Middle.count("e"))
print(Full_name[7])
print(First[0],Middle[0],Last[0])
print(Full_name[1:8])
print()

#ASSIGNMENT 2
import math
p=10000
n=10
r=8
simple_interest=(p*n*r)/100
print("Simple Interest =",simple_interest)
print()

Final_amt=p*pow((1+r/100),n)
print("Final Amount =",Final_amt)
compound_interest=Final_amt-p
print("Compound Interest =",compound_interest)
print()

#ASSIGNMENT 3
x="He is"
y="telling the truth."
z="telling lie."
print('1. ',x,y)
print('2. ',x,z)
print(y*3)
print(x[0:2],y[0:2],z[0:2])
print(y[0:13:2])
print()

#ASSIGNMENT 4
slogan="We are Khalsite."
print(slogan.lower())
print(slogan.upper())
print(slogan.find('r'))
print(slogan.replace("We","You"))
print(slogan.count("e"))
print(len(slogan))
print(slogan[0:16:2])
print()

#ASSIGNMENT 5 (LISTS)
L1=[1,2,3,4,5,6,7,8]
L2=["Aman","Rohan","Shubham","Sanket","Pranv","Amit"]
L3=L1+L2
print(L3)
L3[2]=9
print(L3)
sublist=L3[3:6]
print(sublist)

list11=[10,2,1,10,4,5]
print(max(list11))
print(min(list11))
print(len(list11))
print(list11.count(10))

list11.extend([7,8])
print(list11)

del list11[0:2]
print(list11)
print()

#ASSIGNMENT 6 (TUPLES)
tup1=(1,2,3,4)
tup2=('a','b','c')
tup3=tup1+tup2
print(tup3)
print(tup1*3)
print(max(tup1))
print(min(tup1))
print(len(tup1+tup2))
print(tup1.count(3))
print()

#ASSIGNMENT 7 (DICTIONARY)
dict1={1:'one',2:'two',3:'three'}
print(dict1.keys())
print(dict1.values())
print()

maths_dept={'calculus':"Mrs. Lata Mohan",'algebra':"Mrs. Dipali Sawant",'differential_equations':"Dr. Rakesh Barai"}
print(maths_dept.keys())
print(maths_dept.values())
print(maths_dept['calculus'])

maths_dept['calculus 2']='Ms. Archana Singh'
print(maths_dept)

maths_dept['differential equations']='Dr. Mithu Bhattacharya'
print(maths_dept)
print()

#ASSIGNMENT 8 (SETS)
#1. Example
set1=set([1,2,3,5,7,8])
set2=set([5,10,20,30])

set3=set1|set2
print(set3)

set4=set1&set2
print(set4)

set5=set1-set2
print(set5)

set6=set1^set2
print(set6)
set7=set3^set5
print(set7)
print()

#2. Example
music1=set(['sa','re','ga','ma','pa','dha','ni','sa'])
music2=set(['re','ga','ma','a','b','c'])

music3=music1|music2
print(music3)

music4=music1&music2
print(music4)

music5=music1-music2
print(music5)

music6=music1^music2
print(music6)

print()

#ASSIGNMENT 9 (DATA TYPES)
X=10
print(type(X))

Y=69.5
print(type(Y))

Z='bella ciao'
print(type(Z))

list=[2,3]
print(type(list))

#ASSIGNMENT 10 (ARITHMETIC OPERATORS)
a=50
b=10
c=20
d=40
print(a+b+c)
print(a-b-c)
print(a/c)
print(a*c*d)
print(b%d)
print()

#ASSIGNMENT 11 (INPUT)
First=input('Enter your first name: ')
Middle=input('Enter your middle name: ')
Last=input('Enter your last name: ')
Age=int(input('Enter age: ')
Mobile=input('Enter mobile number: ')
Address=input('Enter address: ')



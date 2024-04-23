#print('Hello World')
a1="Aryan Parle,"
a2="Lower Parel"
a3="Guru Nank Khalsa."
print("My name is " +a1, "I come from "+a2, "and my college's name is "+a3) 
print(a1,a2,a3,sep='/')
print()

#sep('')operator
x=256
y=234
z=456
print(x,y,z,sep=' then ')
print()

#\ operator
print("one\ttwo\nthree\tfour")
print('''one
two
three''')
print()

#ASSIGNMENT 1
print('Welcome to the Python World')
print("I'm a Python learner")
print('''I'm a Python learner and I live in a world of "Python"''')
print("\tPyhton\nFor\n\tBetter\n\tLife")
print()

a=8.9
b=15
print('The Area of Rectangle =',a*b)
print()

#ASSIGNMENT 2
#1. My Contacts
Name="Aryan Parle."
Mobile="7977085519."
Address="Lower Parel."
print('My name is',Name,'\nMy contact number is',Mobile,'\nI live in',Address)
print()

#2. Area of Circumference
import math
r=8
print('The area of circle is',math.pi*r**2)
print()

#3. Mean
x=5
y=10
z=15
print('The mean of',x,y,z,'is',(x+y+z)/3)
print()

#4. Hours to minutes
hours=69
minutes=hours*60
seconds=hours*3600
print(hours,'hours =',minutes,"minutes and",seconds,"seconds.")
print()

#5. Temperature - Celsius to Fahrenheit
c=40
temp=c*9/5+32
print("The temperature of",c,"degrees celsius","in Fahrenheit =",temp,"degrees fahrenheit")
print()

#6. Length & Breadth
L=10
B=20
area=L*B
print('The area of rectangle =',area)
print()

#7. BMI
w=75
h=1.75
bmi=w/h**2
import math
print("The BMI Index =",bmi)
print()

#8. Cube
a=3
cube=a**3
import math
print("The cube of",a,"=",cube)
print()

#9. Swap
a=10
b=20
print(a,b)
a,b=b,a
print(a,b)
print()

#10. Kilometres to Miles
k=150
m=k*0.621371
print(k,'kilometres =',m,'miles')
print()

#11. Tonnes to Quintals & Kilograms
t=10
q=t*10
k=t*1000
print(t,"tonnes =",q,"quintals")
print(t,"tonnes =",k,"kilograms")
print()

#STRING (str)
s1='Hello'
s2='World'
print(s1.lower())
print(s2.upper())
print(s1.isalpha())
print(s2.isdigit())
print(s1.isspace())
print(s2.find("r"))
print(s1.replace("e","o"))
print(s2.replace("o","i"))
print(s1.count("l"))
print(s2.count("d"))
print(s1.len("


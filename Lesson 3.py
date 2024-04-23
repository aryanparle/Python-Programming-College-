#ASSIGNMENT 1
'''First=input("ENTER YOUR FIRST NAME: ")
Middle=input("ENTER YOUR MIDDLE NAME: ")
Last=input("ENTER YOUR LAST NAME: ")
Age=int(input("ENTER YOUR AGE: "))
Mobile=input("ENTER YOUR MOBILE NUMBER: ")
Address=input("ENTER YOUR ADDRESS: ")
print()'''

#ASSIGNEMNT 2
'''p=float(input("Principal ="))
n=float(input("Number of years ="))
r=float(input("Rate of Interest ="))
simple_interest=(p*n*r)/100
print("Simple Interest =",float(simple_interest))

Final_amt=p*pow((1+r/100),n)
compound_interest=Final_amt-p
print("Compound Interest =",compound_interest)'''

#ASSIGNMENT 3
'''slogan=input("Enter your sentence: ")
print("Lower case: ",slogan.lower())
print("Upper case: ",slogan.upper())
print("Length: ",len(slogan))
print()'''

#ASSIGNMENT 4
'''list1=input("Economy of Bumrah: ")
list1=list1.split(',')
list1=[int(value) for value in list1]
print('Results: ',list1)
print()'''

#MAIN ASSIGNMENTS

#Write a program that takes the length of an edge as input and prints the cube's surface area as output.
'''X=int(input("Length of Edge ="))
A=6*(X**2)
#OR A=6*pow(X,2)
print("The surface area of Cube =",A,"square unit.")
print()'''

#Write a program to find the square root of a number by inputting the number through key board.
'''number=float(input("Enter the number: "))
print("The square root of the given number =",number**2,)
print()'''

#Write a program to find the area of a rectangle by inputting the edge through key board.
'''length=float(input("Length of the rectangle: "))
breadth=float(input("Breadth of the rectangle: "))
print("The area of rectangle =",length*breadth,"centimetres.")
print()'''

#Write a program to swap the values of two variables using third variable by inputting the values of the variable through key board.
'''x=input("1st variable: ")
y=input('2nd variable: ')
print("The values are: ",(x,y))
z=y,x
print("The swapped values are :",z)
print()'''

#Write a program to convert kilogram into pound.(1kg = 2.20462)
'''kilogram=float(input("Enter the value in kgs ="))
print(kilogram,"=",kilogram*2.20462)
print()'''

#Write a program that takes the radius of a sphere as input and then outputs the sphere's diameter, circumference, surface area and volume.
'''import math
radius=float(input("Enter the radius of sphere :"))

print("The Sphere's diameter with radius",radius,"=",2*radius,"units.")
print("The Sphere's circumference with radius",radius,"=",2*math.pi*radius,"units.")
print("The Sphere's surface area with radius",radius,"=",4*math.pi*(radius**2),"square units.")
print("The Sphere's volume with radius",radius,"=",(4/3)*math.pi*(radius**3),"cubic units.")
print()'''

#An object's momentum is it's mass multiplied by it's velocity. Write a program that accepts an object's mass (in kg) and velocity (in meters per second) as inputs and the outputs it's momentum.
'''mass=float(input("Enter mass in kilograms :"))
velocity=float(input("Enter velocity in meters per second :"))
print("An object's momentum with mass",mass,"kgs and velocity",velocity,"meters per second =",mass*velocity)
print()'''

#The kinetic energy of a moving object is given by the formula where m is the object's mass and v is it's velocity. Modify the previous program you created so that it prints the object's kinetic energy as well as it's momentum.
'''m=float(input("Mass of the moving object: "))
v=float(input("Velocity of the moving object: "))
print("The kinetic energy of the moving object with mass",m,"and velocity",v,"=",(1/2)*m*(v)**2,"and the momentum =",m*v)
print()'''

#Write a program that calculates and prints the number of minutes in a year.
'''year=int(input("The number of years :"))
print("The number of minutes in",year,"years =",year*365*1440)
print()'''

#Light travels at 3*10^8 meters per second. A light-year is the distance a light beam travel in one year. Write a program that calculates and displays the value of a light year.
'''light_year=int(input("Enter the number of light years :"))
print("Distance travelled in",light_year,"light years =",light_year*365*60*60*24*(3*(10**8)))
print()'''

#12.Question
'''wage= float(input("Hourly wage :"))
regular_hours= float(input("Total number of regular hours :"))
overtime_hours= float(input("Overtime hours :"))
overtime=overtime_hours*1.5*wage
print("An employee's total weekly pay =",wage*regular_hours+overtime)
print()'''

#13.Question

#MAIN ASSIGNMENT
#(IF, ELIF, ELSE OPERATORS)
#Write a program to input a number and check whether it is negative, positive or zero.
'''x=int(input("Enter the number :"))
if x==0:
    print("X is zero")
elif x>0:
    print("X is greater than zero")
else:
    print("X is less than zero")

print("THE PROGRAM IS FINISHED.")'''

#Write a program to determine whether a person is eligible for vote.
'''age= int(input("Enter your age :"))
if age>18:
    print("The person is eligible for voting.")
elif age==18:
    print("The person is eligible for voting.")
else:
    print("The person is not eligible for voting.")
    print("The person will be eligible to vote in",18-age,"years.")
print()'''

#Write a program to input a number and check whether it is even or odd.
'''number= int(input("Enter the number :"))
if number%2==0:
    print("The given number is even.")
else:
    print("The given number is odd.")
print()'''

#Enter gender and salary of an employee. A male gets 10% and female gets 15% of their salary as bonus. Also if the salary is less than 10,000/-, he/she gets 2% of salary
#as extra bonus. Find total bonus

'''gender=input("Enter the gender (in capital letters): ")
salary=float(input("Enter the salary in Rs.: "))

if gender== 'MALE':
    bonus=0.10*salary
else:
    bonus=0.15*salary
print("Bonus =",bonus)

if salary<10000:
    extra_bonus=0.02*salary
else:
    extra_bonus=bonus
    print("Extra bonus =",extra_bonus)
print("The total bonus =",bonus+extra_bonus)
print()'''

#Write a program to find whether an entered year is leap year or not.
'''year=int(input("Enter the year: "))

if year%4==0 and year%100!=0 or year%400==0:
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")
print()'''

#Write a program to input two numbers and find the largest.
'''a=float(input("Enter the 1st number: "))
b=float(input("Enter the 2nd number: "))

if a>b:
    large=a
    print(a,"is the largest number.")
else:
    large=b
print(b,"is the largest number.")
print()'''


    


                     




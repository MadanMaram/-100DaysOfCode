#Day 1
#Given two numbers num1 and num2.The task is to write a Python program to find the addition of these two numbers.
num1 = 5
num2 = 3
print(num1+num2)
#or
num1 =input("enter num:")
num2 =input("enter num:")
b =float(num1)+float(num2)
print(b)

#Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. For example factorial of 6 is 6*5*4*3*2*1 which is 720.
def factorial(n):
    return 1 if(n==1 or n==0)else n*factorial(n-1)
num = 6
print("the factorial:",factorial(num))
#or
def factorial(n):
    return 1:
if(n==1 or n==0):
else n*factorial(n-1):
num = 3
print("the factorial",num,"is",factorial(num))

#Simple interest formula is given by:
#Simple Interest = (P x T x R)/100
#Where,
#P is the principle amount
#T is the time and
#R is the rate

def simple_interest(p, t, r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)
    si = (p*t*r)/100
    print("the simple interest is:",si)
simple_interest(100000,5,5)


#Formula to calculate compound interest annually is given by:
#Compound Interest = P(1 + R/100) t
#Where,
#P is principle amount
#R is the rate and
#T is the time span

def compound_interest(principle,time,rate):
    CI = principle * (pow((1 + rate / 100), time))
    print("Compound interest is", CI)
compound_interest(100000,10.25,5)

#Area of a circle can simply be evaluated using following formula.
#Area = pi * r2
#where r is radius of circle

def findarea(r):
    PI = 3.142
    return PI*(r*r)
print("the area of circle is:",findarea(5))

# Python program to print all
# prime number in an interval
a = range(11,25,2)
for i in a:
    print(i)

#Python Program for n-th Fibonacci number
#In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation
def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

print("the fibonacci number is:",Fibonacci(9))

# Python program to print
# ASCII Value of Character
c = 'g'
# print the ASCII value of assigned character in c
print("The ASCII value of '" + c + "' is", ord(c))

#Python Program for Sum of squares of first n natural numbers
#Given a positive integer N. The task is to find 12 + 22 + 32 + ….. + N2.
def squaresum(n):
    sm = 0
    for i in range(1, n + 1):
        sm = sm + (i * i)
    return sm
n = 2 #1^2 + 2^2 = 1+4 = 5
print("sum of square is:",squaresum(n))

#Python Program for cube sum of first n natural numbers
def sumOfSeries(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i * i
    return sum
# Driver Function
n = 5
print("sumOfSeries is:",sumOfSeries(n))

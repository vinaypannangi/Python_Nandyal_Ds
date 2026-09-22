#1.Add two numbers
def add(a, b):
    return a + b
print(add(10, 20))

#2.Subtract two numbers
def sub(a, b):
    return a - b
print(sub(20, 10))

#3.Multiply two numbers
def multiply(a, b):
    return a * b
print(multiply(5, 4))

#4.Divide two numbers
def divide(a, b):
    return a / b
print(divide(20, 5))

#5.Check even or odd
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"
print(even_odd(7))

#6.Find square
def square(n):
    return n * n
print(square(6))

#7.Find cube
def cube(n):
    return n ** 3
print(cube(4))

#8.Find factorial
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f
print(factorial(5))

#9.Check prime number
def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(prime(7))

#10.Find maximum of two numbers
def maximum(a, b):
    return max(a, b)
print(maximum(15, 25))

#11.Find minimum of two numbers
def minimum(a, b):
    return min(a, b)
print(minimum(15, 25))

#12.Find maximum of three numbers
def maximum(a, b, c):
    return max(a, b, c)
print(maximum(10, 30, 20))

#13.Calculate area of circle
def area(r):
    return 3.14 * r * r
print(area(5))

#14.Calculate area of rectangle
def rectangle(l, b):
    return l * b
print(rectangle(10, 5))

#15.Calculate area of triangle
def triangle(b, h):
    return 0.5 * b * h
print(triangle(10, 8))

#16.Convert Celsius to Fahrenheit
def fahrenheit(c):
    return (c * 9 / 5) + 32
print(fahrenheit(30))

#17.Convert Fahrenheit to Celsius
def celsius(f):
    return (f - 32) * 5 / 9
print(celsius(86))

#18.Check positive or negative
def check(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"
print(check(-5))

#S19.um of numbers
def total(n):
    return sum(range(1, n + 1))
print(total(10))

#20.Print multiplication table
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
        
#21.Check palindrome
def palindrome(s):
    return s == s[::-1]
print(palindrome("madam"))

#22.Count vowels
def vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count
print(vowels("Python Programming"))

#23.Count characters
def count_char(s):
    return len(s)
print(count_char("Hello"))

#24.Convert string to uppercase
def upper(s):
    return s.upper()
print(upper("python"))

#25.Convert string to lowercase
def lower(s):
    return s.lower()
print(lower("PYTHON"))

#26.Find length of list
def list_length(lst):
    return len(lst)
print(list_length([10, 20, 30, 40]))

#27.Find sum of list
def list_sum(lst):
    return sum(lst)
print(list_sum([10, 20, 30]))

#28.Find average
def average(lst):
    return sum(lst) / len(lst)
print(average([10, 20, 30, 40]))

#29.Find largest element
def largest(lst):
    return max(lst)
print(largest([10, 50, 20, 30]))

#30.Find smallest element
def smallest(lst):
    return min(lst)
print(smallest([10, 50, 20, 30]))

#31.Count even numbers
def count_even(lst):
    return sum(1 for x in lst if x % 2 == 0)
print(count_even([1, 2, 4, 7, 8]))

#32.Count odd numbers
def count_odd(lst):
    return sum(1 for x in lst if x % 2 != 0)
print(count_odd([1, 2, 4, 7, 8]))

#33.Find power
def power(a, b):
    return a ** b
print(power(2, 5))

#34.Check leap year
def leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(leap(2024))

#34.Calculate BMI
def bmi(weight, height):
    return weight / (height ** 2)
print(bmi(60, 1.7))

#36.Calculate percentage
def percentage(obtained, total):
    return (obtained / total) * 100
print(percentage(450, 500))

#37.Swap two numbers
def swap(a, b):
    return b, a
print(swap(10, 20))
 
#38.Check divisible by 5
def divisible(n):
    return n % 5 == 0
print(divisible(25))

#39.Generate Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(10)

#40.Find GCD
import math

def gcd(a, b):
    return math.gcd(a, b)
print(gcd(12, 18))

#41.Find LCM
import math

def lcm(a, b):
    return math.lcm(a, b)
print(lcm(4, 6))

#42.Check Armstrong number
def armstrong(n):
    s = str(n)
    return n == sum(int(x) ** len(s) for x in s)
print(armstrong(153))

#43.Count digits
def digits(n):
    return len(str(abs(n)))
print(digits(12345))

#44.Sum of digits
def digit_sum(n):
    return sum(int(x) for x in str(abs(n)))
print(digit_sum(1234))

#45.Reverse a number
def reverse_number(n):
    return int(str(n)[::-1])
print(reverse_number(12345))

#46.Check perfect number
def perfect(n):
    total = sum(i for i in range(1, n) if n % i == 0)
    return total == n
print(perfect(28))

#47.Calculate compound interest
def compound_interest(p, r, t):
    return p * (1 + r / 100) ** t - p
print(compound_interest(10000, 5, 2))

#48.Greeting function
def greet(name):
    return "Hello " + name
print(greet("Vinay"))

#49.Calculate simple interest
def simple_interest(p, r, t):
    return (p * r * t) / 100
print(simple_interest(10000, 5, 2))

#50.table(5)
Reverse a string
def reverse(s):
    return s[::-1]
print(reverse("Python"))
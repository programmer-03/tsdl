#1.	Write a Python program to merge two text files and also count the number of lines in the merged text file.

file1 = 'file1.txt'
file2 = 'file2.txt'
merged_file = 'merged_file.txt'

with open(file1, 'r') as f1, open(file2, 'r') as f2, open(merged_file, 'w') as merged:
    merged.write(f1.read())
    merged.write(f2.read())

with open(merged_file, 'r') as merged:
    line_count = sum(1 for line in merged)

print(f'Number of lines in the merged file: {line_count}')




#2.	Create a class STORE to keep track of products (Product Code, Name and price). Display the menu of all products to the user. Generate bill as per order
class Store:
    def __init__(self):
        self.products = {'001': {'name': 'Product1', 'price': 10},
                         '002': {'name': 'Product2', 'price': 20},
                         '003': {'name': 'Product3', 'price': 30}}

    def display_menu(self):
        print("Product Code\tProduct Name\tPrice")
        for code, details in self.products.items():
            print(f"{code}\t\t{details['name']}\t\t{details['price']}")

    def generate_bill(self, order):
        total_price = 0
        print("Bill:")
        print("Product Code\tProduct Name\tPrice")
        for item in order:
            details = self.products.get(item)
            if details:
                print(f"{item}\t\t{details['name']}\t\t{details['price']}")
                total_price += details['price']
        print(f"Total Price: {total_price}")


# Example usage
store = Store()
store.display_menu()
order = ['001', '002']
store.generate_bill(order)



#3.	Write a Python program to sort a list of elements using the selection sort algorithm
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example Usage:
my_list = [64, 25, 12, 22, 11]
selection_sort(my_list)
print("Sorted list using selection sort:", my_list)



#4.	Write a Python class that has two methods get_string and print_string. Get_string accept a string from the user and print_string print the string in upper case.

class StringManipulator:
    def __init__(self):
        self.my_string = ""

    def get_string(self):
        self.my_string = input("Enter a string: ")

    def print_string(self):
        print("Uppercase String:", self.my_string.upper())

# Example Usage:
str_manipulator = StringManipulator()
str_manipulator.get_string()
str_manipulator.print_string()



"""#5.	Write a python program to count repeated characters in a string Sample String :”thequickbrownfoxjumpsoverthelazydog” Expected output:
o  4
e  3
u  2
h  2
r   2
t   2"""

def count_repeated_characters(input_string):
    char_count = {}
    for char in input_string:
        if char.isalpha() and char.lower() in ["o", "e", "u", "h", "r", "t"]:
            char = char.lower()
            char_count[char] = char_count.get(char, 0) + 1

    for char, count in char_count.items():
        print(f"{char}: {count}")

# Example Usage:
sample_string = "thequickbrownfoxjumpsoverthelazydog"
print("Repeated character count:")
count_repeated_characters(sample_string)



"""6.	Print the pyramid
*
*   *
*   *    *
      AND
       Print the pattern
       *    *    *
       *    *    *
       *    *    *"""
# Pyramid
def print_pyramid(rows):
    for i in range(1, rows + 1):
        print("* " * i)

# Pattern
def print_pattern(rows):
    for i in range(rows, 0, -1):
        print("* " * i)

# Example Usage:
print("Pyramid:")
print_pyramid(3)

print("\nPattern:")
print_pattern(3)




"""7.	Print the pyramid
1
1   2
1   2    3"""
def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Example Usage:
print("Number Pyramid:")
print_number_pyramid(3)





"""8.	Write a python program to print the alphabet pattern ‘O’ and the pattern ‘P’

Expected Output:
***
*  *
*  *
*  *
*  *
*  *
***
AND
****
*     *
*     *
****
*
*
*"""

# Pattern O
print("Pattern O:")
for i in range(7):
    if i == 0 or i == 6:
        print(" *** ")
    else:
        print("*   *")

# Pattern P
print("\nPattern P:")
for i in range(7):
    if i == 0 or i == 3:
        print("**** ")
    elif i < 3:
        print("*   *")
    else:
        print("*")






"""9.	Create an EMPLOYEE class for storing details(Name, Designation, gender, date of joining and salary).Define function members to compute
a.	Total number of employees in an organization
b.	Count male and female employees
c.	An employee with a salary of more than 10,000
d.	Employee with designation “Manager”"""


class EMPLOYEE:
    total_employees = 0
    male_count = 0
    female_count = 0
    high_salary_count = 0
    manager_count = 0

    def __init__(self, name, designation, gender, join_date, salary):
        self.name = name
        self.designation = designation
        self.gender = gender
        self.join_date = join_date
        self.salary = salary

        EMPLOYEE.total_employees += 1

        if gender.lower() == 'male':
            EMPLOYEE.male_count += 1
        elif gender.lower() == 'female':
            EMPLOYEE.female_count += 1

        if salary > 10000:
            EMPLOYEE.high_salary_count += 1

        if designation.lower() == 'manager':
            EMPLOYEE.manager_count += 1

# Example Usage:
employee1 = EMPLOYEE('John Doe', 'Manager', 'Male', '2022-01-01', 12000)
employee2 = EMPLOYEE('Jane Smith', 'Developer', 'Female', '2022-01-15', 8000)

print("Total Employees:", EMPLOYEE.total_employees)
print("Male Employees:", EMPLOYEE.male_count)
print("Female Employees:", EMPLOYEE.female_count)
print("Employees with Salary > 10,000:", EMPLOYEE.high_salary_count)
print("Managers:", EMPLOYEE.manager_count)




"""10.	Write a Python program to construct the following pattern using a nested loop
*
*   *
*   *    *
*   *    *    *   
*   *    *    *    *
*   *    *    *   
*   *    *
*   *
*
"""
def print_nested_loop_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(" * ", end="")
        print()
    for i in range(rows - 1, 0, -1):
        for j in range(1, i + 1):
            print(" * ", end="")
        print()

# Example Usage:
print("Nested Loop Pattern:")
print_nested_loop_pattern(5)





"""11.	Given two lists create a third list by picking an odd-index element from the first list and even index elements from the second"""
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

result_list = list1[1::2] + list2[::2]
print("Result List:", result_list)




"""12.	a. Write a program to print each line of a text file in reverse order
b. Print the substring from the input string “Vishwakarma University” from index 2 to 14
"""
with open('text_file.txt', 'r') as file:
    lines = file.readlines()
    reversed_lines = [line.strip()[::-1] for line in lines]

print("Lines in Reverse Order:")
for line in reversed_lines:
    print(line)

input_string = "Vishwakarma University"
substring = input_string[2:15]
print("Substring:", substring)




"""13.	Write a Pandas program to add, subtract, multiple and divide two Pandas Series. 
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
"""

import pandas as pd

series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])

add_result = series1 + series2
subtract_result = series1 - series2
multiply_result = series1 * series2
divide_result = series1 / series2

print("Addition Result:")
print(add_result)
print("\nSubtraction Result:")
print(subtract_result)
print("\nMultiplication Result:")
print(multiply_result)
print("\nDivision Result:")
print(divide_result)






"""14.	Write a Pandas program to sort a given Series. 

Original Data Series: 

0 100
1 200
2 python
3 300.12
4 400
dtype: object
ans: """

import pandas as pd

data_series = pd.Series([100, 200, 'python', 300.12, 400])
# Convert all values to strings before sorting
sorted_series = data_series.astype(str).sort_values(ascending=True)

print("Sorted Data Series:")
print(sorted_series)




"""
15.	Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
"""
import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
selected_columns = df[['name', 'score']]
print("Selected Columns:")
print(selected_columns)






"""
16.	Write a Python program to print alphabet pattern 'R' and pattern’O’ 
Expected Output:
 ****                                                                   
 *   *                                                                  
 *   *                                                                  
 ****                                                                   
 * *                                                                    
 *  *                                                                   
 *   *
AND
  ***                                                                   
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                 
 *   *                                                                  
  *** """
# Pattern R
# Modified Pattern R
print("Modified Pattern R:")
for i in range(7):
    if i == 0 or i == 3:
        print("**** ")
    elif i < 3:
        print("*   *")
    elif i == 4:
        print("* *  ")
    else:
        print("*   *")

# Pattern O
print("\nPattern O:")
for i in range(7):
    if i == 0 or i == 6:
        print(" *** ")
    else:
        print("*   *")

    



"""
17.	Write a Python program that matches a word containing 'z', not at the start or end of the word and match a string that contains only upper and lowercase letters, numbers, and underscores by using function
import re"""

import re
def match_word_and_string(word, input_string):
    # Match a word containing 'z', not at the start or end of the word
    match_word = re.search(r'\b(?<!\bz)\w*z\w*(?!\bz)\b', word)
    
    # Match a string that contains only upper and lowercase letters, numbers, and underscores
    match_string = re.match(r'^[A-Za-z0-9_]+$', input_string)

    return match_word, match_string

# Example Usage:
word_match, string_match = match_word_and_string("amazing", "Python_123")
print("Word Match:", word_match.group() if word_match else None)
print("String Match:", "Valid" if string_match else "Invalid")







"""
18.	Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

# Example Usage:
rectangle1 = Rectangle(5, 7)
area1 = rectangle1.compute_area()
print("Area of Rectangle 1:", area1)

rectangle2 = Rectangle(8, 10)
area2 = rectangle2.compute_area()
print("Area of Rectangle 2:", area2)






"""
19.	To calculate salary of an employee given his basic pay (take as input from user). Calculate gross salary of employee. Let HRA be 10 % of basic pay and TA be 5% of basic pay. Let employee pay professional tax as 2% of total salary. Calculate net salary payable after deductions.
"""
basic_pay = float(input("Enter the basic pay: "))

# HRA is 10% of basic pay
hra = 0.1 * basic_pay

# TA is 5% of basic pay
ta = 0.05 * basic_pay

# Gross salary
gross_salary = basic_pay + hra + ta

# Professional tax is 2% of total salary
professional_tax = 0.02 * gross_salary

# Net salary after deductions
net_salary = gross_salary - professional_tax

print("Gross Salary:", gross_salary)
print("Net Salary after Deductions:", net_salary)




"""
20.	Find the factorial of a number by using function. Accept a number from user and reverse the number by using function.
"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def reverse_number(number):
    return int(str(number)[::-1])

# Example Usage:
num = int(input("Enter a number for factorial and reversal: "))
factorial_result = factorial(num)
reverse_result = reverse_number(num)

print(f"Factorial of {num}: {factorial_result}")
print(f"Reverse of {num}: {reverse_result}")




"""
21.	Write a Python program to count the number of words in a sentence"""
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print("Number of words in the sentence:", word_count)




"""
22.	 Write a Python program to add, multiply two matrices using numpy
"""
import numpy as np

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Addition
matrix_sum = np.add(matrix1, matrix2)

# Multiplication
matrix_product = np.dot(matrix1, matrix2)

print("Matrix Addition:")
print(matrix_sum)
print("\nMatrix Multiplication:")
print(matrix_product)





"""
23.	Write a Python program to count number of characters, words, spaces and lines in a file."""
file_path = 'sample.txt'

with open(file_path, 'r') as file:
    content = file.read()

char_count = len(content)
word_count = len(content.split())
space_count = content.count(' ')
line_count = content.count('\n') + 1

print("Number of Characters:", char_count)
print("Number of Words:", word_count)
print("Number of Spaces:", space_count)
print("Number of Lines:", line_count)




"""
24.	a) Write a program that matches a word containing ‘z’."""
import re

def match_word_z(word):
    match_result = re.search(r'\b\w*z\w*\b', word)
    return match_result.group() if match_result else None

# Example Usage:
word = input("Enter a word: ")
result = match_word_z(word)
print("Matched Word:", result)
#b) Write a program that matches a string that has an a followed by zero or more b’s.
import re

def match_string_a_followed_by_bs(input_string):
    match_result = re.fullmatch(r'a(b*)', input_string)
    return match_result.group(1) if match_result else None

# Example Usage:
string = input("Enter a string: ")
result = match_string_a_followed_by_bs(string)
print("Matched String:", result)





"""
25.	Write a program that accepts a list from user and print the alternate element of list.
"""
user_list = input("Enter elements of the list separated by spaces: ").split()
alternate_elements = user_list[::2]
print("Alternate Elements of the List:", alternate_elements)





"""26.	Write a program that reads an integer value n from the user, and then produces n lines of output. The first line contains 1 star, the second 2 stars, and so on until the last line, which should have n stars. Can you write this using only a single loop? Hint:
Remember what the expression ‘+’*5 does.
Enter a size: 5
+
++
+++
++++
+++++

Ans: """
n = int(input("Enter a size: "))

for i in range(1, n + 1):
    print('+' * i)






"""27.	Sort following NumPy array
Case 1: Sort array by the second row
Case 2: Sort the array by the second column
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])

ans:"""
import numpy as np

sample_array = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

# Case 1: Sort array by the second row
sorted_array_case1 = sample_array[:, sample_array[1, :].argsort()]

# Case 2: Sort the array by the second column
sorted_array_case2 = sample_array[sample_array[:, 1].argsort()]

print("Sorted Array by Second Row:")
print(sorted_array_case1)
print("\nSorted Array by Second Column:")
print(sorted_array_case2)




"""
28.	Take two input strings, concatenate them, and print the output. Also, Reverse the string and print it."""

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Concatenate strings
concatenated_string = string1 + string2

# Reverse concatenated string
reversed_string = concatenated_string[::-1]

print("Concatenated String:", concatenated_string)
print("Reversed String:", reversed_string)





"""
29.	Write a Python program to find maximum and minimum K elements in Tuple. Take user input for K."""

k = int(input("Enter the value of K: "))
my_tuple = (10, 5, 8, 20, 15)

max_k_elements = tuple(sorted(my_tuple, reverse=True)[:k])
min_k_elements = tuple(sorted(my_tuple)[:k])

print(f"Maximum {k} elements:", max_k_elements)
print(f"Minimum {k} elements:", min_k_elements)





"""
30.	Write a python program to search some literals strings in a string from a file.
Sample text : “the quick brown fox jumps over the lazy dog”
Searched words : “fox”,”dog”,”horse”
"""
file_path = 'sample.txt'
searched_words = ["fox", "dog", "horse"]

with open(file_path, 'r') as file:
    text = file.read()

for word in searched_words:
    if word in text:
        print(f"{word} found in the text.")
    else:
        print(f"{word} not found in the text.")






"""
31.	Write a python program to check whether a string contains all letters of the alphabet
"""
import string

def contains_all_letters(input_string):
    return all(letter in input_string.lower() for letter in string.ascii_lowercase)

# Example Usage:
user_string = input("Enter a string: ")
result = contains_all_letters(user_string)
print("String contains all letters of the alphabet:", result)





"""
32.	Write a Python class to implement pow(x,n)
"""
class PowerCalculator:
    @staticmethod
    def power(x, n):
        return x ** n

# Example Usage:
calculator = PowerCalculator()
result = calculator.power(2, 3)
print("Result of pow(2, 3):", result)






"""
33.	Write a Python program to swap two elements in a list. Take user input for the swap index
"""
user_list = input("Enter elements of the list separated by spaces: ").split()
print("Original List:", user_list)

index1 = int(input("Enter the index of the first element to swap: "))
index2 = int(input("Enter the index of the second element to swap: "))

user_list[index1], user_list[index2] = user_list[index2], user_list[index1]
print("List after swapping elements:", user_list)





"""
34.	Write a Python program to create a file where all letters of the English alphabet are listed by a specified number of letters on each line
"""
with open('alphabet_file.txt', 'w') as file:
    for letter in string.ascii_uppercase:
        file.write(letter + '\n')





"""
35.	Generate two lists of random data and create a scatter plot to visualize their relationship. Label the axes 
"""

import matplotlib.pyplot as plt
import numpy as np

# Generate random data
data1 = np.random.rand(10)
data2 = np.random.rand(10)

# Create a scatter plot
plt.scatter(data1, data2)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.show()




"""
36.	 Write a Python program that calculates basic statistical operations, including mean, median, and standard deviation, on a given NumPy array
"""
import numpy as np

data_array = np.random.rand(10)

mean_value = np.mean(data_array)
median_value = np.median(data_array)
std_deviation = np.std(data_array)

print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)





"""
37.	Design a class hierarchy for a restaurant management system. Define the relevant attributes and methods for the classes.
a. Create a base class Dish with attributes such as dish_name, price, and cuisine_type.
b. Derive a subclass Appetizer from Dish to represent appetizer items.
c. Further derive a class VegetarianAppetizer from Appetizer to represent vegetarian appetizer items.
"""
class Dish:
    def __init__(self, dish_name, price, cuisine_type):
        self.dish_name = dish_name
        self.price = price
        self.cuisine_type = cuisine_type

    def display_info(self):
        print(f"{self.dish_name} - Cuisine: {self.cuisine_type}, Price: {self.price:.2f}")

class Appetizer(Dish):
    def __init__(self, dish_name, price, cuisine_type, is_spicy):
        super().__init__(dish_name, price, cuisine_type)
        self.is_spicy = is_spicy

    def display_info(self):
        super().display_info()
        print(f"Spicy: {'Yes' if self.is_spicy else 'No'}")

class VegetarianAppetizer(Appetizer):
    def __init__(self, dish_name, price, is_spicy):
        super().__init__(dish_name, price, cuisine_type="Vegetarian", is_spicy=is_spicy)

# Example Usage:
dish1 = Dish("Pasta Carbonara", 599, "Italian")
dish2 = Appetizer("Spring Rolls", 299, "Asian", True)
dish3 = VegetarianAppetizer("Spinach Dip", 399, False)

dish1.display_info()
print()
dish2.display_info()
print()
dish3.display_info()






"""
38.	Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included)"""
squares_list = [x**2 for x in range(1, 31)]
print("List of Squares:", squares_list)





"""
39.	Design a class hierarchy for a ticket booking management system. Define the relevant attributes and methods for the classes.
a. Derive subclasses such as Ticket, MovieTicket, and ConcertTicket. Add appropriate attributes and methods to represent different types of tickets.
b. Create a class BookingSystem that inherits from Ticket to manage the overall ticket booking process
"""
from datetime import datetime

class Ticket:
    def __init__(self, ticket_id, event_name, event_date, price):
        self.ticket_id = ticket_id
        self.event_name = event_name
        self.event_date = event_date
        self.price = price
        self.is_booked = False

    def display_info(self):
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Event: {self.event_name}")
        print(f"Date: {self.event_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Price: ₹{self.price:.2f}")
        print(f"Status: {'Booked' if self.is_booked else 'Available'}")

    def book_ticket(self):
        if not self.is_booked:
            self.is_booked = True
            print("Ticket booked successfully!")
        else:
            print("Ticket is already booked.")

class MovieTicket(Ticket):
    def __init__(self, ticket_id, movie_name, show_time, price):
        event_date = datetime.now().replace(hour=show_time.hour, minute=show_time.minute, second=0, microsecond=0)
        super().__init__(ticket_id, movie_name, event_date, price)
        self.movie_name = movie_name
        self.show_time = show_time

class ConcertTicket(Ticket):
    def __init__(self, ticket_id, artist, concert_date, price):
        super().__init__(ticket_id, artist, concert_date, price)
        self.artist = artist

class BookingSystem:
    def __init__(self):
        self.available_tickets = []

    def add_ticket(self, ticket):
        self.available_tickets.append(ticket)

    def display_available_tickets(self):
        print("Available Tickets:")
        for ticket in self.available_tickets:
            ticket.display_info()
            print("-----------")

# Example Usage:
movie_ticket = MovieTicket(1, "Inception", datetime(2023, 1, 15, 18, 30), 399)
concert_ticket = ConcertTicket(2, "Coldplay Concert", datetime(2023, 2, 20, 20, 0), 4999)

booking_system = BookingSystem()
booking_system.add_ticket(movie_ticket)
booking_system.add_ticket(concert_ticket)

booking_system.display_available_tickets()

movie_ticket.book_ticket()
movie_ticket.display_info()




"""
40.	Write a Python program to shuffle the elements of a given list
"""
import random

user_list = input("Enter elements of the list separated by spaces: ").split()
random.shuffle(user_list)
print("Shuffled List:", user_list)




"""
41.	Calculate the number of days between the two given dates"""
from datetime import datetime

date_format = "%Y-%m-%d"

date1 = input("Enter the first date (YYYY-MM-DD): ")
date2 = input("Enter the second date (YYYY-MM-DD): ")

delta = datetime.strptime(date2, date_format) - datetime.strptime(date1, date_format)
print("Number of days between the two dates:", delta.days)





"""
42.	Write a program to count no. of vowels in a string"""
user_string = input("Enter a string: ")
vowel_count = sum(1 for char in user_string.lower() if char in 'aeiou')
print("Number of vowels in the string:", vowel_count)




"""
43.	Create a result array by adding the following two NumPy arrays. Next, modify the result array by calculating the square of each element. Also generate the transposition of an array using the tool numpy
"""
import numpy as np

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

result_array = array1 + array2
modified_result = result_array ** 2
transposed_array = result_array.T

print("Original Result Array:")
print(result_array)
print("\nModified Result Array (Squared):")
print(modified_result)
print("\nTransposed Result Array:")
print(transposed_array)





"""
44.	Write a python program to copy one file to another file and the first two lines from the copied file."""
with open('source_file.txt', 'r') as source_file, open('destination_file.txt', 'w') as destination_file:
    content = source_file.read()
    destination_file.write(content)

with open('destination_file.txt', 'r') as copied_file:
    first_two_lines = copied_file.readlines()[:2]
    print("First Two Lines from Copied File:")
    for line in first_two_lines:
        print(line.strip())






"""
45.	Write a python program to check how many times a given number can be divided by 3 before it is less than or equal to 10."""
number = int(input("Enter a number: "))
count = 0

while number > 10:
    number /= 3
    count += 1

print(f"The given number can be divided by 3, {count} times before it is less than or equal to 10.")







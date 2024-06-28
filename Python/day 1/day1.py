# basic syntax of python code 
# print("Hello, world!")

# variables 
# Variables are containers for storing data values.
# A variable is created the moment you first assign a value to it.
# Variables declaration


# x = 10
# y = "This is a string"

# comments
# "This is a single line comment"
"""This is a multiline comment
    Multiline comment continues here"""

# printing variables
# print("value of the x is: ",x)
# print("value of the y is: ",y)

# Typecasting
# a = int('55')
# b = float(55)
# c = int(a)
# # print(c)
# print("Type of a is ",type(a))
# print("Type of b is ",type(b))
# print("Type of c is ",type(c))


# Challenge 
'''print the type of the variable'''

# solution
# print("Type of b is ",(type(b).__name__))
# 

# ===========================================================================================================
# =============================      variable names         =================================================
# ===========================================================================================================

# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). 
# 
# 
# Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

# legal variable name

# abc = 15
# ___xyz__ = 'xyz'
# small_num = 1
# largeNum = 99
# EvenNum = 2

# print(___xyz__)

# illegal variable name

# 1abc = 15 
    # variable names cannot start with a number
# my var = 'abc'
    # variable names cannot contain spaces
# my-var = 'abc' 
    # variable names cannot contain hyphens


# ==========================================================================================================
# =====================================   Multi Words Variable Names    ====================================
# ==========================================================================================================
# Variable names with more than one word can be difficult to read.
# There are several techniques you can use to make them more readable:

# When naming variables with more than one word in programming, it's essential to use a clear and consistent naming convention to enhance readability and maintainability. Here are the three common naming conventions with examples and their appropriate contexts:

### 1. Camel Case
# In camel case, the first word is in lowercase, and each subsequent word starts with a capital letter. This style is commonly used in many programming languages, particularly in JavaScript and Java.

# ```python
# myVariableName = "John"
# totalAmountDue = 150.75
# employeeFirstName = "Alice"
# ```

# **Context:** 
# - Typically used in languages like JavaScript, Java, and others for variable names and methods.
# - Good for readability, especially in languages that do not support underscores in variable names.

# ### 2. Pascal Case
# Pascal case is similar to camel case but with the first word also starting with a capital letter. This is often used for class names in languages like C# and Java.

# ```python
# MyVariableName = "John"
# TotalAmountDue = 150.75
# EmployeeFirstName = "Alice"
# ```

# **Context:**
# - Commonly used for class names in languages such as C#, Java, and others.
# - Helps in distinguishing between variable names and class names when both are present in the codebase.

# ### 3. Snake Case
# In snake case, each word is written in lowercase and separated by an underscore (`_`). This style is widely used in Python and other languages that emphasize readability.

# ```python
# my_variable_name = "John"
# total_amount_due = 150.75
# employee_first_name = "Alice"
# ```

# **Context:**
# - Standard for variable names and function names in Python.
# - Often used in configuration files, constants, and scripts where readability is prioritized.

# ### Choosing the Right Convention
# - **Camel Case:** Preferable in JavaScript and languages where camelCase is a de facto standard for variables and functions.
# - **Pascal Case:** Ideal for naming classes or when working in environments where this convention is the norm.
# - **Snake Case:** Best for Python scripts, configuration settings, and where clarity and readability are crucial.

# ### Summary

# Use the naming convention that is most appropriate for your programming language and project style guidelines. Here’s a quick summary of when to use each:

# | Naming Convention | Example             | Typical Use Case                       |
# |-------------------|---------------------|----------------------------------------|
# | Camel Case        | `myVariableName`    | Variables, functions in JavaScript, Java |
# | Pascal Case       | `MyVariableName`    | Class names in C#, Java                |
# | Snake Case        | `my_variable_name`  | Variables, functions in Python, config files |

# Adopting a consistent naming strategy helps make your codebase more understandable and maintainable for yourself and others.


# =======================================================================================================
# =================================     Assigning multiple variables ====================================
# =======================================================================================================

# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# Unpack a collection 

# Unpacking a collection into variables in Python allows you to assign elements from a collection (like a list or tuple) directly to individual variables in a single line of code. This is a powerful feature for simplifying code and improving readability. Here’s how you can do it with different types of collections:

# Basic Unpacking
# When you have a collection like a list or tuple, you can unpack its elements directly into variables:

# Unpacking collections in Python allows you to assign elements of a collection (like a list, tuple, or dictionary) to individual variables in a concise way. Here’s how you can unpack various types of collections:

# ### 1. Unpacking Lists and Tuples

# You can unpack elements from a list or tuple directly into variables:

# # Example with a tuple
# coordinates = (10, 20, 30)
# x, y, z = coordinates
# print(x)  # Output: 10
# print(y)  # Output: 20
# print(z)  # Output: 30

# # Example with a list
# colors = ["red", "green", "blue"]
# first, second, third = colors
# print(first)   # Output: red
# print(second)  # Output: green
# print(third)   # Output: blue
# 

# ### 2. Unpacking with `*` Operator

# If you have more elements than variables or you want to capture the remaining elements, you can use the `*` operator.

# 
# # Unpacking with *
# numbers = [1, 2, 3, 4, 5]
# a, b, *rest = numbers
# print(a)     # Output: 1
# print(b)     # Output: 2
# print(rest)  # Output: [3, 4, 5]

# # Unpacking in the middle
# a, *middle, e = numbers
# print(a)       # Output: 1
# print(middle)  # Output: [2, 3, 4]
# print(e)       # Output: 5
# 

# ### 3. Unpacking Dictionaries

# You can unpack dictionaries into variables representing the keys, or into variables representing both keys and values using the `items()` method.

# 
# # Unpacking dictionary keys
# person = {"name": "Alice", "age": 30, "city": "New York"}
# name, age, city = person
# print(name)  # Output: name
# print(age)   # Output: age
# print(city)  # Output: city

# # Unpacking dictionary items
# name, age, city = person.values()
# print(name)  # Output: Alice
# print(age)   # Output: 30
# print(city)  # Output: New York

# # Using items() to unpack keys and values
# for key, value in person.items():
#     print(f"{key}: {value}")
# # Output:
# # name: Alice
# # age: 30
# # city: New York
# 

# ### 4. Unpacking Nested Collections

# When dealing with nested collections, you can unpack them in multiple levels.

# ```python
# # Nested tuple
# nested_tuple = (1, (2, 3), 4)
# a, (b, c), d = nested_tuple
# print(a)  # Output: 1
# print(b)  # Output: 2
# print(c)  # Output: 3
# print(d)  # Output: 4

# # Nested list
# nested_list = ["John", ["Doe", "Smith"], 25]
# first_name, [middle_name, last_name], age = nested_list
# print(first_name)   # Output: John
# print(middle_name)  # Output: Doe
# print(last_name)    # Output: Smith
# print(age)          # Output: 25
# ```

# ### 5. Practical Example: Swapping Variables

# Unpacking is often used for swapping variables without a temporary variable:

# ```python
# a = 5
# b = 10
# a, b = b, a
# print(a)  # Output: 10
# print(b)  # Output: 5
# ```

# ### Summary

# Unpacking is a powerful feature in Python that simplifies the assignment of elements from collections to individual variables. It can be used with lists, tuples, dictionaries, and nested structures, enhancing the readability and conciseness of your code.




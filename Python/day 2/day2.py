# ==========================================================================================================
# ============================       Datatypes =============================================================
# ==========================================================================================================

# Python is a versatile programming language that supports a wide range of data types. These data types are used to define the nature of data, such as integers, floating-point numbers, or text strings, and how that data can be manipulated. Here’s a comprehensive overview of Python’s built-in data types:

# 1. Numeric Types
    # a. Integers (int)
    # Whole numbers without a decimal point.
    # They can be of arbitrary length in Python.
    # Example: 10, -42, 1234567890
    
    # b. Floating-Point Numbers (float)
    # Numbers with a decimal point.
    # Represent real numbers with fractional parts.
    # Example: 3.14, -0.001, 2.0
    
    # c. Complex Numbers (complex)
    # Numbers with a real and an imaginary part.
    # The imaginary part is denoted with a j or J.
    # Example: 3 + 4j, -5 - 2.3j

# 2. Sequence Types
    # a. Strings (str)
    # Ordered collection of characters enclosed in single, double, or triple quotes.
    # Immutable (cannot be changed after creation).
    # Example: "Hello", 'Python', '''Multi-line string'''

    # b. Lists (list)
    # Ordered collection of items (elements) that are mutable.
    # Elements can be of different data types.
    # Defined using square brackets [].
    # Example: [1, "apple", 3.14]

    # c. Tuples (tuple)
    # Ordered collection of items that are immutable.
    # Defined using parentheses ().
    # Example: (1, "apple", 3.14)

    # d. Ranges (range)
    # Represents a sequence of numbers.
    # Often used in loops.
    # Example: range(0, 10) generates numbers from 0 to 9.

# 3. Mapping Types
    # a. Dictionaries (dict)
    # Unordered collection of key-value pairs.
    # Keys must be unique and immutable.
    # Defined using curly braces {}.
    # Example: {"name": "Alice", "age": 25}

# 4. Set Types
    # a. Sets (set)
    # Unordered collection of unique elements.
    # Defined using curly braces {} or the set() function.
    # Example: {1, 2, 3, 4}, set([1, 2, 3, 4])

    # b. Frozen Sets (frozenset)
    # Immutable version of a set.
    # Defined using the frozenset() function.
    # Example: frozenset([1, 2, 3, 4])

# 5. Boolean Type
    # a. Booleans (bool)
    # Represents one of two values: True or False.
    # Used in conditional statements and comparisons.
    # Example: True, False

# 6. Binary Types
    # a. Bytes (bytes)
    # Immutable sequence of bytes.
    # Used for binary data.
    # Defined using the b prefix.
    # Example: b"Hello"

    # b. Byte Arrays (bytearray)
    # Mutable sequence of bytes.
    # Example: bytearray(b"Hello")

    # c. Memory Views (memoryview)
    # A view of memory of another binary data object (e.g., bytes or bytearray).
    # Example: memoryview(bytearray(b"Hello"))

# 7. None Type
    # a. None (NoneType)
    # Represents the absence of a value or a null value.
    # Often used to signify no value or a placeholder.
    # Example: None

# ----------------------------------------------------------------------------------------------------------
# ------------------------------   Number Types ------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------

# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# print("The value of x is :" , x , "and type of x is :", type(x).__name__ ) 
# print("The value of y is :" , y , "and type of y is :", type(y).__name__ ) 
# print("The value of z is :" , z , "and type of z is :", type(z).__name__ ) 

    # Note: The type() function returns the type object of the argument. The __name__ attribute returns the name of the class or module. In this case, the type name is "int", "float", and "complex" respectively.

# x = 35e3
# y = 12E4
# z = -87.7e100

# print(type(x))
# print(type(y))
# print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.

# --------------------------------------------------------------------------------------------------------
#                           
# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# #convert from int to float:
# a = float(x)

# #convert from float to int:
# b = int(y)

# #convert from int to complex:
# c = complex(x)

# # d = int(z)   # Gives error
# # e = float(z)    # Gives error

# print(a)
# print(b)
# print(c)
# # print(d)
# # print(e)
# print(type(a))
# print(type(b))
# print(type(c))

# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------- String ---------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------


# Strings in Python are a fundamental data type used to represent sequences of characters. They are highly versatile and come with a wide range of operations and methods that allow you to manipulate text in various ways
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:

# ----------------------------------------------------------------------------------------------------------

# single_quote_str = 'Hello'
# double_quote_str = "World"
# triple_quote_str = '''This is a 
# multi-line string


# stilll it working'''


# print(single_quote_str)
# print(double_quote_str)
# print(triple_quote_str)

# ----------------------------------------------------------------------------------------------------------

# original = "Hello"
# original += " World" 

# print(original)

# ----------------------------------------------------------------------------------------------------------

# string length 

# str1 = "Hello, World"
# print(len(str1))

# ----------------------------------------------------------------------------------------------------------

# check string 

str1 = "life is good make it great"
# print("life" in str1)

# if "great" in str1:
#     print("Yes, 'great' is present in the string.")

# if "xyz" not in str1:
#     print("No, 'xyz' is not present in the string.")

# ----------------------------------------------------------------------------------------------------------

# string slicing

# str2 = "Hello, World!"
# print(str2[2:10]) #output = llo, Wor
# print(str2[:5]) #output = Hello
# print(str2[2:]) #output = llo, World!

# ----------------------------------------------------------------------------------------------------------

# string modification 

# str3 = "Hello, World!"
# str3 = str3.replace("World", "Universe")
# print(str3) #output = Hello, Universe!

# upper case
# a = "Hello world!"
# print(a.upper()) #output = HELLO WORLD!

# lower case
# a = "HELLO WORLD!"
# print(a.lower()) #output = hello world!

# title case
# a = "hello world! tHis is tiTle"
# print(a.title()) #output = Hello World!

# strip leading and trailing white spaces
# a = "    Hello, World!   "
# print(a.strip()) #output = Hello, World!

# split string into a list
# a = "Hello, World! This is a test"
# print(a.split()) #output = ['Hello,', 'World!', 'This', 'is', 'a', 'test']

# join list elements into a string

# list1 = ['Hello,', 'World!', 'This', 'is', 'a', 'test']
# print(' '.join(list1)) #output = Hello, World! This is a test

# ----------------------------------------------------------------------------------------------------------

# concatenate string

# a = "Hello"
# b = "World"
# c = a + b;
# c = a + " " + b;
# print(c)

                                                    # f-string 

# age = 20 

# f-string syntax: f"string {expression}"
# f-string is a way to embed expressions inside string literals.
# It's useful when you want to include the result of an operation inside a string.

# str = f"Hello, My name is John and my age is {age}"
# print(str)

# price_pen = 10
# price_pencil = 5
# print(f"The price of this pen is {price_pen:.2f} rs and price of this pencil is {price_pencil:.2f} rs ")
# print(f"totol price is {(price_pen + price_pencil ):.2f} rs ")



                                    # escape sequence characters

                                    
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value
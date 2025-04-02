# Python for Ethical Hacking - Beginner's Guide

## 1. Introduction to Python for Ethical Hacking
Python is widely used in cybersecurity due to its simplicity and powerful libraries. In this guide, we’ll cover the fundamental Python concepts that are essential for ethical hacking.

## 2. Python Basics
Before diving into hacking, you should be comfortable with the following concepts:

### 2.1 Variables and Data Types
Variables store data values. Python supports various data types such as integers, floats, strings, and lists.
```python
x = 10  # Integer
y = 3.14  # Float
name = "Hacker"  # String
is_active = True  # Boolean
```

### 2.2 Loops (For & While)
Loops allow execution of a block of code multiple times.
```python
# For loop
for i in range(5):
    print("Iteration:", i)

# While loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1
```

### 2.3 Conditional Statements (If-Else)
Conditionals control the flow of execution based on conditions.
```python
age = 20
if age >= 18:
    print("Access granted")
else:
    print("Access denied")
```

### 2.4 Functions and Modules
Functions allow code reusability, and modules enable additional functionalities.
```python
def greet(name):
    return "Hello, " + name

print(greet("Hacker"))
```
Importing built-in modules:
```python
import os
print(os.name)
```

## 3. File Handling
Reading and writing files is crucial for log analysis and data storage.
```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("This is a test file.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

## 4. Networking with Sockets
The `socket` module helps in network communications, such as scanning open ports.
```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("example.com", 80))
s.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
response = s.recv(1024)
print(response.decode())
s.close()
```

## 5. Regular Expressions (Regex) for Pattern Matching
Regex is used for extracting and validating data (e.g., finding emails in text).
```python
import re

text = "Contact me at hacker@example.com"
pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
match = re.findall(pattern, text)
print("Found emails:", match)
```

## 6. Hands-On Exercises
1. **Create a script that scans open ports on a given IP.**
2. **Write a program to extract all URLs from a webpage.**
3. **Develop a keylogger (for legal educational purposes only).**

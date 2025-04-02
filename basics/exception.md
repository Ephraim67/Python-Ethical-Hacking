### **Understanding Exceptions in Python**  

An **exception** is an **error** that occurs during program execution, **interrupting the normal flow** of the program.  

🔹 If an exception is **not handled**, the program will **crash**.  
🔹 Python provides a way to **handle exceptions** using `try-except` blocks, ensuring that the program **does not terminate unexpectedly**.  


## **1. Common Exceptions in Python**  

Python has several built-in exceptions. Some common ones are:  

| Exception | Cause |
|-----------|-------------|
| `ZeroDivisionError` | Division by zero (`5 / 0`) |
| `TypeError` | Wrong data type (`"5" + 5`) |
| `ValueError` | Invalid value (`int("abc")`) |
| `IndexError` | List index out of range (`my_list[10]`) |
| `KeyError` | Key not found in dictionary (`my_dict['key']`) |
| `FileNotFoundError` | File does not exist (`open('file.txt')`) |


## **2. Handling Exceptions with `try-except`**  

The **`try-except` block** is used to handle errors and **prevent program crashes**.  

### **Example 1: Handling `ZeroDivisionError`**  
```python
try:
    result = 10 / 0  # Division by zero error
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
```
✔️ **Output:**  
```
Error: Cannot divide by zero!
```
👉 The program **does not crash** and continues execution.


## **3. Handling Multiple Exceptions**  

You can handle **different exceptions separately**.  

### **Example 2: Handling `ZeroDivisionError` and `ValueError`**  
```python
try:
    num = int(input("Enter a number: "))  # Input a number
    result = 10 / num  # Potential ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")
```
✔️ **Possible Outputs:**  
- If input is `"abc"` → `Error: Please enter a valid number!`  
- If input is `0` → `Error: Cannot divide by zero!`  


## **4. Using `else` with `try-except`**  
- The `else` block runs **only if no exception occurs**.  

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
else:
    print("Division successful:", result)
```

## **5. Using `finally` (Always Executes)**  
- The `finally` block **always executes**, whether an exception occurs or not.  
- It is often used for **clean-up operations** (e.g., closing files, releasing resources).  

```python
try:
    file = open("test.txt", "r")  # Try to open a file
    content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
finally:
    print("Closing file (if opened).")
    file.close()  # Ensure file is closed
```

✔️ **Output (if file exists):**  
```
Closing file (if opened).
```
✔️ **Output (if file doesn't exist):**  
```
Error: File not found!
Closing file (if opened).
```

## **6. Raising Custom Exceptions (`raise`)**  
You can **manually raise exceptions** using `raise`.  

```python
age = int(input("Enter your age: "))

if age < 18:
    raise ValueError("You must be at least 18 years old!")
else:
    print("Access granted.")
```
✔️ **If input is `15`:**  
```
Traceback (most recent call last):
  File "script.py", line 4, in <module>
    raise ValueError("You must be at least 18 years old!")
ValueError: You must be at least 18 years old!
```


## **7. Creating Custom Exceptions**  
You can define **custom exception classes** using `class`.  

```python
class UnderageError(Exception):
    pass  # Custom exception

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise UnderageError("You are under 18!")
except UnderageError as e:
    print("Custom Exception:", e)
```
✔️ **Output (if age is `16`):**  
```
Custom Exception: You are under 18!
``` 
- **Exceptions prevent program crashes** and allow error handling.
-  Use `try-except` to **catch errors** and avoid program failures.
-  Use `else` to execute code **only if no exception occurs**.
-  Use`finally` to **clean up resources**, even if an error occurs.
-  You can **raise exceptions** manually with `raise`.  
- You can **create custom exceptions** using Python classes.  

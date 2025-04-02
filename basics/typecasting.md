### **Understanding Typecasting (Type Conversion) in Python**  

Typecasting is the process of **converting a value from one data type to another** (e.g., integer to string, float to integer, etc.).  

Python provides **two types** of type conversion:  
1. **Implicit Type Conversion (Automatic)** → Done by Python automatically.  
2. **Explicit Type Conversion (Manual)** → Done by the programmer using built-in functions.  

## **1. Implicit Type Conversion (Automatic Typecasting)**  
Python automatically **converts a smaller data type into a larger one** to prevent data loss.  

### **Example:**  
```python
num_int = 10  # Integer
num_float = 2.5  # Float

result = num_int + num_float  # Python converts num_int to float automatically

print(result)  # Output: 12.5
print(type(result))  # Output: <class 'float'>
```
✔️ **Explanation:**  
- `num_int` (integer) is converted to `float` automatically.  
- The result is a `float`, preventing data loss.  

### **Another Example:**  
```python
num = 5
result = num / 2  # Python automatically converts it to float
print(result)  # Output: 2.5
```


## **2. Explicit Type Conversion (Manual Typecasting)**  
When automatic conversion is not possible, **we use built-in functions** to change data types.  

🔹 Common typecasting functions:  
- `int()` → Converts to integer  
- `float()` → Converts to float  
- `str()` → Converts to string  
- `list()` → Converts to list  
- `tuple()` → Converts to tuple  
- `set()` → Converts to set  

---

### **Example 1: Converting `float` to `int`**  
```python
num_float = 9.8
num_int = int(num_float)  # Manually converting to integer

print(num_int)  # Output: 9
print(type(num_int))  # Output: <class 'int'>
```
✔️ **Note:** The decimal part (`.8`) is **removed**, not rounded.


### **Example 2: Converting `int` to `str`**  
```python
num = 100
num_str = str(num)  # Convert integer to string

print(num_str)  # Output: "100"
print(type(num_str))  # Output: <class 'str'>
```
✔️ **Use case:** This is useful for **string concatenation**.  

```python
age = 25
print("I am " + str(age) + " years old.")  # Correct

# print("I am " + age + " years old.")  # ❌ TypeError (Cannot concatenate str and int)
```

### **Example 3: Converting `str` to `int` or `float`**  
```python
num_str = "50"
num_int = int(num_str)  # Convert string to integer
num_float = float(num_str)  # Convert string to float

print(num_int + 10)  # Output: 60
print(num_float + 0.5)  # Output: 50.5
```
✔️ **Note:** The string must contain **only numbers**.  

```python
num_str = "50a"
num_int = int(num_str)  # ❌ ValueError: invalid literal for int()
```


### **Example 4: Converting `list` to `tuple` and vice versa**  
```python
my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # Convert list to tuple

print(my_tuple)  # Output: (1, 2, 3)

new_list = list(my_tuple)  # Convert tuple back to list
print(new_list)  # Output: [1, 2, 3]
```
  
- **Implicit conversion** is done automatically by Python when **no data loss occurs**.  
- **Explicit conversion** is done manually using **typecasting functions** like `int()`, `float()`, `str()`, etc.  
- Always ensure valid conversions (e.g., `"123"` can be converted to `int`, but `"abc"` cannot).  

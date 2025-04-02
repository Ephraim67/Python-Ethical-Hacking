### **Understanding Loops in Python**  

Loops are used to **repeat a block of code** multiple times, reducing redundancy and making programs more efficient.  

---

## **Types of Loops in Python**  
Python has **two main types** of loops:  
1. **`for` Loop** → Used when the number of iterations is known.  
2. **`while` Loop** → Used when the number of iterations is unknown and depends on a condition.  

Additionally, Python provides **loop control statements** like:  
- **`break`** → Exits the loop prematurely.  
- **`continue`** → Skips the current iteration and moves to the next.  
- **`pass`** → Acts as a placeholder.

---

## **1. The `for` Loop**  
The `for` loop is used for iterating over **sequences** (lists, tuples, dictionaries, strings, etc.).  

### **Syntax:**  
```python
for variable in sequence:
    # Code to execute
```

### **Example: Iterating Over a List**  
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```
✔️ **Output:**  
```
apple
banana
cherry
```

### **Example: Using `range()` in a `for` Loop**  
The `range(start, stop, step)` function generates numbers within a range.  

```python
for i in range(1, 6):  # Loops from 1 to 5
    print(i)
```
✔️ **Output:**  
```
1
2
3
4
5
```

---

## **2. The `while` Loop**  
A `while` loop **keeps running as long as a condition is True**.

### **Syntax:**  
```python
while condition:
    # Code to execute
```

### **Example: Counting from 1 to 5**  
```python
count = 1

while count <= 5:
    print(count)
    count += 1  # Increments count to avoid infinite loop
```
✔️ **Output:**  
```
1
2
3
4
5
```

---

## **3. Loop Control Statements**  

### **A. `break` Statement** (Exits the loop)  
```python
for num in range(1, 10):
    if num == 5:
        break  # Stops the loop when num reaches 5
    print(num)
```
✔️ **Output:**  
```
1
2
3
4
```

### **B. `continue` Statement** (Skips an iteration)  
```python
for num in range(1, 6):
    if num == 3:
        continue  # Skips when num is 3
    print(num)
```
✔️ **Output:**  
```
1
2
4
5
```

### **C. `pass` Statement** (Placeholder for future code)  
```python
for num in range(1, 6):
    if num == 3:
        pass  # Does nothing but avoids syntax errors
    print(num)
```
✔️ **Output:**  
```
1
2
3
4
5
```

---

## **4. Nested Loops**  
A **loop inside another loop** is called a nested loop.

### **Example: Printing a Pattern**  
```python
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"({i}, {j})", end=" ")
    print()  # New line after inner loop
```
✔️ **Output:**  
```
(1, 1) (1, 2) (1, 3) 
(2, 1) (2, 2) (2, 3) 
(3, 1) (3, 2) (3, 3)
```

---

## **5. Infinite Loops (Avoid These!)**  
If a `while` loop’s condition never becomes `False`, it runs **forever**.  
```python
while True:  # Infinite loop
    print("This will never stop!")
```
⚠️ **To stop an infinite loop, press `Ctrl + C` in the terminal.**


- Use a **`for` loop** when the number of iterations is **known**.  
- Use a **`while` loop** when the number of iterations is **unknown** and based on a condition.  
- Use **loop control statements** (`break`, `continue`, `pass`) to manage loop execution.  
- Avoid **infinite loops** unless intended.  

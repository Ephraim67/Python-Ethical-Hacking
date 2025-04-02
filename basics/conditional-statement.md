### **Understanding Conditional Statements in Python**  

Conditional statements allow a program to **make decisions** based on certain conditions. This is useful for executing different code depending on whether a condition is **true** or **false**.  

---

## **1. The `if` Statement**  
The `if` statement is used to execute a block of code only if a certain condition is met.  

### **Syntax:**  
```python
if condition:
    # Code block (runs if condition is True)
```

### **Example:**  
```python
age = 18

if age >= 18:
    print("You are eligible to vote.")  
```
✔️ **Output:**  
```
You are eligible to vote.
```
If `age` is less than 18, nothing happens because the condition is **False**.

---

## **2. The `if-else` Statement**  
The `else` block runs when the `if` condition is **False**.

### **Example:**  
```python
age = 16

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```
✔️ **Output:**  
```
You are not eligible to vote.
```

---

## **3. The `if-elif-else` Statement**  
The `elif` (short for "else if") allows checking multiple conditions. The first **True** condition executes, and the rest are skipped.

### **Example:**  
```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```
✔️ **Output:**  
```
Grade: B
```
Since `score` is 85, only the second condition (`score >= 80`) is True.

---

## **4. Nested `if` Statements**  
You can place `if` statements inside other `if` statements.

### **Example:**  
```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You can enter the club.")
    else:
        print("You need an ID to enter.")
else:
    print("You are too young to enter.")
```
✔️ **Output:**  
```
You can enter the club.
```

---

## **5. The `match-case` Statement (Python 3.10+)**  
The `match-case` statement is similar to `switch-case` in other languages. It simplifies multiple condition checks.

### **Example:**  
```python
day = "Monday"

match day:
    case "Monday":
        print("Start of the week!")
    case "Friday":
        print("Weekend is near!")
    case "Sunday":
        print("It's a holiday!")
    case _:
        print("Just another day.")
```
✔️ **Output:**  
```
Start of the week!
```
- `_` acts as a default case (like `else`).

---

## **6. Using Logical Operators in Conditions**  
Python allows combining multiple conditions using:  
- `and` → **Both conditions must be True**  
- `or` → **At least one condition must be True**  
- `not` → **Negates the condition**  

### **Example:**  
```python
temperature = 30
is_raining = False

if temperature > 25 and not is_raining:
    print("It's a good day for a walk!")
```
✔️ **Output:**  
```
It's a good day for a walk!
```

---

## **7. Ternary Conditional Operator (`if-else` in one line)**  
This is a **shorter way** to write an `if-else` statement.

### **Example:**  
```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
```
✔️ **Output:**  
```
Adult
```

---
  
- Conditional statements help make decisions in programs.  
- The `if-elif-else` structure allows multiple conditions.  
- The `match-case` statement is useful for matching specific values.  
- Logical operators (`and`, `or`, `not`) enhance condition checking.  
- A **ternary operator** allows writing concise conditions.  

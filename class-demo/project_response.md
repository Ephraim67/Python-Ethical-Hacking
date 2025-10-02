Here's a practical Python cybersecurity task that incorporates variables, strings, for loops, and functions:

## 🔐 Password Strength Analyzer

### Task Objective:
Create a program that analyzes password strength by checking for common security vulnerabilities.

### Concepts Used:
- **Variables** - Store password criteria
- **Strings** - Analyze password content
- **For Loop** - Iterate through password characters
- **Function** - Encapsulate the analysis logic

### Starter Code Template:

```python
def analyze_password_strength(password):
    """
    Analyze the strength of a password based on security criteria
    """
    # Variables to track password characteristics
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    length_ok = False
    
    # Special characters commonly used in passwords
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Check password length
    if len(password) >= 8:
        length_ok = True
    
    # For loop to check each character
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    
    # Calculate strength score
    strength_score = 0
    if length_ok:
        strength_score += 1
    if has_uppercase:
        strength_score += 1
    if has_lowercase:
        strength_score += 1
    if has_digit:
        strength_score += 1
    if has_special:
        strength_score += 1
    
    # Return analysis results
    return {
        'strength_score': strength_score,
        'length_ok': length_ok,
        'has_uppercase': has_uppercase,
        'has_lowercase': has_lowercase,
        'has_digit': has_digit,
        'has_special': has_special
    }

def display_results(password, analysis):
    """
    Display the password analysis results in a user-friendly format
    """
    print(f"\n🔐 Password Analysis for: {password}")
    print("=" * 40)
    
    # Display criteria check results
    criteria = {
        'Minimum 8 characters': analysis['length_ok'],
        'Contains uppercase letters': analysis['has_uppercase'],
        'Contains lowercase letters': analysis['has_lowercase'],
        'Contains numbers': analysis['has_digit'],
        'Contains special characters': analysis['has_special']
    }
    
    for criterion, met in criteria.items():
        status = "✅" if met else "❌"
        print(f"{status} {criterion}")
    
    # Strength rating
    score = analysis['strength_score']
    print(f"\nStrength Score: {score}/5")
    
    if score == 5:
        print("💪 Password Strength: EXCELLENT")
    elif score >= 3:
        print("👍 Password Strength: GOOD")
    elif score >= 2:
        print("⚠️ Password Strength: WEAK")
    else:
        print("🚨 Password Strength: VERY WEAK")

# Main program
def main():
    print("=== Password Strength Analyzer ===")
    print("A Cybersecurity Tool for Password Assessment")
    print("=" * 45)
    
    # Test multiple passwords using a for loop
    test_passwords = [
        "password",
        "123456",
        "Password123",
        "StrongPass!2024",
        "Abc123!@"
    ]
    
    print("\nTesting common passwords:")
    for pwd in test_passwords:
        analysis = analyze_password_strength(pwd)
        display_results(pwd, analysis)
    
    # Interactive mode
    print("\n" + "=" * 45)
    print("Interactive Mode - Test Your Own Password")
    
    while True:
        user_password = input("\nEnter a password to analyze (or 'quit' to exit): ")
        
        if user_password.lower() == 'quit':
            print("👋 Stay secure!")
            break
        
        analysis = analyze_password_strength(user_password)
        display_results(user_password, analysis)

# Run the program
if __name__ == "__main__":
    main()
```

### Learning Objectives:

1. **Variables**: Understand how to store and track multiple conditions
2. **Strings**: Learn string methods (`isupper()`, `islower()`, `isdigit()`) and membership testing
3. **For Loop**: Practice iterating through each character in a string
4. **Function**: Create reusable code blocks for specific tasks

### Extension Challenges:

1. **Add Common Password Check**:
```python
def is_common_password(password):
    common_passwords = ["password", "123456", "qwerty", "admin", "letmein"]
    return password.lower() in common_passwords
```

2. **Add Sequential Character Check**:
```python
def has_sequential_chars(password):
    for i in range(len(password) - 2):
        # Check for sequences like "abc", "123"
        if (ord(password[i+1]) - ord(password[i]) == 1 and 
            ord(password[i+2]) - ord(password[i+1]) == 1):
            return True
    return False
```

3. **Create Password Generator**:
```python
import random
import string

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))
```

### Real-World Cybersecurity Connection:
- This mimics how security systems evaluate password strength
- Teaches students about common password vulnerabilities
- Demonstrates why complex passwords are important for security

This task gives students practical experience while reinforcing fundamental programming concepts in a cybersecurity context!

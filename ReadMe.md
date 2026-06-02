# Python
##  This repository documents my journey of Intership

## 1. Topic: Variables and Data Types

In this section I learned:
- int
- float
- string
- boolean
- type() function
- type conversion


### Output of Variables_Datatypes.py:
Name: Aditya  
Age: 21  
Height: 5.8  
Is Student: True  
<class 'int'>    
<class 'float'>  
<class 'str'>  
<class 'bool'>  
60  

## 2. Topic:Input Output Statements:
### Output of input_output.py:
Enter your name: aditya  
Enter your age: 22  
Hello aditya  
You are 22 years old.  
Enter first number: 20  
Enter second number: 69  
Addition: 89  
Multiplication: 1380  

## 3. Topic : Operators:

### Output of operators.py
Addition: 13   
Subtraction: 7  
Multiplication: 30   
Division: 3.3333333333333335  
Floor Division: 3  
Modulus: 1  
Power: 1000  
Is a equal to b? False  
Is a not equal to b? True  
Is a greater than b? True  
Is a less than b? False  
AND: False  
OR: True  
NOT x: False  

## 4. Topic : Conditional statements

## output of conditional_statement.py
Iron man  
shakti man  
Enter your age: 1  
You are not eligible to vote.  
Enter your marks: 65  
Grade: C  
 
 ## 5. Topic Loops:

 # Python Loops

Loops are used to execute a block of code repeatedly.

## Types of Loops in Python

1. for loop
2. while loop

---

# for Loop

The `for` loop is used to iterate over a sequence.

## Syntax

```python
for variable in sequence:
    # code
```

## Example

```python
for i in range(5):
    print(i)
```

## Output

```text
0
1
2
3
4
```

---

# while Loop

The `while` loop executes as long as the condition is true.

## Syntax

```python
while condition:
    # code
```

## Example

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

## Output

```text
1
2
3
4
5
```

---

# Infinite Loop

A loop that never ends is called an infinite loop.

## Example

```python
while True:
    print("Hello")
```

---

# break Statement

Used to stop the loop immediately.

## Example

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

# continue Statement

Used to skip the current iteration.

## Example

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

# Nested Loops

A loop inside another loop is called a nested loop.

## Example

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```
6. Funtions:
# Python Functions

Functions are reusable blocks of code used to perform a specific task.

They help:
- reduce code repetition
- improve readability
- organize programs

---

# Creating a Function

## Syntax

```python
def function_name():
    # code
```

## Example

```python
def greet():
    print("Hello")
    
greet()
```

---

# Function with Parameters

Parameters allow values to be passed into functions.

## Example

```python
def greet(name):
    print("Hello", name)

greet("Aditya")
```

---

# Function with Return Value

The `return` statement sends a value back.

## Example

```python
def add(a, b):
    return a + b

result = add(5, 3)

print(result)
```

---

# Default Parameters

Default values can be assigned to parameters.

## Example

```python
def country(name="India"):
    print(name)

country()
country("USA")
```

---

# Keyword Arguments

Arguments can be passed using parameter names.

## Example

```python
def student(name, age):
    print(name, age)

student(age=21, name="Aditya")
```

---

# Arbitrary Arguments

`*args` allows multiple values.

## Example

```python
def numbers(*num):
    print(num)

numbers(1, 2, 3, 4)
```

---

# Recursive Function

A function calling itself is called recursion.

## Example

```python
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)
```


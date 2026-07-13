# 🐍 Python Learning Journey

Welcome to my Python learning repository! This project documents my journey during my internship, covering core concepts from fundamental syntax to advanced programming topics, Object-Oriented Programming (OOP), file operations, and database connectivity.

---

## 📂 Repository Index

Below is the organized directory structure of the repository. Click on any topic to view the implementation details, notebooks, or scripts.

| Category | Topics Covered | Key Concepts | Files |
| :--- | :--- | :--- | :--- |
| **01. Basics** | Variables, I/O, Operators, Strings | Data types, user inputs, formatting, slicing, string methods | 📁 [01_Basics](./01_Basics) |
| **02. Control Flow** | Conditions, Loops, Patterns | `if-elif-else`, `for`/`while` loops, break/continue, practice | 📁 [02_Control_Flow](./02_Control_Flow) |
| **03. Data Structures** | Lists, Tuples, Sets, Dictionaries | Mutability, indexing, set theory, key-value mappings | 📁 [03_Data_Structures](./03_Data_Structures) |
| **04. Functions** | Code Reusability | Parameters, return values, `*args`, keyword args, recursion | 📁 [04_Functions](./04_Functions) |
| **05. OOP** | Object-Oriented Programming | Classes, objects, inheritance, encapsulation, polymorphism | 📁 [05_Object_Oriented_Programming](./05_Object_Oriented_Programming) |
| **06. File & Errors** | Exception & File Handling | `try-except-finally`, file I/O, context managers (`with`) | 📁 [06_File_and_Exception_Handling](./06_File_and_Exception_Handling) |
| **07. Advanced** | Functional Programming & DB | Lambdas, Decorators, Generators, SQLite Database connectivity | 📁 [07_Advanced_Concepts](./07_Advanced_Concepts) |

---

## 📝 Topic Highlights & Executable Files

### 1. Basics
*   **[Variables & Data Types](./01_Basics/01_Variables_Datatypes.py)**: Introduction to `int`, `float`, `str`, `bool`, type checking with `type()`, and type conversion.
    <details>
    <summary>📄 View Console Output</summary>
    
    ```text
    Name: Aditya  
    Age: 21  
    Height: 5.8  
    Is Student: True  
    <class 'int'>    
    <class 'float'>  
    <class 'str'>  
    <class 'bool'>  
    60  
    ```
    </details>

*   **[Input & Output Statements](./01_Basics/02_Input_Output.py)**: Reading inputs from users and formatting print statements.
    <details>
    <summary>📄 View Console Output</summary>
    
    ```text
    Enter your name: aditya  
    Enter your age: 22  
    Hello aditya  
    You are 22 years old.  
    Enter first number: 20  
    Enter second number: 69  
    Addition: 89  
    Multiplication: 1380  
    ```
    </details>

*   **[Operators](./01_Basics/03_Operators.py)**: Arithmetic, comparison, and logical operators.
    <details>
    <summary>📄 View Console Output</summary>
    
    ```text
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
    ```
    </details>

*   **[Strings & Methods](./01_Basics/04_Strings.ipynb)**: Immutability, slicing, string interpolation (f-strings), and methods like `upper()`, `lower()`, `strip()`, `split()`, `join()`.

---

### 2. Control Flow & Loops
*   **[Conditional Statements](./02_Control_Flow/01_Conditional_Statements.py)**: `if`, `else`, and `elif` decision making.
    <details>
    <summary>📄 View Console Output</summary>
    
    ```text
    Iron man  
    shakti man  
    Enter your age: 1  
    You are not eligible to vote.  
    Enter your marks: 65  
    Grade: C  
    ```
    </details>
    
*   **[Loops](./02_Control_Flow/02_Loops.ipynb)**: Iterating with `for` and `while` loops, infinite loops, and controlling loops with `break` and `continue`.
*   **[Pattern Programs](./02_Control_Flow/03_Pattern_Programs.ipynb)**: Matrix pattern output, right-angled star patterns, and numerical patterns.
*   **[Practice Exercises](./02_Control_Flow/04_Practice.py)**: Multi-level coding practice covering easy, medium, and hard decision-making problems (e.g., Leap Year, ATM Withdrawal, Password Strength Checker, Electricity Bill).

---

### 3. Data Structures
*   **[Lists](./03_Data_Structures/01_Lists.ipynb)**: Mutability, negative indexing, slicing, inserting/removing items, sorting, and List Comprehensions.
*   **[Tuples](./03_Data_Structures/02_Tuples.ipynb)**: Immutable sequences, single-element tuples, packing, and unpacking.
*   **[Sets](./03_Data_Structures/03_Sets.ipynb)**: Unordered unique collections, adding/removing items, set operations (union, intersection, difference, symmetric difference).
*   **[Dictionaries](./03_Data_Structures/04_Dictionaries.ipynb)**: Key-value stores, accessing items safely using `.get()`, pop operations, and dictionaries iteration.

---

### 4. Functions
*   **[Functions](./04_Functions/01_Functions.ipynb)**: Defining functions with `def`, arguments, keyword args, default parameters, arbitrary args (`*args`), and recursive functions.

---

### 5. Object-Oriented Programming (OOP)
*   **[Classes & Objects](./05_Object_Oriented_Programming/01_Classes_and_Objects.ipynb)**: Class blueprints, constructors (`__init__`), instance variables, methods, and `__str__` method.
*   **[Inheritance](./05_Object_Oriented_Programming/02_Inheritance.ipynb)**: Extending classes using Single, Multilevel, and Multiple inheritance, method overriding, and calling `super()`.
*   **[Encapsulation & Polymorphism](./05_Object_Oriented_Programming/03_Encapsulation_Polymorphism.ipynb)**: Public, protected, and private access specifiers (`__variable`), getter/setter methods, duck typing, and polymorphism.

---

### 6. File & Exception Handling
*   **[Exception Handling](./06_File_and_Exception_Handling/01_Exception_Handling.ipynb)**: Catching runtime errors using `try`, `except`, `else`, `finally`, and writing custom exceptions.
*   **[File Handling](./06_File_and_Exception_Handling/02_File_Handling.ipynb)**: Reading, writing, and appending files using `open()` and context managers (`with` statement).

---

### 7. Advanced Concepts
*   **[Advanced Concepts](./07_Advanced_Concepts/01_Advanced_Concepts.ipynb)**: Lambda functions, `map()`, `filter()`, `reduce()`, Custom Decorators, and Generators (`yield`).
*   **[Database Connectivity](./07_Advanced_Concepts/02_Database_Connectivity.ipynb)**: Integrating Python with SQL using built-in SQLite (`sqlite3` module). Establishing database connections, execution of CRUD query statements, secure parameterization, and transaction commits.

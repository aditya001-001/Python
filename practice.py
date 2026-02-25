# Conditional Statement Practice:
#🟢 LEVEL 1 — EASY
#1️⃣ Check if a number is positive.
#Input: 5
#Output: Positive
'''n=int(input("Enter a number:"))
if n>0:
    print("Positive")'''



#2️⃣ Check if a number is divisible by 5.
'''num=int(input("Enter a number:"))
if num%5==0:
    print("It is divisible by 5")'''


#3️⃣ Check if a number is even or odd.
'''number=int(input("Enter a number:"))
if number%2==0:
    print("Even")
else:
    print("odd")'''



#4️⃣ Take age as input.

#Print:
#"Child" if age < 13
#"Teen" if age between 13–19
#"Adult" otherwise
'''age=int(input("Enter age:"))
if age < 13:
    print("Child")
elif age>=13 and age<=19:
    print("Teen")
else:
    print("Adult")'''

#5️⃣ Take a number.
#Print:
#"Small" if less than 10
#"Medium" if between 10 and 50
#"Large" if greater than 50
'''num=int(input("Enter a Number:" ))
if num<10:
    print("Small")
elif num<50 and num>=10:
    print("Medium")
else:
    print("Large")'''

#  LEVEL 2 — MEDIUM
# 6️⃣ Largest of Two Numbers
# Take two numbers and print the largest.
'''num1=int(input("Enter a number1:"))
num2=int(input("Enter a number2:"))
if num1>num2:
    print("NUM 1 is Larger")
else:
    print("NUM 2 is Larger")'''


# 7️⃣ Largest of Three Numbers
# (Without using max())
'''num1=int(input("Number 1:"))
num2=int(input("Number 2:"))
num3=int(input("Number 3:"))
if num1>num2:
    if num1>num3:
        print("Number 1  is larger-that is  {}".format(num1))
    else:
        print("Number 3 is larger-that is {}".format(num3))
elif num2>num3:
    print("Number 2 is larger-that is {}".format(num2))
else:
    print("Number 3 is larger-that is  {}".format(num3))'''
# 8️⃣ Check Leap Year
# Rules:
# Divisible by 4
# But not divisible by 100
# Except if divisible by 400
# Example:
# 2000 → Leap
# 1900 → Not Leap
year=int(input("Enter the year:"))
if (year%4==0 or year%100!=0) and (year%400==0):
    print("Leap Year")
else:
    print("Not Leap year")

# 9️⃣ Simple Calculator
# Take:
# Number 1
# Number 2
# Operator (+, -, *, /)
# Perform calculation based on operator.

# 🔟 Check Voting Eligibility
# Input:
# Age
# Citizenship (True/False)
# Eligible only if:
# Age >= 18
# Citizenship is True



# 🔴 LEVEL 3 — HARD
# 1️⃣1️⃣ ATM Withdrawal Logic
# Take:
# Account balance
# Withdrawal amount
# Conditions:
# Withdrawal amount must be multiple of 100
# Withdrawal amount <= balance
# Print:
# "Transaction Successful"
# Or proper error message


# 1️⃣2️⃣ Student Result System
# Take:
# Marks in 5 subjects
# Conditions:
# If any subject < 35 → Fail
# If average >= 75 → Distinction
# If average >= 60 → First Class
# If average >= 50 → Second Class
# Else Pass

# 1️⃣3️⃣ Password Strength Checker
# Take password as input.
# Check:
# Length >= 8
# Contains at least one number
# Contains at least one uppercase letter
# Print:
# Strong Password
# Weak Password

# 1️⃣4️⃣ Electricity Bill Calculation
# Units:
# First 100 units → ₹5 per unit
# Next 100 units → ₹7 per unit
# Above 200 → ₹10 per unit
# Calculate total bill.


# 1️⃣5️⃣ Triangle Type Checker
# Take three sides.
# Check:
# Valid triangle first
# Equilateral
# Isosceles
# Scalene

# 🔥 REAL INTERVIEW LEVEL (Optional Challenge)
# 1️⃣6️⃣ Number Guess Validator
# Take:
# Secret number = 25
# User guess
# If guess:
# Within ±5 → "Very Close"
# Exact → "Correct!"
# Otherwise → "Try Again"
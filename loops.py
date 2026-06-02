# for loop example
print("For Loop")

for i in range(5):
    print(i)

# while loop example
print("\nWhile Loop")

i = 1

while i <= 5:
    print(i)
    i += 1

# break statement
print("\nBreak Statement")

for i in range(10):
    if i == 5:
        break
    print(i)

# continue statement
print("\nContinue Statement")

for i in range(5):
    if i == 2:
        continue
    print(i)

# nested loop
print("\nNested Loop")

for i in range(3):
    for j in range(2):
        print(i, j)
#Write a program that asks the user to enter a sequence of "non-decreasing" numbers one at a time. Numbers are non-decreasing if each number is greater than or equal to the last.


print("Enter a sequence of non-decreasing numbers.")

length = 0
prev = None

while True:
    num = float(input("Enter num: "))
    if prev is not None and num < prev:
        break
    length += 1
    prev = num

print("Thanks for playing!")
print(f"Sequence length: {length}")

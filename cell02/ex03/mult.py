n1 = int(input("Enter the first number:\n"))
n2 = int(input("Enter the second number:\n"))

num = n1 * n2
print(f"{n1} x {n2} = {num}")

if num == 0:
    print("This number is both positive and negative.")
elif num > 0:
    print("This number is positive.")
else:
    print("This number is negative")

# This program calcalates the factors of the given numbe .
n = int(input("Enter a number : "))
product = 1
for i in range(1, n + 1):
    product = product * i

print(f"The factor of the number {n} is {product}")

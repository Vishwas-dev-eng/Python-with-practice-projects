"""
Factorial of 1 to 5 :
    0 = 1 ---> by  defualt the factorial of 0 is 1

    1 = 1 ----> by defualt the factorial of 1 is 1
    2 = 2 X 1
    3 = 3 X 2 X 1
    4 = 4 X 3 X 2 X 1
    5 = 5 X 4 X 3 X 2 X 1

    So our formula is :
    factorial(n) : - n X factorial(n-1)

"""

# This is  a program that finds out the facotorial of entered number : 
def factorial(n):
    if n == 1 or n == 0:
        return 1

    return n * factorial(n - 1)


n = int(input("Enter the number to calucate the factorial of the number : "))

print("The factorial of the number is : ", factorial(n))

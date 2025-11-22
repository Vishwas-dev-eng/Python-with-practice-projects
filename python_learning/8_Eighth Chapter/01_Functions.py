# The python language have functions for the ease of use : 

a  = int(input("Enter a number to calculate the average of the numbers : "))
b  = int(input("Enter a number to calculate the average of the numbers : "))
c  = int(input("Enter a number to calculate the average of the numbers : "))

print(f"The average of the number is  {(a+b+c)/3}")

# To smaller the size of the program to do the same thing 50 times there are FUNCTIONS : 

def avg():  # This is called defination of the funcition .
    a  = int(input("Enter a number to calculate the average of the numbers : "))
    b  = int(input("Enter a number to calculate the average of the numbers : "))
    c  = int(input("Enter a number to calculate the average of the numbers : "))

    print(f"The average of the number is  {(a+b+c)/3}")

avg() # This is called the calling of the function . 


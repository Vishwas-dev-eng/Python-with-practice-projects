# This problem is little bit complicated but not impossible :
# Here we have to print a star pyramid based on the user input :

"""
for n = 3
output :
  *
 ***
*****

"""
"""
for n = 5 
output : 
    * 
   ***
  *****
 *******
*********

"""
n = int(input("Enter a number  to start a draw a pyramid : "))
for i in range(1, n + 1):
    print(" " * (n - 1), end="")
    print("*" * (2 * i - 1), end="")
    print("")

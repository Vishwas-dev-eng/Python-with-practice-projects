def game(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    else : 
        return c 
    #


a = int(input(" Enter the numbers to check which is the greater : "))
b = int(input(" Enter the numbers to check which is the greater : "))
c = int(input(" Enter the numbers to check which is the greater : "))

print("The greater numbers are  : " , game(a , b , c ))

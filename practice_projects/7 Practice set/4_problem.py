
n = int(input("Enter a number : "))
 
for i in range ( 1 , n) : 
    if(n%2) == 0 :
        print("The number entered is not prime . ")
    break # break is necessary here as if not the value entered will be the loop run's if it will cause the statement again and again
else:
    print("The number is prime . ")

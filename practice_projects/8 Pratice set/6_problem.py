def converter(i):
    inch = 2.54
    c = inch * i
    return c


i = float(input("Enter a number to calculate the cm  : "))
print(f"The value of inch in centimetre is  : {converter(i)} ")

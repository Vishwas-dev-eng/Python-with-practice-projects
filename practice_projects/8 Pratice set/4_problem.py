"""
This problem is to calculate the sumo  of the n natural numbers :

1 = 1
2 = 1 + 2
3 = 1 + 2 + 3
4 = 1 + 2 + 3 + 4
5 = 1 + 2 + 3 + 4 + 5


"""


def sum(n):
    if n == 1:
        return 1

    return sum(n - 1) + n


n = int(input("Enter the number to calucate the sum ofthe natural number : "))
a = sum(n)
print(f" The sum of the entered number is :  {a} ")

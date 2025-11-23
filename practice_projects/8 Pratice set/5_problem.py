def pyramid(n):
    if n == 0:
        return
    print("*" * n)
    pyramid(n - 1)


n = int(input("Enter a number : "))
pyramid(n)

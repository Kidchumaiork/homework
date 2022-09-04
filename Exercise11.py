n = int(input("Number: "))
for x in range(n):
    text2 = " " * (n - x)
    print(text2, "*" + "*" * (x*2))

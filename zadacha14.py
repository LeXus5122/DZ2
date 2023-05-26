def powersoftwo(N):
    k = 0
    while 2**k <= N:
        print(2**k)
        k += 1

N = int(input("Введите число: "))
powersoftwo(N)

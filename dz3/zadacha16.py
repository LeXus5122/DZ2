def count():
    N = int(input("Введите количество элементов в массиве: "))
    A = list(range(1, N+1)) 
    print("Список A: ", A)
    X = int(input("Введите число X: "))
    return A.count(X)

print(count())

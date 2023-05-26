def closest_number():
    N = int(input("Введите количество элементов в массиве: "))
    A = list(range(1, N+1))  
    print("Список A: ", A)
    X = int(input("Введите число X: "))
    return min(A, key=lambda num: abs(num-X))

print(closest_number())

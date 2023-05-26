def find_numbers(S, P):
    for x in range(1, 1001):
        for y in range(x, 1001):  
            if x + y == S and x * y == P:
                return x, y
    return None 

S = int(input("Введите сумму: "))
P = int(input("Введите произведение: "))
numbers = find_numbers(S, P)
if numbers is not None:
    print("Искомые цифры: ", numbers)
else:
    print("Не найдено")

# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 
def get_power(A,B):
    if B == 0:
        return 1
    # elif B % 2 == 0:
    #     return get_power(A,B//2)**2
    # else:
    return A*get_power(A,B-1)
A = int(input("Введите число А: "))
B = int(input("Введите степень В: "))
print(get_power(A,B))
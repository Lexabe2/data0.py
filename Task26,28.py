# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

number = int(input("Введите целое число: "))
degree = int(input("Введите степень числа: "))

def funk(number: int, degree: int) -> int:
    if degree == 0:
        return 1
    else:
        return number * funk(number, degree - 1)
print(funk(number, degree))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
def funk(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return a + funk(a, b - 1)

print(funk(2, 2))

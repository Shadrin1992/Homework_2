# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

print('Введите число: ')
num = input()
res_num = num.replace('.','')
def sum_digits(s):
    return sum(map(int, s))

print(sum_digits(res_num))

# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

print('Введите число: ')
num = int(input())

def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")

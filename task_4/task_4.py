# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)

print('Введите число: ')
n = int(input())
list=[]
for i in range(-n,n+1):
    list.append(i)
print(list)

f = open('C:\\Users\\user\\Desktop\\Python Homework\\Homework_2\\task_4\\file.txt').read().split('\n')
l = [line.strip() for line in f]
result = [int(item) for item in l]

multip = list[result[0]]*list[result[1]]*list[result[2]]
print('Произведение числел на позициях: ',multip)

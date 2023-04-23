import random

count = 0
num1, num2 = 1, 100
enter = 0

while enter != 'y':
    count += 1
    number = random.randint(num1, num2)
    print(number)
    enter = input("Угадал 'y', больше '>', меньше '<': ")

    if enter == '<':
        num2 = number-1
    elif enter == '>':
        num1 = number + 1

input('\n\nТак просто...Всего ' + str(count) + ' попыток: )))) \n\n' + 't\t' + str(number)) 





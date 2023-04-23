# Напишите программу "Генератор персонажей" для ролевой игры. Пользователю должно быть предоставлено 30 пунктов,
# которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость.
# Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда
# из характеристик, которым он решит присвоить другие значения.

choice = None
power = []
hp = []
mud = []
lovk = []
score = None
punkt = 30

while choice != "0":
    print(
        '''
        "Калькулятор характеристик"

        0 - Выйти
        1 - Добавить очки
        2 - Забрать очки
        3 - Посмотреть
        '''
    )
    choice = input("Ваш выбор: ")
    if choice == "0":
        print("До встречи, герой!")
    elif choice == "1":
        print(

            "\n\t\tХарактеристики: \tу вас осталось", 
            punkt, "очков"
            "\n\t\t1-Сила"
            "\n\t\t2-Здоровье"
            "\n\t\t3-Мудрость"
            "\n\t\t4-Ловкость"

        )

        choice = input("Ваш выбор:")

        if choice == "1":
            score = int(input("Сколько вы хотите вложить очков:"))
            
            power.append(score)
            print("Очков вложенных в силу", sum(power))
            print("Вы вложили:", score, "очков")
            punkt -= score
            print("У вас осталось: ", punkt, "очков")

        if choice == "2":
            score = int(input("Сколько вы хотите вложить очков:"))

            hp.append(score)
            print("Очков, вложенных в Здоровье", sum(hp))
            print("Вы вложили:", score, "очков")
            punkt -= score
            print("У вас осталось:", punkt, "очков")

        if choice == "3":
            score = int(input("Сколько вы хотите вложить очков:"))

            mud.append(score)
            print("Очков вложенных в Здоровье", sum(mud))
            print("Вы вложили:", score, "очков")
            punkt -= score
            print("У вас осталось:", punkt, "очков")

        if choice == "4":
            score = int(input("Сколько вы хотите вложить очков: "))
            lovk.append(score)
            print("Очков вложенных в Здоровье", sum(lovk))
            print("Вы вложили:", score, "очков")
            punkt -= score
            print("У вас осталось:", punkt, "очков")
    elif choice == "2":
        print(
            '''
            С какой характеристики вы хотите забрать: 
            1-Сила
            2-Здоровье
            3-Мудрость
            4-Ловкость
            '''
                )

        choice = input("Ваш выбор: ")
        if choice == "1":
            score = int(input("Сколько вы хотите забрать очков:"))

            power[0] -= score
            print("Осталось очков Силы:", power)
            print("Очков забрано у Силы:", score)
            punkt += score
            print("У вас осталось:", punkt, "очков")
        if choice == "2":
            score = int(input("Сколько вы хотите забрать очков:"))

            hp[0] -= score
            print("Осталось очков силы:", hp)
            print("Очков забрано у Силы:", score)
            punkt += score
            print("У вас осталось:", hp, "очков")
        if choice == "3":
            score = int(input("Сколько вы хотите забрать очков:"))

            mud[0] -= score
            print("Осталось очков силы:", mud)
            print("Очков забрано у Силы:", score)
            punkt += score
            print("У вас осталось:", mud, "очков")
        if choice == "4":
            score = int(input("Сколько вы хотите забрать очков:"))

            lovk[0] -= score
            print("Осталось очков силы:", lovk)
            print("Очков забрано у Силы:", score)
            punkt += score
            print("У вас осталось:", lovk, "очков")
        elif choice == "3":
            print("Сила:", sum(power))
            print("Здоровье", sum(hp))
            print("Мудрость", sum(mud))
            print("Ловкость", sum(lovk))
        else:
            print("Извините, в меню нет пункта", choice)
input("Нажмите Enter")


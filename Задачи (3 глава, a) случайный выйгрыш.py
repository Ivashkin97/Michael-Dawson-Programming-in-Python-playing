# Игра "Симулятор пирожка с 'сюрпризом'"

import random
print("При запуске программа отображает один из пяти различных 'сюрпризов', выбранный случайным образом.")
print("Итак, ваш сюрприз...")
prize = random.randint(1, 5)
if prize == 1:
    #без выйгрыша
    print( \
    """ вы выйграли 0 рублей!!! """)
elif prize == 2:
    # 20.000 рублей
    print( \
    """ вы выйграли 20.000 рублей!!!""")

elif prize == 3:
    # 40.000 рублей
    print( \
    """ вы выйграли 40.000 рублей!!!""")

elif prize == 4:
    # 60.000 рублей
    print( \
    """ вы выйграли 60.000 рублей!!!""")

elif prize == 5:
    # 80.000 рублей
    print( \
    """ вы выйграли 80.000 рублей!!!""")

else:
    print("Аппарат сломан! (Должно быть, вы не выйграли.)")
print("...Но это только сегодня. ")

input("\n\nPress the enter key to exit.")
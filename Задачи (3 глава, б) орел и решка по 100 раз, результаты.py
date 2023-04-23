# Игра 'подбрасывает' условную монету 100 раз и сообщает, сколько раз выпал орел, а сколько - решка.
import random
tries = 0
eagle = 0
tail = 0

while tries < 100:
    coin = random.randint(0,1)
    tries += 1
    if coin > 0:
        eagle +=1
    elif coin < 1:
        tail +=1
print(f"Монета подброшена {tries} раз")
print(f"Орел {eagle}")
print(f"Решка {tail}")
input("\n\nPress the enter key to exit.")

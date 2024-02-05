import random
dictionary = ("перепічка", "завіт", "відбиток", "примха", "протиріччя", "перевірка", "закон", "професія", "безпека", "підсумок", "привітання", "проект", "перемога", "принцип", "проблема", "перевага", "захист", "процес", "передача", "пропозиція", "перетворення", "заклад", "профіль", "безлад", "підтримка", "процент", "передмова", "закінчення", "професор", "безумовно")


letter = []
world = []
result = []
world = list (random.choice(dictionary))
temp = []
test = world
count = 0
used = []

for i in range(len(world)):
    result.append(world[i])
    result[i] = "*"
    
print("Ви вгалуєте слово -", result)
while result != test:
    used = list(used)
    state = 0
    count += 1
    letter = str(input("Для того щоб почати грати введіть букву "))
    if  letter[0] in used:
        print("Ви вже пробували дану літеру")
        print("---------------------------------------------------")
        continue
    for i in range(len(world)):
        if world[i] == letter[0]:
            state = 1   
            result[i] = letter[0]
            temp.append(i)
    if state == 1 :
        print("Ви вгадати літеру! Поточне солов -",result)
    else:
        print("Немає даної літери. Поточне слово -", result)
        print("---------------------------------------------------")
    used.append(letter)
    print("Кількість спроб -", count)
    used.append(letter)
    used = set(used)
    print("Використані літери :", used)
    print("---------------------------------------------------")

print("Вітаю! Ви вгадали слово -", world, " за ", count, "спроб")
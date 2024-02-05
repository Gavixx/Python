import numpy as np
number = int(input("Введіть порогове значення "))
arr = np.random.randint(1,100,100)
print("arr - ", arr)
print("number - ", number)
temp = []
for i in arr:
    if i > number:
        temp.append(i)
print(temp)
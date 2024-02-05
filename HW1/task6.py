import random
n = int(input("Введіть номер за журналом (n) = "))
m = int(input("Введіть номер за групи (m) = "))
a = (n*m)+100
text1 = []
text2 = [i for i in range(1,8)]
for i in range(a):
    text1.append((random.randint(1, 8)))
# print(f" text1 - {text1}, len - {len(text1)}")
dict1 = {v:k for k,v in enumerate(text1)}
sorted_dict1 = dict(sorted(dict1.items()))

print(f" dictionary - {sorted_dict1}")
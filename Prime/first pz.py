a = int(input("Input number "))
temp = [1]
state = 0
for i in range(2, a):
    if a % i == 0:
        state = 1
        temp.append(i)
if state == 0:
    print("Proste")
else:
    print("Sckladne")
    print(temp)
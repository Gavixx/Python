number = int(input("Введіть число "))
result = 1
for i in range(1, number + 1):
    result *= i
    
print("result = ", result)
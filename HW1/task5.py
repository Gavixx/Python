import random
def Calculation(n):
    avg = 0
    for i in range(n):
        avg +=  numbers[i]
        
    avg /= n
    return avg

n =24* 4
numbers = []
for i in range(n):
    numbers.append(random.randint(1, 1000))
    
print('Середнє арифметичне = ',round(Calculation(n), 3))

def Calculating(num1, num2, operator):
    result = 0
    if operator == '+':
        result = num1 + num2
        return result
    
    if operator == '-':
        result = num1 - num2
        return result
    
    if operator == '*':
        result = num1 * num2
        return result
    
    if operator == '/':
        result = num1 / num2
        return result
    
    if operator == '%':
        result = num1 % num2
        return result
state = 0
while state != 1:
    num1 = float(input("Введіть перше значення(використовувати '.') "))
    operator = input("Введіть оператор('+','-','*','/','%') ")
    num2 = float(input("Введіть друге значення(використовувати '.') "))
    if num2 != 0:
        print("Результат ", num1, operator, num2, " = ", round(Calculating(num1,num2,operator), 3))
    else:
        "На 0 ділити не можна"
    state = input("\nДля продовження введіть 1, для виходу введіть 0 ")
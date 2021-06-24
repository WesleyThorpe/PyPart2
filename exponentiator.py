def exponentiate(num1,num2):
    '''takes two integers and raises the first to the power of the second'''
    return num1**num2

def raised_to_fourth_power(num3):
    '''raise the given paremeter to the 4th power'''
    return exponentiate(num3,4)

square = lambda x: exponentiate(x,2)
result= square(2)

cube = lambda x: exponentiate(x,3)
result2= cube(2)

result3= raised_to_fourth_power(2)

print(result)
print(result2)
print(result3)


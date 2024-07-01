import random

a=random.randint(1, 100)

print ('Добро пожаловать в числовую угадайку')
print ('Угадай моё число от 1 до 100, дружок)))))')

def is_valid(o):
    if o in range (1,101):
        return True
    else:
        return False
otvet=int(input())
while not otvet==a:
    if is_valid(otvet)==False:
        print ('От 1 до 100 говорю тебе...')
        otvet=int(input())

    if otvet>a:
        print ('Многовато')
        otvet=int(input())
    elif otvet<a:
        print ("Малоооооо")
        otvet=int(input())
if otvet==a:
    print ('К Р А С U В О')
    

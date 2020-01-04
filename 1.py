"""

s= 'hello \'my\' world'
print(s, end='\n') #метод для print переводит на новую строку
print(s, end='')

   

n1 = 2
n2 = 3

if n1 > n2 :
    print('bigger')
elif n1 < n2:
    print('less')
else:
    print('=')




if n == 1
    pass
else:
    pass #пустышка код будет работать



#угадай число
import random
num = random.randrange(1, 11)

while True:
    answer = input('Input number ')
    if not answer.isdigit(): #провека что с строке все цифры
        print('put a number')
        continue
    
    answer = int(answer)
    if answer > num:
        print('less')
    elif answer < num:
        print('bigger')
    else:
        print('done')
        break
    
#пропустить итерацию закончиить цикл        
i = 0
while i<5:
    i += 1
    if i==3:
        continue #пропуск итерации
    print(i)



#угадай что результат сложения
import random

n1 = random.randrange(1, 11)
n2 = random.randrange(1, 11)

while True: 
    answer = input(f'{n1} plus {n2} = ')
    test = answer.replace('.', '', 1)
    if not test.isdigit(): #провека что с строке все цифры
        print('not a number')
    else:
        break
    
if answer == test:
    answer = int(answer)
else:
    answer = floor(answer)
        
if answer == n1+n2:
    print('yes!')
else:
    print('no!')
"""









        




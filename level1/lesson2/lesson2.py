
"""
r = range(10)
print(r[2]) #вывод конкретного числа
list(r)
print(type(r)) #


for i in range(1, 11): #1 до 10
    print(i)
    

for i in ['a', 'b', 'c']:   #список
    print(i)

l = [1,2,3,4,5]
l.append(6) #добавление числа в список
print(l)
print(l[2])  #вывод конкретного числа в списке
l[2] = 33
print(l) #новое значение индекса 2
print(len(l)) #вовращает количество элементов
print(len(r))


a = 'abc'
for i in [a]:   #вывод кадого элмента строки
    print(i)
    print(i[0]) #вывод первой буквы
    

l = [1,2,3]
l[0] = 10 #список изменить можно
s = 'abc'
#s[0] = 'z' строка не изменяема. можно получить только копию
s2 = s
s.upper() #при этом создается новая ясейка памяти ABC, при этом abc осталась 
l = list('abc') # спосок в последовательность
print(l)
l2 = l
l2[0] = 'z'
print(l2) #происходит замена в первичной переменной
d = l2.pop() #извлечение элемента из списка(по умолчанию последний)
a = l2.pop(0) #извлечение конретого значения
l =[3,6,5,2,8,4]
l.sort(reverse=True); #сортировка + реверс
print(l)

#кортеж tuple не изменяемый
t =(1, 2, 3)
a = 1; b = 2
a, b = b, a #смена значений
a, b, c = 1, 2, 3 #неявные кортежи


l = [1,2,3]
l3 = l #l3=l
l2 = l.copy()#а это уже копия
s = {1, 4, 3, 6, 3, 6} # множество одно знанчение встеается только один раз
l = [1, 7, 8, 6, 7, 4, 3, 9, 9, 5, 6, 6, 1]#как получить список уникальных значений?
s = set(i)
l = list(s)


#dictionary
d = {'a': 100, 'b': 200, 'c': 300}
d['b'] = 400 #изменяем
d['x'] = 500 #добавляем
print(d['b'])
print('y' in d)
print(d.get('y',  0)) #методы проверки наличия значения
for k, v in d.items(): #ключ - значение
    print(k, v)
print(d.values()) #все значения
print(d.keys()) #все ключи


l = [1,2,3,4,5,6,7,8,9]
l[5] #тотечное обращение
l[5:] #[6, 7, 8]
print(l[:5]) #[1,2,3,4,5]
print(l[2:6]) #[3, 4, 5, 6]

3 in l
30 not in l #методы проверки наличия значения

l[;] #копия списка

#генерация списка
l = [i**2 for i in [2, 3, 4] if i>2]
#====
#for i in [2, 3, 4]: #
    #if i>2:
#    l.append(i**2)

#switch
hello = {
    'ru': 'Добрый день',
    'en': 'Good day',
    'de': 'Guten tag',
    'dk': 'God dag',
    'default': 'Unknown language'
    }
s = input('Введите код: ')
greet = hello.get(s, hello['default'])
print(greet)


#functions
def seconds_per_day(days = 1):
    s = 24 * days * 60 * 60
    return s
sec = seconds_per_day(5)
print(sec)

def area_of_disk(radius):
    return 3.14 * radius ** 2

def area_of-ring(outer, inner):
    return area_of_disk(outer) - area_of_disk(inner)


x = 10 #global value
def fn():
    global x
    print(x)
    x = 20  #local value
    print(x)
    
print(x)
fn()
print(x)
    
def fn():
    global account
    account = 0

account = 100
fn()
print(account) #wrong

def fn():
    return 0

account = 100
account = fn()
print(account) #right

#явное присваивание значений в функции
def fb(a, b =2, c = 3):
    pass

fn(10, c = 20)
#or fn(c = 10, a = 20) здесь не обязателен порядок



def fn(*params): #вывод всех значений 
    for p in params:
        print(p)
    print(type(params))


fn(1,2,3,4,5)  #class tuple - кортеж

def fn(**params): #вывод всех значений 
    for p, m in params.items():
        print(p, m)
    print(type(params))


fn(John=100, Mike=200, Pete=300)  #class dict - словарь


def area_of_disk(radius): #создание документации
    '''Help on function

        area_of_disk(number) -> number
        Return area of disk by radius
    '''
    return 3.14 * radius ** 2

print(help(area_of_disk))
 

#функционал библиотеки
import math
print(dir(math))
print(help(math.gcd))


#импорт нужных функций
from math import cos, sin
print(cos(2))

from math import cos as math_cos
print(math_cos(2))

import random
import string
print(dir(string)) 
print(help(random.choice))


import numpy
#pip install numpy/uninstall
nump.tan(3)
numpy.product([2,2,5,6])

jupyter notebook
http://localhost:8888/tree
"""
def seconds_per_day(days = 1):
    s = 24 * days * 60 * 60
    return s

if __name__ == '__main__':
    sec = seconds_per_day(5)
    print(sec)

def area_of_disk(radius):
    return 3.14 * radius ** 2

def area_of_ring(outer, inner):
    return area_of_disk(outer) - area_of_disk(inner)
    
#import funcs  //пподключение файла в тойже папке
#print(dir(funcs))
#import sys //подлючение директорий
#sys.path





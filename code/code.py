#!/usr/bin/env python3

'''
import time
from SimpleThread import Thread

@Thread()
def funct1():
    while True:
        time.sleep(1)
        print('hello from funct1')
    
@Thread()
def funct1():
    while True:
        time.sleep(1)
        print('hello from funct2')

while True:
    time.sleep(1)
        
'''
'''
import time

def perform(func):
    print(n)
    def inner(*argv, **kwargv):        
        stime = time.time()
        fpar = func(*argv, **kwargv)
        dtime = time.time() - stime
        print('time passed: ', dtime)
        return fpar
    return inner

@perform
def factorial(maximal):
    m = 1
    for n in range(1,maximal):
        m *= n
    return m


for n in range(2):
    result = factorial(10**n)
    print(result)
        
factorial = perform(factorial)
'''

import time
# PythonDecorators/my_decorator.py
class TimeDelta(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print(self.a, self.b, self.c)
        
    def __call__(self, f):

        def closure(*argv, **kwargv):
            print('Power of {} by {}'.format(argv[0], argv[1]))
            # მსგავსი მეთოდით შეგვიძლია გამოვიყენოთ ფუნქციისთვის გადაცემული ატრობუტები
            stime = time.time()
            fpar = f(*argv, **kwargv)
            dtime = time.time() - stime
            print(' Time passed: ', dtime)
            return fpar #  დავაბრუნოთ შესრულებული ფუნქციის მნიშვენლობა
        return closure

@TimeDelta(1,2,3)
def Power(a, n):
    return a**n

a = Power(3, 4)
print(a)



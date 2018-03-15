#coding:utf-8
#斐波那契数列的yield写法

def fib(num):
    a,b=0,1
    for i in range(num):
        yield b
        a,b=b,a+b
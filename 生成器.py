# 要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。     保留的是算法
# 对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。


# def fbi(max):
#     n,a,b=0,0,1
#     while n<max:
#         print(b)
#         a,b=b,a+b                                                 这种一边循环一边计算的机制，称为生成器：generator。
#         n=n+1                                     第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
#                                                   generator的第二种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
#     return 'done'                           generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
#
# ff=fbi(6)#print是一个调用函数，打印出返回的值
# print(ff)

# def fbi(max):                             #回到fib的例子，我们在循环过程中不断调用yield，就会不断中断。
#     n,a,b=0,0,1
#     while n<max:
#         yield b                                # generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
#         a,b=b,a+b                               #fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
#         n=n+1                                                               #面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
#     return 'done'
#
# ff=fbi(6)#print是一个调用函数，打印出返回的值
# print(ff)#<generator object fbi at 0x0000000002801258> 打印出的是一个generator生成器对象
#
# # for x in ff:#因为generator是一个可迭代对象
# #     print(x)
# #但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
# while True:
#     try:
#         g=next(ff)
#         print(g)
#     except StopIteration as e:#返回值包含在StopIteration的value中：
#         print('generator return value:',e.value)
#         break  #一直取值  直到拿到他的返回值  就退出break

# 这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

# def odd():
#     print('step1')
#     yield 1
#     print('step2')
#     yield 3
#     print('step3')
#     yield 5
#     return 'done'
# 调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：
# aa=odd()#生成器对象
# print(next(aa))  #可以通过next()函数获得generator的下一个返回值：
# print(next(aa))
# print(next(aa))#可以看到，odd不是普通函数，而是generator，在执行过程中，遇到yield就中断   如果是个普通函数的话就会直接按照顺序打印135 然后结束
# #下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。
# for x in aa:
#     print(x)


l=[1,2]
print(l[1])

def triangles():
    L=[1]
    while True:
        yield L
        L = [1]+[L[x]+L[x+1] for x in range(len(L)-1)] +[1]
for x in triangles():
    print(x)
## 제너레이터

## 제너레이터는 파이썬의 시퀀스를 생성하는 객체다.
## 전체 시퀀스를 한번에 메모리에 생성하고 정렬할 필요 없이, 
## 잠재적으로 아주 큰 시퀀스를 순회할 수 있다.

## 제너레이터 생성하기

# def my_range(first=0, last=10, step=1):
#     number = first
#     while number < last:
#         yield number
#         number += step

# print(my_range)

# ranger = my_range(1,5)

# print(ranger.next())

# for x in ranger:
#     print(x)

## 데코레이터

# def decoTest(func):
#     def newFunction(*args, **kwargs):
#         print('this is my deco')
#     return newFunction

# def add_int(a, b):
#     return a + b

# print(add_int(3, 5))

# decoTest(add_int(3, 5))()
# @decoTest
# def addWithDeco(a, b):
#     return a + b

# addWithDeco(3, 5)
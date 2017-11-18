# # 함수정의

# def doSomeThing():
#     print('quack')

# # 함수 사용

# doSomeThing()

# # 인자값을 받는 함수
# # 함수로 전달한 값을 인자라고 부른다.
# # 인자값은 함수 내에서 해당하는 매개변수에 복사된다.

# def test(input):
#     return input + ' ' + input

# print(test('this is input'))

# # 유용한 None
# # None 은 아무것도 없다는 것을 뜻한다.
# # Bool값으로 평가될 때는 False 처럼 보이지만 False 와는 다른 특징이 있다.

# def isNone(input = None):
#     if input is None:
#         print("It's None")
#     elif input:
#         print("It's True")
#     else:
#         print("It's False")

# # None Test

# isNone()
# isNone(True)
# isNone(False)
# isNone(0)
# isNone('')

## 함수 인자값 받기 형태

## 위치 인자

# def menu(wine, entree, dessert):
#     return {'wine':wine, 'entree':entree, 'dessert':dessert}

# print(menu('test1', 'test2', 'test3'))

## 키워드 인자

# print(menu(entree='test1', dessert='test2', wine='test3'))

## 기본 매개변수값 지정하기

# def menu(input1, input2= 'this is input2', input3 = 'this is input3'):
#     print(input1 + input2 + input3)

# menu('test1')

##! 기본 인자값은 함수를 실행할 때 선언되는 것이 아니라
##! 함수를 정의할 때 선언된다 

# def buggy(arg, result = []):
#     result.append(arg)
#     print(result)

# buggy('1')
# buggy('2')

## None 사용의 좋은 예

# def noBuggy(arg, result=None):
#     if result is None:
#         result = []
#     result.append(arg)
#     print(result)

# noBuggy('a')
# noBuggy('b', [1,2,3,4,5])

## 위치인자 모으기
# def print_args(*args):
#     print('Positional argument tuple:', args)

# print_args(3,2,1)

## 키워드 인자 모으기
# def print_kwargs(**kwargs):
# 	type(kwargs)
# 	print('keyword arguments:', kwargs)

# print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

## docstring

from collections import defaultdict

def echo(anything):
    'echo returns its input argument'
    return anything

def print_if_true(thing, check):
    '''
    Print the first ajsdkfl;askdjf;lasdifjalsdifj
    '''
    if check:
        print(thing)

# help(defaultdict.__missing__.__doc__)
# help(echo)
# help(echo.__doc__)
# help(print_if_true)
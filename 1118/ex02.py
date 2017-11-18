## 모든것이 객체다

# def test1():
#     print(42)

# def doSomething(fun):
#     fun()

# doSomething(test1)

# print(type(doSomething))

# def test(func, arr1, arr2):
#     return func(arr1, arr2)

# test(print, 5, 9)

## 내부함수
## 내부 함수는 루프나 코드 중복을 피하기 위해 또 
## 다른 함수 내에 어떤 복잡한 작업을 한번 이상 수행할 때 유용하게 사용된다.

# def outer(a,b):
#     def inner(c, d):
#         return c + d
#     return inner(a, b)

# print(outer(4,7))

## 클로져
## outer 의 return inner 에 의해 
## inner의 복사본이 반환된다.
# def outer(input):
#     def inner():
#         return "this is test : %s" % input
#     return inner

# a = outer(1)
# b = outer(1)

# print(outer('value'))
# print(outer('value1123123'))

## 익명함수 : lambda

# def test(arr, func):
#     for ele in arr:
#         print(func(ele))

# inputs = [1,2,3,4,5,6]

# def numChange(num):
#     return num + 3

# test(inputs, numChange)

## 람다 사용

# test(inputs, lambda num: num + 2)
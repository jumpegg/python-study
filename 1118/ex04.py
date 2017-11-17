## 네임 스페이스와 스코프
# animal = "test"

# def animalChange():
#     # print(animal)
#     animal = "after test"
#     print(animal)

# animalChange()

## 명시적 전역변수 접근

# animal = "test"

# def animalChange():
#     global animal
#     animal = 'after test'
    
# print(animal)
# animalChange()
# print(animal)

## 네임스페이스 내용 접근 함수

# animal = "test"
# def animalChange():
#     animal = 'after test'
#     print('locals: ', locals())

# animalChange()

# print('globals: ', globals())

## 언더바 네이밍
## __ 로 시작하고 끝나는 이름은 파이썬 내의 사용을 위해 예약되어 있다.
## 그러므로 __를 사용한 변수 명명법은 피하는 것이 좋다.
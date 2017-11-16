## while

count = 1
while count <= 5:
	print(count)
	count += 1

## break

while True:
	stuff = input("String to capitalize [type q to quit]:")
	if stuff == "q":
		break
	print(stuff.capitalize())


## countinue

while True:
	value = input("Integer, please [q to quit]:")
	if value == 'q':
		break
	number = int(value)
	if number % 2 == 0:
		continue
	print(number, "square is", number*number)

## break else

numbers = [1,2,5]
position = 0
while position < len(numbers):
	number = numbers[position]
	if number % 2 == 0:
		print('Found even number', number)
		break
	position += 1
else: #break 가 호출되지 않으면 실행된다
	print('No even number found')

## for

rabbits = ['flopsy', 'mopsy', 'cottontail', 'peter']
current = 0
while current < len(rabbits):
	print(rabbits[current])
	current += 1

for rabbit in rabbits:
	print(rabbit)

## 문자열 순회
word = 'cat'
for letter in word:
	print(letter)

## 딕셔너리 순회
temp = {'case1':'out1', 'case2':'out2', 'case3':'out3', 'case4':'out4'}
for card in temp:
	print(card)

for value in temp.values():
	print(value)

for key, value in temp.items():
	print(key + " " + value)

## 여러 시퀀스 순회하기 zip()

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
	print(day + fruit + drink + dessert)

newList = list(zip(desserts, days))
print(newList)

newDict = dict(zip(days, desserts))
print(newDict)

## 숫자 시퀀스 생성하기 range()
## zip(), range() 와 같은 함수는 순회 가능한 객체를 반환한다.
## range() 함수는 리스트나 튜플 같은 자료구조를 생성하여 저장하지 않더라도 특정 범위내에서 숫자 스트림을 반환한다.
## 이것은 컴퓨터의 메모리를 전부 사용하지 않고, 프로그램의 충돌 없이 아주 큰 범위를 생성할 수 있게 해준다.

for x in range(0,5):
	print(x)

for x in range(0,10,2):
	print(x)

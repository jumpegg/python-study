### 컴프리헨션

## 리스트 

## ex00
number_list = []
for number in range(1,6):
	number_list.append(number)

print(number_list)

## ex01

number_list = [number for number in range(1,6)]
print(number_list)

## ex02

a_list = [number for number in range(6,0,-1) if number % 2 == 1]
print(a_list)

rows = range(1,4)
cols = range(1,3)
tests = range(1,5)
for row in rows:
	for col in cols:
		print(row, col)

cells = [{row, col, test} for row in rows for col in cols for test in tests]

for cell in cells:
	print(cell)

## 딕셔너리

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

## 셋 

a_set = {number for number in range(1,6) if number % 3 == 1}
print(a_set)

## 제너레이터
## 튜플은 컴프리헨션이 없다.
number_thing = (number for number in range(1,6))
print(number_thing)

for number in number_thing:
	print(number)

for number in number_thing:
	print(number)
# 주석 달기
print('no comment')

# 라인 유지하기
text = 'asdf' + \
			'asdfdfdf'

print(text)

# 비교하기 if, elif, else

disaster = True
# disaster = False

if disaster:
	print("Woe")
else:
	print("whee")

# 비교 연산자

x = 7
nums = [1,2,3]

print('x == 7')
print(x == 7)
print('x == 5')
print(x == 5)
print('x < 10')
print(x < 10)
print('in : ')
print(x in nums)

# False형 데이터

xfalse = None
# xfalse = 0
# xfalse = 0.0
# xfalse = ''
# xfalse = []
# xfalse = ()
# xfalse = {}
# xfalse = set()

if xfalse:
	print('this is true')
else:
	print('this is false')

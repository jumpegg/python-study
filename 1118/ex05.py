## 예외처리

# short_list = [1,2,3]
# position = 5
# # short_list[position]
# try:
#     short_list[position]
# except:
#     print('this is error')

## error 타입에 따른 예외처리 방법

testArr = [1,2,3]
while True:
    value = input('Position [q to quit]?')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad Index:', position)
    except Exception as other:
        print('this is error')

## error 타입 만들기

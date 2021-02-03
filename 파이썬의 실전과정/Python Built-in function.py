## 파이썬 프로그래밍의 핵심, 내장함수
# 내장함수란? 파이썬에서 기본적으로 포함하고 있는 함수(print(),type())

# abs / 절대값

print(abs(-3))          ## Result : 3

# all / 모두 참인지 검사

print(all([1,2,3]))         ## Result : True
print(all([1,2,3,0]))           ## Result : False
# 파이썬에서 0은 False로 구분한다.

# any / 하나라도 참이 있는가?

print(any([1,2,3,0]))           ## Result : True
print(any([0,""]))          ## Result : False
# 파이썬에서 "" 빈 구문은 False로 구분한다.

# chr / ASCII 코드를 입력받아 문자 출력
# ASCII(아스키 코드) = 0~127 사이의 숫자를 각 문자에 대응

print(chr(97))          ## Result : a
print(chr(48))          ## Result : 0

# dir / 자체적으로 가지고 있는 변수나 함수를 보여줌
# 해당 리스트에서 무슨 명령어를 사용 할 수 있는지 모아서 보여준다.

print(dir([1,2,3]))         ## Result : ['__add__', '__class__', '__class_getitem__',...]
print(dir({'1':'a'}))           ## Result : ['__class__', '__class_getitem__',...]

# divmod / 몫과 나머지를 튜플 형태로 돌려줌

print(divmod(7,3))          ## Result : (2, 1)
print(divmod(1.3,0.2))          ## Result : (6.0, 0.09999999999999998)

# enumerate / 열거하다
# 어떠한 리스트를 인덱스와 value로 빼서 활용 할 수 있다.

for i, name in enumerate(['body','foo','bar']):
    print(i,name)
    ## Result : 0 body
    ##          1 foo
    ##          2 bar

# eval / 실행 후 결과값을 돌려줌

print(eval('1+2'))          ## Result : 3
print(eval("'hi' + 'a'"))           ## Result : hia
print(eval('divmod(4,3)'))          ## Result : (1, 1)

# filter / 함수를 통과하여 참인 것만 돌려줌

def positive(x):    # x의 값이 양수인 값만 남기는 함수
    return x > 0

a = list(filter(positive, [1,-3,2,0,-5,6]))

print(a)            ## Result : [1, 2, 6]

b = list(filter(lambda x: x > 0, [1,-3,2,0,-5,6]))

print(b)            ## Result : [1, 2, 6]

# id / 주소 값

c = 3

print(id(3))            ## Result : 2001170491760
print(id(a))            ## Result : 2001176248256

d = c

print(id(d))            ## Result : 2001170491760

# input / 사용자 입력 받는 함수

e = input() # insert 'hi'

print(e)            ## Result : hi

f = input("Enter: ")

print(f)            ## Result : hi

# int / 10진수 정수 형태로 변환

print(int(3.4))         ## Result : 3
print(int('11',2))          ## Result : 3
print(int('1A',16))         ## Result : 26

# len / 길이

print(len("python"))            ## Result : 6
print(len([1,2,3]))         ## Result : 3
print(len((1,'a')))         ## Result : 2

# list / 리스트로 변환

print(list("python"))           ## Result : ['p', 'y', 't', 'h', 'o', 'n']

g = [1,2,3]
h = list(g)

print(g)            ## Result : [1, 2, 3]
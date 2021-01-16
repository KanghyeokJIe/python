## 1. 숫자열 자료형 표현 방법
a = 1

print(type(a))
## Result : <class 'int'> int는 정수형 자료형 이란 뜻이다.

a = 1.24

print(type(a))
## Result : <class 'float'> float은 실수형 자료형 이란 뜻이다.


## 1.1 사칙연산

a = 3
b = 4

print(a+b)
## Result : 7 덧셈을 할 수 있다.

print(a*b)
## Result : 12 곱셈을 할 수 있다.

print(a/b)
## Result : 0.75 나눗셈을 할 수 있다.

print(a//b)
## Result : 0 // 연산자는 나눴을 때 몫을 구할 수 있다.

print(a%b)
## Result : 3 % 연산자는 나눴을 때 나머지를 구할 수 있다.

print(a**b)
## Result : 81 **연산자는 제곱의 값을 구할 수 있다.




## 2. 문자열 자료형 표현 방법
# 2.1 문자열 자료형 만드는 4가지 방법

a = "Hello World"
b = 'Python is fun'
c = """Life is too short, You need python"""
d = '''Life is too short, You need python'''

print(a)
print(type(a))
## Result : Hello World 
## Result : <class 'str'> str은 문자열 자료형 뜻이다.

print(b)
## Result : Python is fun

print(c)
## Result : Life is too short, You need python

print(d)
## Result : Life is too short, You need python

# 2.2 문자열에 따옴표 포함시키기

a = 'Python\'s favorite food is perl'

print(a)
## Result : Python's favorite food is perl \ 키를 통해 문자열에 따옴표를 포함 시킬 수 있다.

# 2.3 여러 줄로 이루어진 문자열

a = 'Life is too short\nYou need python'

print(a)
## Result : Life is too short
##          You need python \n(이스케이프 문자)를 이용하여 여러 줄로 문자열을 만들 수 있다.

a = """Life is too short
You need
python"""

print(a)
## Result : Life is too short
##          You need
##          python : 따옴표 3개로 작성하면 이스케이프 문자를 사용하지 않아도 여러 줄의 문자열을 만들 수 있다.

# 2.4 문자열 더하거나 곱해서 연결하기 

a = "Python"
b = " is fun!"

print(a+b)
## Result : Python is fun!

print(a*3)
## Result : PythonPythonPython

# 2.5 인덱싱 (Indexing)

a = "Life is too short, You need python"

print(a[0])
print(a[1])
print(a[2])
## Result : L
## Result : i
## Result : f 변수 a에 저장한 문자열에 각 문자마다 번호를 매긴 것을 인덱싱이라 한다.

print(a[-1])
print(a[-2])
## Result : n
## Result : o 인덱싱에서 -는 역방향으로 값을 나타낸다.






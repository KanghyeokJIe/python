## 파이썬 프로그래밍의 핵심, 클래스(과자 틀(클래스), 과자(객체))
# 클래스란? 반복되는 변수 & 메서드(함수)를 미리 정해놓은 틀(설계도)
# 클래스는 도대체 왜 필요한가?

result = 0
def add(num):
    global result           # 전역변수에 영향을 주기 위해 global 함수를 사용
    result += num
    return result

print(add(3))           ## Result : 3
# 함수를 실행 시킨뒤 3이 출력 되었다.
print(add(4))           ## Result : 7
# 전역변수에 영향을 주었기 때문에 result의 값이 3이 되어 7이 출력 되었다.

# 두 개의 계산기

result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))          ## Result : 3
print(add1(4))          ## Result : 7
print(add2(3))          ## Result : 3
print(add2(7))          ## Result : 10

# 클래스는 함수와 변수를 하나로 묶어 설계도로 나타낸 것이다.
        # class 사용 방법
#   1. class를 입력한다.
#   2. 대문자로 시작하는 class의 이름을 작성한다.
#   3. 안에 들어갈 함수와 변수를 설정 한다.

class Calculator:
    def __init__(self):
        self.result3 = 0

    def add(self, num):
        self.result3 += num
        return self.result3

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))          ## Result : 3
print(cal1.add(4))          ## Result : 7
print(cal2.add(3))          ## Result : 3
print(cal2.add(7))          ## Result : 10

# 위에 계산기와 결과는 같지만 훨씬 간단히 만들었다.

# 사칙연산 클래스 만들기(+,-,*,/)
# 사칙연산 클래스 1

class Fourcal:
    pass

a = Fourcal()
print(type(a))          ## Result : <class '__main__.Fourcal'>

# 사칙연산 클래스 2

class Fourcal2:
    def setdata(self,first,second):
        self.first = first
        self.second = second

a = Fourcal2()
# a라는 객체가 self에 들어가게 된다.
a.setdata(4,2)

print(a.first)          ## Result : 4
# a가 갖고 있는 first라는 변수는 setdata를 통해 값이 출력되었다.

print(a.second)         ## Result : 2
# a가 갖고 있는 second라는 변수는 setdata를 통해 값이 출력되었다.

# 사칙연산 클래스 3

class Fourcal3:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result4 = self.first+self.second
        # self가 self.first+self.second를 실행하였다.
        return result4
        # result변수에 담아 return 하여준다.

a = Fourcal3()
a.setdata(4,2)
print(a.add())          ## Result : 6
# 4와 2를 더한 값인 6이 출력 되었다.

# 생성자(Constructor)

class Fourcal4:
    def __init__(self,first,second):
        # __init__ 은 Fourcal4라는 class를 실행 할때 무조건 가장 먼저 수행하게 된다.
        self.first = first
        self.second = second
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result5 = self.first+self.second
        return result5

a = Fourcal4(1,2)
# __init__을 사용하였기에 first,second 값을 넣어 주지 않으면 오류가 나게 된다.
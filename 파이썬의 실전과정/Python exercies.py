## 파이썬 심화형 연습문제
# Q1 다음은 Calculator 클래스이다.

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

# 위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해보자.
# 즉 다음과 같이 동작 하는 클래스를 만들어야 한다.

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value) # 10에서 7을 뺀 3을 출력

# Q2 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자.
# 즉 다음과 같이 동작해야 한다.

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기

print(cal.value) # 100 출력

# 단 반드시 다음과 같은 Calculator 클래스를 상속해서 만들어야 한다.
#class Calculator:
#    def __init__(self):
#        self.value = 0

#    def add(self, val):
#        self.value += val

# Q3 다음 결과를 예측해 보자.

print(all([1, 2, abs(-3)-3]))
# False abs(-3)은 -3의 절댓값이므로 3이 되어 all([1, 2, 0])이 되고,
# 리스트의 요솟값중 0이 있기 때문에 all 내장 함수의 결과는 False가 된다.

# 두번째

chr(ord('a')) == 'a'
# True ord('a') 의 결과는 97이 되어 chr(97)로 치환된다.
# chr(97)의 결과는 다시 'a'가 되므로 'a' == 'a'가 되어 True를 돌려준다.

# Q4 filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.

print(list(filter(lambda x:x>0, [1,-1,3,-5,8,-3])))
# [1,3,8]

# Q5 234라는 10진수의 16진수는 다음과 같이 구할 수 있다.

print(hex(234))     ## Result : 0xea

# 이번에는 반대로 16진수 문자열 0xea를 10진수로 변경해 보자.
# ※ 내장 함수 int를 활용해 보자.

print(int('0xea',16))
# 234

# Q6 map과 lambda를 사용하여 [1, 2, 3, 4] 리스트의 각 요솟값에
# 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어 보자.

list(map(lambda x:x*3,[1,2,3,4]))
# [3,6,9,12]

# Q7 다음 리스트의 최댓값과 최솟값의 합을 구해 보자.
[-8, 2, 7, 5, -3, 5, 0, 1]

a = [-8, 2, 7, 5, -3, 5, 0, 1]

print(max(a))+min(a)
# -1

# Q8 17 / 3의 결과는 다음과 같다.

print(17/3)     ## Result : 5.666666666666667

# 위와 같은 결괏값 5.666666666666667을 소숫점 4자리까지만 반올림하여 표시해 보자.

round(17/3, 4)
# 5.6667

# Q9 time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해 보자.

import time
print(time.strftime("%Y/%m/%d %H:%M:%S"))   # %Y:년, %m:월, %d:일, %H:시, %M:분, %S:초


# Q10 random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 생성해 보자
# (단 중복된 숫자가 있으면 안 됨).

import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)   # 1부터 45까지의 난수 발생
    if num not in result:
        result.append(num)

print(result)
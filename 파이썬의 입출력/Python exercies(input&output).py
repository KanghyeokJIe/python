## 파이썬 입출력 연습문제
# Q1 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해보자.

def is_odd(number):
    if number % 2 == 1:     # 2로 나누었을 때 나머지가 1이면 홀수이다.
        return True
    else:
        return False

print(is_odd(3))            ## Result : True
# 2로 나눈 값이 1일 경우 True를 리턴 하였고, 아닌경우 False를 리턴 하였다.

# Q2 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해보자.
# (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
# ※ 평균 값을 구할 때 len 함수를 사용해 보자.

def average(*args):     # 입력 개수에 상관없이 사용하려면 *args를 사용.
    result = 0
    for i in args:
        result += i
    return result / len(args)
print(average(1,2,3))           ## Result : 2.0
# 입력값을 += 할당 연산자를 통해 result에 값을 넣고
# len 함수를 이용하여 평균 값을 구했다.

# Q3 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.
# input1 = input("첫번째 숫자를 입력하세요:")
# input2 = input("두번째 숫자를 입력하세요:")

# total = input1 + input2
# print("두 수의 합은 %s 입니다" % total)
# 이 프로그램을 수행해 보자.

# 첫번째 숫자를 입력하세요:3
# 두번째 숫자를 입력하세요:6
# 두 수의 합은 36 입니다
# 3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다.
# 이 프로그램의 오류를 수정해 보자.
# ※ int 함수를 사용해 보자.

input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")
total = int(input1) + int(input2)

print("두 수의 합은 %s 입니다" % total)
## Result : 첫번째 숫자를 입력하세요:3
##          두번째 숫자를 입력하세요:6
##          두 수의 합은 9 입니다.


# Q4 다음 중 출력 결과가 다른 것 한 개를 골라 보자.
print("you" "need" "python")                #youneedpython
print("you"+"need"+"python")                #youneedpython
print("you", "need", "python")              #you need python
print("".join(["you", "need", "python"]))   #youneedpython
## Result : ,가 있는 경우 공백이 삽입되어 더해진다.


# Q5 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후
# 다시 그 파일을 읽어서 출력하는 프로그램이다.

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

# 이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다.
# 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.

## Result : 파일을 닫지 않은 상태에서 다시 열면 저장한 데이터를 읽을 수 없다.
## 따라서 파일을 파일 객체 close로 닫아준 후 다시 열어 내용을 읽는다.


# Q6 사용자의 입력을 파일(test2.txt)에 저장하는 프로그램을 작성해 보자.
# (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)

user_input = input("저장할 내용을 입력하세요:")

f = open("test2.txt", 'a')
f.write(user_input)
f.write("\n")
# Hello World! 입력
f.close()
## Result : test2.txt 파일에는 Hello World! 라고 입력이 되었다.


# Q7 다음과 같은 내용을 지닌 파일 test3.txt가 있다.
# 이 파일의 내용 중 "java"라는 문자열을 "python" 으로 바꾸어서 저장해 보자.
# ※ replace 함수를 사용해 보자.

# Life is too short
# you need java

with open("test3.txt", "w") as f:
    f.write("Life is too short\nyou need java")

f = open('test3.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test3.txt', 'w')
f.write(body)
f.close()
## Result : 파일을 모두 읽은 후에 문자열의 replace 함수를 사용하여
## java라는 문자열을 python으로 변경한 다음 저장한다.
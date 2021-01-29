## 프로그램의 입출력은 어떻게 해야 할까?
# 함수의 구조

def sum(a,b):
    result = a+b
    return result

print(sum(1,2))         ## Result : 3

# 입력값,결과값이 없는 함수

def say():
    return 'HI'

print(say())            ## Result : HI / 입력값이 없어도 결과가 출력 되었다.

def sum(a,b):
    print("%d, %d의 합은 %d입니다."%(a,b,a+b))

sum(1,2)            ## Result : 1, 2의 합은 3입니다. / print 함수가 실행 되여 결과 값이 나왔다.

print(sum(1,2))         ## Result : None / return 값이 없기 때문에 None 이라고 출력 되었다.

# 입력값과 결과값이 모두 없는 함수

def say():
    print('HI')

print(say())            ## Result : None / 입출력이 모두 없다.

# 여러 개의 입력값

def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum

print(sum_many(1,2,3))          ## Result : 6 / *args는 몇 개든 상관없이 다 들어갈 수 있다.

# 키워드 파라미터

def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if(k == "name"):
            print("당신의 이름은 :"+k)
print(print_kwargs(name="martin"))

# 함수의 결과값은 언제나 하나이다.

def sum_and_mul(a,b):
    return a+b,a*b

print(sum_and_mul(1,2))         ## Result : (3, 2) / 값은 두개이지만 튜플 형태로 하나로 묶여서 출력된다.

# 매개 변수에 초깃값 미리 설정하기

def say_myself(name,old,man=True):
    print("나의 이름은 %s 입니다."% name)
    print("나이는 %d살입니다."% old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("martin",23)
## Result : 나의 이름은 martin 입니다.
## 나이는 23살입니다.
## 남자입니다. / man 의 값을 True 로 기본값을 설정 하였기 때문에 값을 넣지 않아도 오류가 생기지 않았다.

# 함수 매개 변수에 초깃값을 설정할 때 주의할 사항

# def say_myself(name,man=True, old):
#     print("나의 이름은 %s 입니다."% name)
#     print("나이는 %d살입니다."% old)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")

# say_myself("martin",23)
## Result : SyntaxError: non-default argument follows default argument / 함수의 초기값을 설정 하면 설정한 값은 맨 끝으로 가야 한다.

# 함수 안에서 선언된 변수의 효력 범위

a = 1
def vartest(a):
    a = a+1

vartest(1)
print(a)            ## Result : 1 / def함수 안에서 변수를 선언하면 함수 안에서만 쓰인다.

# 함수 안에서 함수 밖의 변수를 변경하는 방법 1,2

a = 1
def vartest(a):
    a = a+1
    return a

a = vartest(a)
print(a)            ## Result : 2 / return 값을 a에 다시 할당하였다.

a = 1
def vartest():
    global a
    a = a+1

vartest()
print(a)            ## Result : 2 / global을 이용해서 a를 전역변수로 지정하여 준다.

# Lambda

add = lambda c ,d: c+d

print(add(3,4))         ## Result : 7 / lambda 함수를 이용하여 함수를 간단하게 만들 수 있다.

myList = [lambda c,d:c+d, lambda c,d:c*d]

print(myList[0](1,2))           ## Result : 3 / lambda c,d:c+d 함수를 리스트에서 불러와서 실행 (인덱스 0번째).
print(myList[1](1,2))           ## Result : 2 / lambda c,d:c*d 함수를 리스트에서 불러와서 실행 (인덱스 1번째).
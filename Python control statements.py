## 파이썬의 제어문
# 1. 조건문 / if문의 기본 구조

moeny = True

if moeny:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
## Result : 택시를 타고 가라 / if조건문 뒤에 수행할 문장과 else 뒤에 수행할 문장을 통해 조건에 따라 값이 다르게 출력됨.

# 1.1 들여쓰기 오류

moeny = True

if moeny:
    print("택시를 타고 가라")
#print("aa")
else:
    print("걸어 가라")
## Result : SyntaxError: invalid syntax / 문법이 잘못 되었다고 오류가 남.

##   비교 연산자          설명
##      x<y          x가 y보다 작다.
##      x>y          x가 y보다 크다.
##      x==y         x와 y가 같다.
##      x!=y         x와 y가 같지 않다.
##      x>=y         x가 y보다 크거나 같다.
##      x<=y         x가 y보다 작거나 같다.

## 실습

a = 1
b = 2

if a < b:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
## Result : 택시를 타고 가라 / a가 b보다 작은 것이 True 이기 때문에 택시를 타고 가라 라고 출력 됨.

## 예문 : 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어가라

money = 2000

if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
## Result : 걸어가라 / money의 값이 2000으로 if 문에서 3000의 조건에 False 이기 때문에 걸어가라 라고 출력되었다.

##                and, or, not
##      연산자                   설명
##      x or y (|)        x와 y둘중에 하나만 참이면 참이다.
##      x and y (&)       x와 y 모두 참이어야 참이다.
##      not x             x가 거짓이면 참이다.

money = 2000
card = 1

if money >= 3000 or card :
    print("택시를 타고 가라")
else:
    print("걸어가라")
## Result : 택시를 타고 가라 / or 연산자를 통해 money는 False 이지만 card는 True이기 때문에 택시를 타고 가라가 출력됨.

# 1.2 x in s, x not in s

if 1 in [1,2,3]:
    print("Hello World!")
else:
    print("Good bye")
## Result : Hello World! / 리스트 안에 1이 있는지 확인 후 Hello World! 가 출력되었다.

if 1 not in [1,2,3]:
    print("Hello World!")
else:
    print("Good bye")
## Result : Good bye / 리스트 안에 1이 없는지 확인 후 Good bye 가 출력되었다.

# 1.3 조건문에서 아무 일도 하지 않게 설정하고 싶다면?

pocket = ['paper','money','cellphone']

if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
## Result : / pocket 리스트 안에 money 가 있기에 pass 하여 아무런 값도 출력 되지 않는다.

# 1.4 다중 조건 판단 (elif)

pocket = ['paper','cellphone']
card = True

if 'money' in pocket:
    pass
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")
## Result : 택시를 타고가라 / pocket 안에 money 는 없지만 다중 조건문 elif를 통해 card는 있기 때문에 택시를 타고 가라가 출력되었다.

# 1.5 조건부 표현식

score = 70
message = "success" if score >= 60 else "failure"

print(message)
## Result : success / 한 줄로 더 간결하게 표현이 가능하다. (else를 반드시 써야 오류가 나지 않는다.)
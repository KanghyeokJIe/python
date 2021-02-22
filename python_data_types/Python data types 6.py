## 자료형의 값을 저장하는 공간, 변수
# 다음 예와 같은 a,b,c를 변수라고 한다.

a = 1
b = 'python'
c = [1,2,3]

# 파이썬에서 사용하는 변수는 객체를 가리키는 것

a = 3

### 3이라는 값을 가지는 정수 자료형(객체)이 자동으로 메모리에 생성
### 변수 a는 객체가 저장된 메모리에 위치를 가리키는 레퍼런스 (Reference)
### a라는 변수는 3이라는 정수형 객체를 가리키고 있다. // pythontutor.com 에서 시각적으로 볼 수 있다.

# 리스트 변수 주의사항

a = [1,2,3]
b = a

a[1] = 4

print(a)            ## Result : [1, 4, 3] / a변수의 1번째 인덱스를 4로 바꿔서 [1, 4, 3] 이라는 결과가 나왔다.
print(b)            ## Result : [1, 4, 3] / a리스트의 주소를 b에 넣었기 때문에 b의 값도 같이 변화하여 출력 되었다.
print(a is b)           ## Result : True / a와 b 가 같은 주소를 가리킨다.

a = [1,2,3]
b = a[:]
a[1] = 4

print(a)            ## Result : [1, 4, 3] / a변수의 1번째 인덱스를 4로 바꿔서 [1, 4, 3] 이라는 결과가 나왔다.
print(b)            ## Result : [1, 2, 3] / 슬라이싱해서 새로 넣으면 값을 새로 넣는 것이다.
print(a is b)           ## Result : False / a와 b 가 다른 주소를 가리킨다.

from copy import copy
a = [1,2,3]
b = copy(a)
a[1] = 4

print(a)            ## Result : [1, 4, 3] / a변수의 1번째 인덱스를 4로 바꿔서 [1, 4, 3] 이라는 결과가 나왔다.
print(b)            ## Result : [1, 2, 3] / copy 함수를 가져와 복사 하였다.
print(a is b)           ## Result : False / a와 b 가 다른 주소를 가리킨다.

## 변수를 할당하는 여러가지 방법
# 튜플을 이용하여 각각 할당

(a,b) = 'python','life'

print(a)            ## Result : python
print(b)            ## Result : life

# 리스트를 이용하여 각각 할당

[a,b] = ['apple','banana']

print(a)            ## Result : apple
print(b)            ## Result : banana

#  = 부등호 이용하여 할당(a와 b에 같은 값을 넣을 때 사용)

a = b = 'hello'

print(a)            ## Result : hello
print(b)            ## Result : hello

# 임시변수 활용하여 변수의 값을 바꾸기

a = 3
b = 5

a,b = b,a

print(a)            ## Result : 5
print(b)            ## Result : 3
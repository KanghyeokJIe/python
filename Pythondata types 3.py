## 3. 리스트 자료형 표현방법
from typing import List

a = ["이시영","문재성","int","김정현"]

print (a)
## Result : ['이시영', '문재성', 'int', '김정현'] / 하나의 변수에 여러 개의 값을 관리할 때 사용함.

## 3.1 리스트의 인덱싱

a = [1,2,3]

print (a[0])
print (a[0] + a[2])
print (a[-1])
## Result : 1 / 리스트의 인덱싱.
## Result : 4 / 리스트의 인덱스 값을 더해서 출력.
## Result : 3 / 리스트의 인덱스 번호를 - 기호를 통해 거꾸로 출력.

## 3.2 리스트의 슬라이싱

a = [1,2,3,4,5]

print (a[0:3])
## Result : [1, 2, 3] / 슬라이싱을 통해 4 전까지 잘라냈다.

## 3.3 리스트 더하기, 반복하기

a = [1,2,3]
b = [4,5,6]

print (a+b)
## Result : [1, 2, 3, 4, 5, 6] / 리스트 두개를 더하여 하나로 합쳐진다.

print (a*3)
## Result : [1, 2, 3, 1, 2, 3, 1, 2, 3] / 리스트를 곱하여 출력한다.

## 3.4 리스트에서 하나의 값,연속된 범위에 값 수정하기

a: list[str] = ["a","b","c"]
a[0] = "d"

print (a)
## Result : ['d', 'b', 'c'] / 변수값이 바뀌어 출력 되었다.

a[0:2] = ["e","f"]

print(a)
## Result : ['e', 'f', 'c'] / 변수값의 값을 연속적으로 수정하여 출력한다.

## 3.5 [],del 함수 사용해 리스트 요소 삭제하기

a[0:2] = []

print(a)
## Result : ['c'] / 빈 리스트로 교체하면 삭제된다.

del a[0]

print(a)
## Result : [] / del 함수를 이용해 삭제하였다.

## 3.6 리스트에 요소 추가(append)

b = ["apple", "banana", "cake",]
b.append("diamond")

print(b)
## Result : ['apple', 'banana', 'cake', 'diamond'] / 기존의 리스트에 값을 추가 하였다.

## 3.7 리스트 정렬(sort)

a = [1,5,3]
b = ["c","a","b"]
a.sort()
b.sort()

print(a)
print(b)
## Result : [1, 3, 5] / 숫자는 크기 순으로 정렬된다.
## Result : ['a', 'b', 'c'] / 문자는 가나다 혹은 알파벳 순으로 정렬된다.

## 3.8 리스트 뒤집기(reverse)

a = [1,5,3]
a.reverse()

print(a)
## Result : [3, 5, 1] / a 변수의 값을 거꾸로 출력한다.

## 3.9 위치 변환(index)

a = [1,5,3]

print(a.index(5))
## Result : 1 / 변수에서 5번이 있을 때 그 값의 인덱스값을 출력한다.

## 3.10 리스트에 요소 삽입,제거(insert,remove)

a = [1,5,3]
a.insert(0,4)

print(a)
## Result : [4, 1, 5, 3] / 0번째 인덱스에 4를 추가하여 출력한다.

a = [1,5,3]
a.remove(1)

print(a)
## Result : [5, 3] / 리스트에서 1번 값을 삭제하고 출력한다.

## 3.11 리스트 요소 끄집어 내기(pop)

a = [1,5,3]

print(a.pop())
print(a)
## Result : 3 / 리스트에서 3번 값을 나오게 한다.
## Result : [1, 5] / 리스트에서 3이 나온 나머지 값을 출력한다.

## 3.12 리스트에 포함된 요소 x의 개수 세기(count)

a = [1,5,3,1,1]

print(a.count(1))
## Result : 3 / 리스트에서 1의 개수를 세어준다.

## 3.13 리스트 확장(extend)

a = [1,2,3]
a.extend([4,5])

print(a)
## Result : [1, 2, 3, 4, 5] / a리스트에 [4,5] 리스트를 확장하여 출력한다.



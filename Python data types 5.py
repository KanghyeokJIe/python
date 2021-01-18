## 집합 자료형 표현방법
# 6. 집합 자료형은 순서가 없고 중복이 허용되지 않는다.

s1 = set([1,2,3])
s2 = set("hello")

print(s1)
print(s2)
## Result : {1, 2, 3}
## Result : {'h', 'e', 'l', 'o'}

# 6.1 교집합

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1 & s2)
print(s1.intersection(s2))
## Result : {4, 5, 6}
## Result : {4, 5, 6}

# 6.2 합집합

print(s1 | s2)
print(s1.union(s2))
## Result : {1, 2, 3, 4, 5, 6, 7, 8, 9}
## Result : {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 6.3 차집합

print(s1-s2)
print(s1.difference(s2))
## Result : {1, 2, 3}
## Result : {1, 2, 3}

#6.4 값 1개,여러 개 추가하기(add,update)

s1 = set([1,2,3,4,5,6])
s1.add(7)

print(s1)
## Result : {1, 2, 3, 4, 5, 6, 7}

s1 = set([1,2,3,4,5,6])
s1.update([7,8,9])

print(s1)
## Result : {1, 2, 3, 4, 5, 6, 7, 8, 9} / 기존의 값을 추가하면 중복 값이기에 추가 되지 않는다.

# 6.5 특정 값 제거하기(remove)

s1 = set([1,2,3,4,5,6])
s1.remove(1)

print(s1)
## Result : {2, 3, 4, 5, 6}

## 불 자료형 표현방법
# 불 자료형은 참, 거짓을 나타내는 True,False 로 나타낼 수 있다.

a = True

if a:
    print(a)
## Result : True

a = "hello"
b = 1
c = [1,2,3]

if a:
    print(a)
if b:
    print(b)
if c:
    print(c)
## Result : hello,1,[1,2,3] / 불 자료형은 문자열(str) 자료형과 숫자 1, 채워진 딕셔너리는 True로 판단한다.







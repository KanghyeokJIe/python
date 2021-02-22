## 튜플 자료형 표현 방법
# 튜플 요소값 삭제,변경 시 오류

t1 = (1,2,'a','b')
## del t1[0]
## Result : TypeError: 'tuple' object doesn't support item deletion / 튜플은 삭제를 지원 하지 않음.

t1 = (1,2,'a','b')
## t1[0] = 'c'
## Result : TypeError: 'tuple' object does not support item assignment / 튜플은 변경을 지원 하지 않음.

# 인덱싱,슬라이싱

t1 = (1,2,'a','b')

print(t1[0])            ## Result : 1 / 0 번째 요소는 1 이다.

print(t1[0:2])          ## Result : (1,2) / 0 번째 요소는 1 이다.

# 더하기,곱하기

t2 = (3,4)

print(t1+t2)            ## Result : (1, 2, 'a', 'b', 3, 4) / t1,t2 를 더한 새로운 튜플 생성.

print(t1*3)         ## Result : (1, 2, 'a', 'b', 1, 2, 'a', 'b', 1, 2, 'a', 'b') / t1을 3번 쓴 새로운 튜플 생성.

## 딕셔너리 자료형 표현 방법
# 딕셔너리 쌍 추가하기,요소 삭제하기

a = {1: 'a'}
a['name'] = "martin"

print(a)            ## Result : {1: 'a', 'name': 'martin'} / 딕셔너리에 name martin key 와 value 한쌍이 추가됨.

del a[1]

print(a)            ## Result : {1: 'a', 'name': 'martin'} / key 가 1이고 value 가 a 인 한쌍이 삭제됨.

# 딕셔너리에서 Key 사용해 Value 얻기

grade = {'pey': 10, 'julliet': 99}

print(grade['pey'])         ## Result : 10
print(grade['julliet'])         ## Result : 99

# 딕셔너리 만들 때 주의할 사항

a = {1: 'a', 1:'b'}

print(a)            ## Result : {1: 'b'} / key 가 중복 되면 마지막 키만 나온다.

# Key,value 리스트 만들기 (keys,values)

a = {1: 'apple', 2:'banana', 3: 'coconut'}

print(a.keys())         ## Result : dict_keys([1, 2, 3]) / key 만 따로 리스트 형태로 뽑을 수 있다.

print(a.values())           ## Result : dict_values(['apple', 'banana', 'coconut']) / value 만 따로 리스트 형태로 뽑을 수 있다.

# Key,value 쌍 얻기(items)

print(a.items())            ## Result : dict_items([(1, 'apple'), (2, 'banana'), (3, 'coconut')]) / key 와 value 쌍을 담을 수 있다.

# Key:Value 쌍 모두 지우기(clear)

a.clear()

print(a)            ## Result : {}

# Key로 Value 얻기(get)

a = {1: 'apple', 2:'banana', 3: 'coconut'}

###print(a[4])          ## Result : KeyError: 4
print(a.get(4))         ## Result : None / []를 사용할 때는 없는 key가 오류로 나오지만 get을 사용시 none 으로 도출된다.

print(a.get(4,'없음'))            ## Result : 없음 / 딕셔너리 안에 4라는 key가 없을 때 없음이라는 값을 리턴하라고 지정 가능하다.

# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)

a = {1: 'apple', 2:'banana', 3: 'coconut'}

print(4 in a)           ## Result : False
print(1 in a)           ## Result : True / in을 이용하여 Ture&False로 나타 낼 수 있다.
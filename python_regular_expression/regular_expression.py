## 파이썬 정규표현식 살펴보기
# 정규 표현식이란? 복잡한 문자열을 처리할 때 사용하는 기법 (모든 언어 공통)

# 문자 클래스 []
# [abc]

# [] 사이의 문자들과 매치
# "a" 는 정규식과 일치하는 문자인 "a" 가 있으므로 매치
# "before"는 정규식과 일치하는 문자인 "b"가 있으므로 매치
# "dude"는 정규식과 일치하는 문자인 a,b,c 중 어느 하나도 포함하고 있지 않으므로 매치되지 않음
# 하이픈을 사용하여 From-To로 표현 가능 ex) [a-c] = [abc], [0-5] = [012345]

# Dot(.)
# a.b

# 줄바꿈(\n)을 제외한 모든 문자와 매치
# "aab"는 가운데 문자가 "a"가 모든 문자를 의미하는 '.' 과 일치하므로 정규식과 매치
# "a0b"는 가운데 문자 "0"가 모든 문자를 의미하는 '.' 과 일치하므로 정규식과 매치
# "abc" 는 "a"문자와 "b"문자 사이에 어떤 문자라도 하나는있어야 하는 이 정규식과 일치하지 않으므로 매치되지 않음

# 반복(*), (+), ({m,n}, ?)
# ca*t (0번 이상의 반복부터 매치)

# "ct"는 "a"가 0번 반복되어 매치
# "cat"는 "a"가 0번이상 반복되어 매치(1번 반복)
# "caaat"는 "a"가 0번이상 반복되어 매치(3번 반복)

# ca+t (1번 이상의 반복부터 매치)

# "ct"는 "a"가 0번 반복되어 매치되지 않음
# "cat"는 "a"가 1번이상 반복되어 매치(1번 반복)
# "caaat"는 "a"가 1번이상 반복되어 매치(3번 반복)

# ca{2}t ({n}에 들어간 수의 반복만 매치)

# "cat"는 "a"가 1번만 반복되어 매치되지 않음
# "caat"는 "a"가 2번 반복되어 매치

# ca{2,5}t ({m,n} 사이에 반복만 매치)

# "cat"는 "a"가 1번만 반복되어 매치되지 않음
# "caat"는 "a"가 2번 반복되어 매치
# "caaaaat"는  "a"가 5번 반복되어 매치

# ab?c (? == {0,1}와 같은 표현)

# "abc"는 "b"가 1번 사용되어 매치
# "ac"는 "b"가 0번 사용되어 매치

# 정규 표현식 시작하기
# 파이썬에서 정규 표현식을 지원하는 re 모듈

import re

p = re.compile('ab*')

# 패턴 객체를 이용하는 4가지 모듈 
# match 

import re

p = re.compile('[a-z]+')
# a-z 까지 문자열이 1번 이상 반복되는 표현을 찾는 식
m = p.match("python")
# 검사하고 싶은 문자를 넣어준다.

print(m)        ## Result : <re.Match object; span=(0, 6), match='python'>
# 매치가 될 경우 매치 객체를 리턴 해줌

m = p.match("3 python")

print(m)       ## Result : None
# 매치가 되지 않을 경우 None 으로 출력됨

# search

p = re.compile('[a-z]+')
# a-z 까지 문자열이 1번 이상 반복되는 표현을 찾는 식
m = p.search("python")

print(m)        ## Result : <re.Match object; span=(0, 6), match='python'>

m = p.search("3 python")
# match와 달리 일치하는 구문이 존재하면 match 객체를 리턴해줌

print(m)        ## Result : <re.Match object; span=(2, 8), match='python'>

# findalll,finditer

import re

p = re.compile('[a-z]+')
m = p.findall('life is too short')
# findall은 일치하는 것을 찾아 리스트로 리턴해줌.

print(m)        ## Result : ['life', 'is', 'too', 'short']
# 일치하는 str을 리스트에 담아서 출력하였다.

p = re.compile('[a-z]+')
m = p.finditer('life is too short')
# finditer는 match 되는 문자열을 다 match 객체 형태로 반복 가능한 객체 하나로 리턴함

print(m)        ## Result : <callable_iterator object at 0x10b7e3b50>
# 반복 가능한 객체 하나로 리턴함

for r in m:
    print(r)
# <re.Match object; span=(0, 4), match='life'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 17), match='short'> 

# match 객체의 메서드1
# method            목적
# group()       매치된 문자열을 리턴한다.
# start()       매치된 문자열의 시작 위치를 리턴한다.
# end()         매치된 문자열의 끝 위치를 리턴한다.
# span()        매치된 문자열의 (시작, 끝)에 해당되는 튜플을 리턴한다.

import re

p = re.compile('[a-z]+')
m = p.match('python')

print(m.group())        ## Result : python
print(m.start())        ## Result : 0
print(m.end())          ## Result : 6
print(m.span())         ## Result : (0,6)

# 컴파일 옵션 / DOTALL, S

import re

p = re.compile('a.b', re.DOTALL)
# DOTALL은 줄바꿈 문자를 포함하도록 만드는 옵션 약어인 S를 사용하여도 된다.
m = p.match('a\nb')

print(m)        ## Result : <re.Match object; span=(0, 3), match='a\nb'>


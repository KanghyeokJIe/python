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

# IGNORECASE, I

import re

p = re.compile('[a-z]', re.I)
# 대소문자를 무시하고 매칭 시켜주는 옵션

print(p.match('python'))        ## Result : <re.Match object; span=(0, 1), match='p'>
print(p.match('Python'))        ## Result : <re.Match object; span=(0, 1), match='P'>
print(p.match('PYTHON'))        ## Result : <re.Match object; span=(0, 1), match='P'>

# MULTILINE, M

import re

p = re.compile("^python\s\w+", re.M)
# ^는 맨처음, \s는 공백을 \w 는 알파벳, 숫자, _ 를 나타내는 문자이다.
# MULTILINE은 ^를 맨처음이 아닌 각 라인의 처음으로 인식 시키는 옵션

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))      ## Result : ['python one', 'python two', 'python three']

# VERBOSE, X

import re

charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)
# 긴 정규 표현식을 줄바꿈으로 나누어도 컴파일 되게 만들어 주는 옵션

# 백슬래시 문제 

# \section
# p = re.compile('\\section')   \ 가 2개 붙은 표현식을 매칭하려면
# p = re.compile('\\\\section') \ 를 이처럼 4개 사용해야 하게된다.
# p = re.compile(r'\\section') 따라서 백슬래시가 있는 어떤 표현식이 있을 때 
# r을 붙여서 로우스트링으로 백슬래시 두개를 붙여서 표현해주면 정상 작동하게 된다.

# 강력한 정규 표현식의 세계로
# 메타문자 |

import re

p = re.compile('Crow|Servo')
# |는 or 과 같은 뜻이다.
m = p.match('CrowHello')

print(m)        ## Result : <re.Match object; span=(0, 4), match='Crow'>
# Crow 가 겹치기 때문에 매칭 된 값을 리턴 해준다.

# 메타문자 ^

import re
# re 모듈에서 바로 search를 주고 컴파일할 정규표현식(^Life)을 써주고 찾을 문자열(Life is too short) 입력해주면 한줄에 표현 가능하다.

print(re.search('^Life', 'Life is too short'))      ## Result : <re.Match object; span=(0, 4), match='Life'> 
# 맨처음을 나타내는 ^가 있어 Life 가 맨 처음 있기 때문에 결과 값이 출력되었다.

print(re.search('^Life', 'My Life'))        ## Result : None
# My Life는 My가 맨 처음 나왔기 때문에 일치 조건에 일치 하지 않아 None 이 출력되었다.

# 메타문자 $ 

import re

print(re.search('short$','Life is too short'))      ## Result : <re.Match object; span=(12, 17), match='short'>
# 맨끝을 나타내는 $가 있어 맨끝에 short가 있어 결과 값이 출력되었다.

print(re.search('short$','Life is too short, you need python'))     ## Result : None
# 맨끝을 나타내는 $가 있으나 맨끝에 python이 있어 결과 None 이 출력 되었다.

# 메타문자 \b

import re

p = re.compile(r'\bclass\b')
# \b는 공백을 나타내는 메타 문자다.

print(p.search('no class at all'))      ## Result : <re.Match object; span=(3, 8), match='class'>
# 공백을 나타내는 \b가 있어 class 양쪽에 공백이 있는 결과값이 출력되었다.

print(p.search('the declassified algorithm'))     ## Result : None
# 공백을 나타내는 \b가 있지만 class 양쪽에 공백이 없어 None이 출력되었다.

print(p.search('one subclass is'))      ## Result : None
# 공백을 나타내는 \b가 있지만 class 양쪽에 공백이 없어 None이 출력되었다.

# 그룹핑 ()

import re

p = re.compile('(ABC)+')
# 반복되는 문자열(ABC)을 검색하기 위해 그룹핑으로 묶어 주게 되면 반복 되는 문자열을 검색하기 용이하다.
m = p.search('ABCABCABC OK?')

print(m)    ## Result : <re.Match object; span=(0, 9), match='ABCABCABC'>

print(m.group())    ## Result : ABCABCABC

p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")

print(m.group(1))   ## Result : park
# 그룹핑된 첫 번째 그룹을 따로 불러올수 있다.

p = re.compile(r'(\b\w+)\s+\1')
# \1은 정규표현식 내부에서 그룹의 결과를 사용 할 수 있다.
print(p.search('Paris in the the spring '))   ## Result : the the

# 그룹핑된 문자열에 이름 붙이기 ?P<name>

p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
# ?P<name>으로 그룹에 이름을 붙여 쓸 수 있다.
m = p.search("park 010-1234-1234")

print(m.group("name"))    ## Result : park 

import re

p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')

print(p.search('Paris in the the spring').group())    ## Result : the the

# 전방탐색: 긍정형 (?=)

import re

p = re.compile(".+(?=:)")
# :까지의 검색 결과를 도출 하고 싶으나 결과에는 포함 하고 싶지 않을 경우 (?=)을 사용한다.

m = p.search("http://google.com")

print(m.group())    ## Result : http

## 파이썬 프로그래밍의 핵심, 외장함수
# 외장함수란? 라이브러리 함수, import 해서 쓰는 것

# sys.argv

# argv_test.py
import sys
print(sys.argv)

# pickle

import pickle
f = open("test.txt",'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

import pickle
f = open("test.txt",'rb')
data = pickle.load(f)
print(data)
{2:'you need', 1:'python'}

# time

import time
print(time.time())      ## Result : 1613373171.1033266 (함수 작성 기준)
#1970년 1월 1일 0시 0초를 기준으로 지난 시간 초

# time.sleep
#sleep1.py
import time

for i in range(5):
    print(i)
    # 숫자를 5까지 출력하는 함수
    time.sleep(1)
    # 1초씩 쉬면서 출력하는 함수

## Result : 0
#           1
#           2
#           3
#           4

# random

import random

print(random.random())          ## Result : 0.4261820149737079
# 0~1 사이의 난수

print(random.randint(1, 10))        ## Result : 3

data = [1,2,3,4,5]
random.shuffle(data)

print(data)     ## Result : [1, 3, 5, 2, 4]

# 랜덤 함수로 로또 번호 뽑기
lotto = sorted(random.sample(range(1,46), 6))

print(lotto)        ## Result : [1, 12, 24, 26, 29, 45]

# webbrowser

import webbrowser

webbrowser.open("https://google.com")       ## Result : google.com 사이트에 연결 된다.

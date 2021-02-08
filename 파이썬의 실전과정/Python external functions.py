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

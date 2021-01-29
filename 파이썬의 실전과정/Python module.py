## 파이썬 프로그래밍의 핵심, 모듈
# 모듈이란? 미리 만들어 놓은 .py 파일(함수,변수,클래스)

import mod1

print(mod1.add(1,2))        ## Result : 3 / mod1.py 파일에 만들어 둔 함수를 불러서 출력하였다.

# from 모듈이름 import 모듈함수

from mod1 import add

print(add(3,4))         ## Result : 7 / 만약 mod1.py에 여러가지의 함수가 있을 경우
                        ## from 을 이용하여 하나의 함수만 가져와 사용 할 수 있다.

# if __name__=="__main__": 의 의미

import mod1         ## Result : 실행 되지 않는다. / if __name__=="__main__" 을 이용하여
                    # mod1 의 파일에 print 문이 구동 되지 않게 하였다. (main이 아닌 파일의 이름이 되어 실행을 막는 것)

# sys.path.append

import sys
sys.path.append("C:\\Users\\martin\\Desktop\\python\\파이썬의 실전과정") # 파일의 위치가 다른경우 이처럼 추가 하지 않으면 에러가 난다.
import mod1

print(mod1.add(3,4))            ## Result : 7
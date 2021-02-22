## 파이썬 프로그래밍의 핵심, 패키지
# 패키지란? 모듈 여러 개 모아놓은 것

# 테스트를 위해 패키지 만들기

# echo.py 생성

# def echo_test():
#     print("echo")

# render.py 생성

# def render_test():
#     print("render")

# 패키지 안의 함수 실행하기

import game.sound.echo

game.sound.echo.echo_test()         ## Result : echo

# game의 sound 폴더에서 echo 함수만 불러와 실행하기 (from 사용)
from game.sound import echo

echo.echo_test()            ## Result : echo

from game.sound.echo import echo_test as e
# as 를 이용하여 echo_test 함수를 간단히 e 로 줄여서 사용 가능 하다.

e()         ## Result : echo

# __all__

from game.sound import *
# * 를 이용하여 모든 함수를 가져 올 수 있으나 오류가 걸린다.
# __init__.py 폴더에 __all__ = ['echo'] 과 같이 리스트에 지정하여 주면
# * 실행시 사용할 함수를 지정할 수 있다.

echo.echo_test()            ## Result : echo

# relative 패키지

# from ..sound.echo import echo_test
# ..은 상대경로에서 이전 폴더를 의미 한다.

# def render_test():
#     print("render")
#     echo_test()

# 즉 render.py에 sound 폴더 안에 있는 echo_test 함수를 사용할 수 있다.
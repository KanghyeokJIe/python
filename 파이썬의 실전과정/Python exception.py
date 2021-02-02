## 파이썬 프로그래밍의 핵심, 예외 처리
# 예외처리란? 오류가 발생했을 때 어떻게 할지 정하는 것

# try,except문

try:
    4 / 0
except ZeroDivisionError as e1:
    print(e1)                   ## Result : division by zero
    # 에러의 이름이 e에 담겨서 출력이 되었다.

print("Hello World!")           ## Result : Hello World!
# 에러가 생겼음에도 print문이 제대로 작동을 한다.

# try .. else

try:
    f = open('none', 'r')
except FileNotFoundError as e2:
    # none 이라는 파일이 없을 시에 notfounderror 를 출력함
    print(str(e2))
    ## Result : [Errno 2] No such file or directory: 'none'
else:
    # try를 해서 구문에 오류가 없을 때 else문을 실행 한다.
    data = f.read()
    print(data)
    f.close()

# try .. finally

f = open('foo.txt', 'w')

try:
    # 오류가 생길 수 있는 것을 시도하는 것
    data = f.read()
    print(data)
except Exception as e3:
    # 오류 발생시 대처 하는 것
    # Exception 으로 어떠한 에러도 잡을 수 있다.
    print(e3)
    ## Result : not readable
finally:
    # 오류와 상관없이 마지막에 실행 하는 것
    f.close()
    # 파일을 오픈 후에는 무조건 파일을 닫아주어야 한다.
    # 즉 오류와 상관없이 수행 되어야 한다.

# 여러 개의 오류 처리하기

try:
    a = [1,2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    # except 를 이용해서 각각 다르게 오류를 처리 할 수 있다.
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱할 수 없습니다.")
    ## Result : 인덱싱할 수 없습니다.

# 오류 회피하기

try:
    f = open("없는파일", 'r')
except FileNotFoundError:
    pass
    # pass를 넣었기 때문에 아무런 일도 일어나지 않는다.

# 오류 일부러 발생시키기

class Bird:
    def fly(self):
        raise NotImplementedError
        # raise뒤에 NotImplementedError을 적고 구동시 오류를 강제로 발생 시킨다.
class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()         ## Result : very fast

# 부모 클래스(Bird)를 만들고 싶은데 자식클래스(Eagle)가 함수(fly)를 변형해서 사용 하고 싶을때
# raise NotImplementedError 를 통해 강제로 오류를 발생시켜 변형해서 사용을 강제시킨다.
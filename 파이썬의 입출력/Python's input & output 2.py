## 사용자 입력과 출력
# input의 사용

# a = input()           # input Life is too short, you need python

# print(a)          ## Result : Life is too short, you need python / input 함수를 이용해 값을 넣어서 출력 시켰다.

# number = input("숫자를 입력하세요:")          # 숫자를 입력하세요:10

# print(number)         ## Result : 10 / input 함수 안에 인자를 넣을 수 있다.


# print 문의 기능

print("life""is""too short")            ## Result : lifeistoo short / str 문을 자동으로 붙여서 출력 한다.

print("life","is","too short")          ## Result : life is too short / ,를 넣으면 띄어쓰기를 되어 출력 된다.

for i in range(10):
    print(i, end=' ')           ## Result : 0 1 2 3 4 5 6 7 8 9 / i 뒤에 end 라는 인자를 통해 띄어쓰기로 출력 된다.

## 파일 읽고 쓰기
# 파일 생성하기

##      파일열기모드          설명
##      r                읽기모드-파일을 읽기만 할 때 사용
##      w                쓰기모드-파일에 내용을 쓸 때 사용
##      a                추가모드-파일의 마지막에 새로운 내용을 추가 시킬 때 사용

f = open("새파일.txt",'w')
f.close()           ## Result : 새파일.txt라는 파일이 생겼다.

# 파일을 쓰기 모드로 열어 출력값 적기

f = open("새파일.txt", 'w', encoding="UTF-8")

for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()           ## Result : 1-10번째 줄입니다. 가 새파일.txt에 저장되었다.

# readline() 함수

f = open("새파일.txt", 'r', encoding="UTF-8")
line = f.readline()

print(line)         ## Result : 1번째 줄입니다.
f.close()

f = open("새파일.txt", 'r',encoding="UTF-8")

while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
## Result : 1번째 줄입니다.
##
##          2번째 줄입니다.
##          ...
##          10번째 줄입니다.


# readlines() 함수 이용하기

f = open("새파일.txt", 'r',encoding="UTF-8")

lines = f.readlines()
for line in lines:
    print(line)
f.close()
## Result : 1번째 줄입니다.
##
##          2번째 줄입니다.
##          ...
##          10번째 줄입니다.



# read() 함수 이용하기

f = open("새파일.txt", 'r',encoding="UTF-8")
data = f.read()
print(data)
f.close()
## Result : 1번째 줄입니다.
##
##          2번째 줄입니다.
##          ...
##          10번째 줄입니다.

f = open("새파일.txt", 'a', encoding="UTF-8")

for i in range(11,20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
# a함수는 add의 개념으로 새파일.txt에 10번째 줄입니다. 뒤에
# 11번째 줄입니다. 부터 19번째 줄입니다 까지 삽입을 하였다.

# with문과 함께 사용하기

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
# foo.txt 파일에 Life is too short, you need python 문장이 들어가고 f함수가 자동으로 close 되었다.
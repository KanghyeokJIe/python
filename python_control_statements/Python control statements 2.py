## 반복문(while문)
# 열 번 찍어 안 넘어 가는 나무 없다.

treeHit = 0

while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d 번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")
## Result : 나무를 1 번 찍었습니다.
## 나무를 2 번 찍었습니다.
## 나무를 3 번 찍었습니다.
##        ......
## 나무를 9 번 찍었습니다.
## 나무를 10 번 찍었습니다.
## 나무 넘어갑니다. / treeHit 가 0부터 시작해서 1번씩 더해 10이 될때 까지 실행 후 마지막에 나무 넘어갑니다. 를 출력함.

# break, continue

coffee = 10
money = 300

while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
## Result : 돈을 받았으니 커피를 줍니다.
## 남은 커피의 양은 9개 입니다.
## 돈을 받았으니 커피를 줍니다.
## 남은 커피의 양은 8개 입니다.
##         .......
## 남은 커피의 양은 1개 입니다.
## 돈을 받았으니 커피를 줍니다.
## 남은 커피의 양은 0개 입니다.
## 커피가 다 떨어졌습니다. 판매를 중지합니다. / 다 출력 후 money 값은 True 이지만 coffee 값이 False이기에 break 가 걸렸다.

a = 0

while a < 10:
    a = a+1
    if a % 2 == 0:
        continue
    print(a)
## Result : 1
## 3
## 5
## 7
## 9 / a 가 0부터 시작해서 1을 더하고 a 를 2로 나눈 나머지(%)가 0이 되면 continue 를 만나 print(a)를 실행하지 않고 다시
## while 문을 10 까지 실행한다.

# 무한 루프

# while True:
    # print("Hello World!")
## Result : Hello World!
##        ....... / Hello World! 가 무한정 출력 된다.

## 반복문(for문)
# 전형적인 for문

test_list = ['one','two','three']

for i in test_list:
    print(i)
## Result : one
## two
## three / 리스트에 있는 값을 하나씩 꺼내 i에 담아서 print 한 결과다.

# 다양한 for문의 사용

a = [(1,2),(3,4,),(5,6,)]

for (first,last) in a:
    print(first+last)
## Result : 3
## 7
## 11 / a에 있는 값을 first,last 변수에 담아 더해서 출력하였다.

# 60점이 넘으면 합격이고 그렇지 않으면 불합격

marks = [90,25,67,45,80]
number = 0

for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)
## Result : 1번 학생은 합격입니다.
## 2번 학생은 불합격입니다.
## 3번 학생은 합격입니다.
## 4번 학생은 불합격입니다.
## 5번 학생은 합격입니다. / for문에서 number=0 이었으나 for문을 돌리기 전에 1씩 증가 시킨 후
## mark에서 marks로 하나씩 빼와서 if문을 실행하는 것을 반복 한다.

# for문과 continue

marks = [90,25,67,45,80]
number = 0

for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)
## Result : 1번 학생 축하합니다. 합격입니다.
## 3번 학생 축하합니다. 합격입니다.
## 5번 학생 축하합니다. 합격입니다. / 60점 미만인 학생은 continue에 걸려서 다시 if문을 실행하고
## 초과인 학생은 print("%d번 학생 축하합니다. 합격입니다." % number)를 구동시킨다.

# for와 함께 자주 사용하는 range함수

sum = 0

for i in range(1,11):
    sum = sum + i
print(sum)
## Result : 55 / range안에 있는 1이상 11미만에 있는 숫자를 계속 i에 넣고 sum = sum + i 를 실행하여 출력한다.

# 이중 for문(구구단)

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end= " ")
    print('')
## Result :2 4 6 8 10 12 14 16 18
## 3 6 9 12 15 18 21 24 27
## 4 8 12 16 20 24 28 32 36
## 5 10 15 20 25 30 35 40 45
## 6 12 18 24 30 36 42 48 54
## 7 14 21 28 35 42 49 56 63
## 8 16 24 32 40 48 56 64 72
## 9 18 27 36 45 54 63 72 81 / i에 2부터 9까지 값을 j에 1부터 9까지에 값을 곱하여 연속적으로 출력한다.

# 리스트 내포(List comprehension)

# result = [num * 3 for num in a]

# result = []
# for num in a:
#   result.append(num*3)
## 리스트 안에 for문을 넣어서 구동 하는 것이다.

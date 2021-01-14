## 2. 문자열 자료형 표현 방법
# 2.6 슬라이싱 (Slicing)

a = "Life is too short, You need Python"

print (a[0:4])
## Result : Life / [이상:미만:간격] = 첫 글자부터 시작해서 4번 인덱스 전까지 출력.

a = "20010331Rainy"

print (a[:8])
## Result : 20010331 / [이상:미만:간격] = 첫 글자부터 시작해서 8번 인덱스전까지 출력.

print (a[8:])
## Result : Rainy / [이상:미만:간격] = 8번 인덱스 부터 마지막 인덱스까지 출력.

a = "12345678"

print (a[::1])
## Result : 12345678 / [이상:미만:간격] = 첫 인덱스부터 마지막 인덱스까지 한칸 간격으로 출력.

print (a[::2])
## Result : 1357 / [이상:미만:간격] = 첫 인덱스부터 마지막 인덱스까지 두칸 간격으로 출력.

# 2.7 문자열 포매팅

a = "I eat %d apples." %3

print (a)
## Result : I eat 3 apples. / %d 자리에 뒤에 있는 숫자가 들어감.

a = "I eat %d apples." %3
b = "I eat " + str(3) + " apples"

print (b)
## Result : I eat 3 apples. / b로 쓰는 과정이 복잡하니까 a로 쓰기위해 포매팅 사용.

number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number, day)

print (a)
## Result : I ate 10 apples. so I was sick for three days.

a = "hello ! my name is {name} and i'm {age} years old ." .format(name="kanghyeok",age=23)

print (a)
## Result : hello ! my name is kanghyeok and i'm 23 years old .

name = "kanghyeok"
a = f"나의 이름은 {name}입니다."

print (a)
## Result : 나의 이름은 kanghyeok입니다.

# 2.8 정렬과 공백
a = "%10s" % "hi"

print (a)
## Result :         hi / 공백을 둘 수 있다.

# 2.9 소수점 표현

a = "%0.4f" % 3.42134234

print (a)
## Result : 3.4213 / %간격.소수점 남기는 자리 수f 를 이용해 소수점을 제한 할 수 있다.


## 문자열 자료형 표현 방법
# 슬라이싱 (Slicing)

a = "Life is too short, You need Python"

print(a[0:4])           ## Result : Life / [이상:미만:간격] = 첫 글자부터 시작해서 4번 인덱스 전까지 출력.

a = "20010331Rainy"

print(a[:8])            ## Result : 20010331 / [이상:미만:간격] = 첫 글자부터 시작해서 8번 인덱스전까지 출력.

print(a[8:])            ## Result : Rainy / [이상:미만:간격] = 8번 인덱스 부터 마지막 인덱스까지 출력.

a = "12345678"

print(a[::1])           ## Result : 12345678 / [이상:미만:간격] = 첫 인덱스부터 마지막 인덱스까지 한칸 간격으로 출력.

print(a[::2])           ## Result : 1357 / [이상:미만:간격] = 첫 인덱스부터 마지막 인덱스까지 두칸 간격으로 출력.

# 문자열 포매팅

a = "I eat %d apples." %3

print(a)            ## Result : I eat 3 apples. / %d 자리에 뒤에 있는 숫자가 들어감.

a = "I eat %d apples." %3
b = "I eat " + str(3) + " apples"

print(b)            ## Result : I eat 3 apples. / b로 쓰는 과정이 복잡하니까 a로 쓰기위해 포매팅 사용.

number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number, day)

print(a)            ## Result : I ate 10 apples. so I was sick for three days.

a = "hello ! my name is {name} and i'm {age} years old ." .format(name="kanghyeok",age=23)

print(a)            ## Result : hello ! my name is kanghyeok and i'm 23 years old .

name = "kanghyeok"
a = f"나의 이름은 {name}입니다."

print(a)            ## Result : 나의 이름은 kanghyeok입니다.

# 정렬과 공백
a = "%10s" % "hi"

print(a)            ## Result :         hi / 공백을 둘 수 있다.

# 소수점 표현

a = "%0.4f" % 3.42134234

print(a)            ## Result : 3.4213 / %간격.소수점 남기는 자리 수f 를 이용해 소수점을 제한 할 수 있다.

# 문자열 개수 세기 (count)

a = "hobby"

print(a.count('b'))         ## Result : 2 / a 변수에서 b 가 몇 개 있는지 카운트 하여준다.

print(a.find('b'))          ## Result : 2 / 가장 먼저 나오는 b의 인덱스를 찾아 리턴 하여준다.

print(a.find('x'))          ## Result : -1 / 찾는 값이 존재 하지 않을 경우 -1 을 리턴한다.

# 문자열 삽입(join)

a = ",".join("abcd")

print(a)            ## Result : a,b,c,d / abcd에 ,라는 문자열을 삽입 한다.

# 대,소문자를 각각 변환하기, 양쪽 공백 지우기(upper,lower,strip)

a = "hi"
a = "HI"
print(a.upper())            ## Result : HI / upper 를 이용하여 소문자를 대문자로 변경.
print(a.lower())            ## Result : hi / lower 를 이용하여 대문자를 소문자로 변경.

a = "   HI  "

print(a.strip())            ## Result : HI / strip 를 이용하여 공백을 삭제 시킴.

# 문자열 바꾸기,나누기(replace,split)

a = "Life is too short"

print(a.replace("Life", "Your leg"))            ## Result : Your leg is too short / replace 함수를 이용하여 Life를 Your leg으로 교체한다.

print(a.split())            ## Result : ['Life', 'is', 'too', 'short'] / 문자열 자료형을 띄어쓰기 기준으로 자르는 함수.
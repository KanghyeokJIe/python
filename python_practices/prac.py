# 백준 10171번 

print('''\\    /\\''')
print(''' )  ( ')''')
print('''(  /  )''')
print(''' \\(__)|''')
# \를 출력할 때는 \를 두번 입력 해야한다.

# 백준 10172번 

print('''|\\_/|''')
print('''|q p|   /}''')
print('''( 0 )"""\\''')
print('''|"^"`    |''')
print('''||_/=\\\\__|''')

# 백준 1000번 

a, b = input().split()
a = int(a)
b = int(b)
print(a+b)

# 백준 1001번 

a, b = input().split()
a = int(a)
b = int(b)
print(a-b)

# 백준 10998번 

a, b = input().split()
a = int(a)
b = int(b)
print(a*b)

# 백준 1008번 

a, b = input().split()
a = int(a)
b = int(b)
print(a/b)

# 백준 10869번 

a, b = input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

# 백준 10430번 

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print((a+b)%c)
print((a%c + b%c)%c)
print((a*b)%c)
print((a%c * b%c)%c)

# 백준 2588번 

a = int(input())
b = input()

c = a * int(b[2])
d = a * int(b[1])
e = a * int(b[0])
f = a * int(b)

print(c,d,e,f,sep='\n')

# 백준 1330번 

a, b = map(int, input().split())

if (a > b):
    print('>')
elif (a == b):
    print('==')
else:
    print('<')

# 백준 9498번

num = int(input())

if 90 <= num <= 100:
    print('A')
elif 80 <= num <= 89:
    print('B')
elif 70 <= num <= 79:
    print('C')
elif 60 <= num <= 69:
    print('D')
else:
    print('F')

# 백준 2753번


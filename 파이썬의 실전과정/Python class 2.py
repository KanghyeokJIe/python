## 클래스의 상속

class FourCal:          # 부모 클래스
    def __init__(self,fiist,second):
        self.first = fiist
        self.second = second
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal):         # 부모 클래스를 MoreFourCal 클래스에 상속 시킨다.
    pass

a = MoreFourCal(4,2)
print(a.add())          ## Result : 6 부모클래스가 만든 클래스를 자식 클래스를 적용 할 수 있다.

## 클래스의 상속 2 - 메서드 추가

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a=MoreFourCal(4,2)
print(a.pow())          ## Result : 16 부모 클래스에 새로운 메서드를 추가 한다.

## 메서드 오버라이딩

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:    # 두번째 입력값이 0인경우 부모 클래스의 함수를 무시하고 실행됨.
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4,0)
print(a.div())
## Result : 0 원래는 에러가 나야 하지만 자식클래스의 함수가 부모클래스의 함수를 덮어
# 에러가 나지 않고 0으로 출력이 되었다.

## 클래스 변수, 객체 변수
# 공통으로 사용 할 때는 클래스 변수를 사용하고, 각각 객체마다 다르게 지정 할 경우 객체 변수를 사용한다.

class Family:
    lastname = "김"          # 클래스 변수에 "김" 이라고 지정하였다.

Family.lastname = "박"       # 클래스 변수를 "박"으로 바꾸었기 때문에 모든 lastname값이 박으로 출력 되었다.

print(Family.lastname)      ## Result : 박

a = Family()
b = Family()

print(a.lastname)           ## Result : 박
print(a.lastname)           ## Result : 박
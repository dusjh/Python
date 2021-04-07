# 연주홍_2주차시험답안.py

# 1번문제-------------------------------------------------------------------------
class BankAccount:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0},{1},{2}".format(self.__id, self.__name, self.__balance)

account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
print(account1)


# 2번 문제-------------------------------------------------------------------------
class Developer:
    def __init__(self,name):
        self.name = name 
    def getSalary(self,day):
        result = day * 100000
        print("개발자 월급:", result)

dev = Developer("홍길동")
dev.getSalary(20)


# 3번 문제-------------------------------------------------------------------------
class WebDeveloper(Developer):
    def __init__(self,name,skill):
        Developer.__init__(self,name)
        self.skill = skill
    def getSalary(self,day):
        result = day * 200000
        print("웹 개발자 월급:", result)

webDev = WebDeveloper("이순신", "ASP.NET")
webDev.getSalary(20)


# 4번 문제-------------------------------------------------------------------------
# 함수 클래스 모듈 패키지
# 1) 함수: 함수는 직접 만들 수 있고, 이미 파이썬에 내장되어 있는 것도 있다. 함수 선언은  def로 시작해서 콜론(:)으로 끝내고,
# 함수의 시작과 끝은 코드의 들여쓰기로 구분한다. 시작과 끝은 명시하지 않는다.
# 함수 선언을 헤더파일에 미리 선언하거나, 인터페이스와 구현으로 나누지 않고 필요할 때 바로 선언하고 사용할 수 있다.

# 2) 클래스: 파이썬에 내장디ㅗ어 있는 클래스들이 있지만, 사용자가 필요하면 자기만의 형식을 정의해서 사용할 수 있다.
# 일반적으로 클래스는 데이터와 메서드로 구성되어 있다.

# 3) 모듈: 모듈은 여러 코드를 묶어 다른 곳에 재사용 할 수 있는 코드 모음을 말한다. (하나의 파일로 저장된 물리적인 파일)
# 파이썬에는 많은 내장 모듈이 있지만 사용자가 직접 모듈을 생성할 수 있다. 
# 모듈은 메모리에 한번, 하나만 로딩되고 이를 참고하는 여러 개의 레퍼런스가 있다.
# 모듈 임포트 시 파이썬에서는 import구문을 어디서나 사용할 수 있다.

# 4) 패키지: 하나의 파일에 모든 함수와 클래스를 저장할 수 있다면 모듈을 사용한다. 
# 그러나 복잡한 경우는 여러 개의 모듈을 포함하는 패키지(폴더 형태)로 구현한다. urllib패키지 내부에 있는 다양한 모듈을 볼 수 있다.


# 5번 문제-------------------------------------------------------------------------
import re
bool(re.search("\d{5}","우편번호: 34567"))

# -*- 생성자와 소멸자 -*-
import sys

class MyClass:
    # 생생자 필수
    def __init__(self, value):
        self.value = value
        print("Instace is created! value = ", value)
    # 소멸자는 유명무실함(쓰는 경우는 별로 없음)
    def __del__(self):
        print("Instance is deleted!")

# 인스턴스 생성
d = MyClass(5)
#d_copy = d   # 무조건 참조 복사
print("참조 횟수: {0}".format(sys.getrefcount(d)))
#del d_copy
#del d

print("전체 코드 실행 종료")
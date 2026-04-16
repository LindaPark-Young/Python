#Tuple
"""
tuple는 일련번호로 구분되는 순서에 따라 데이터가 정렬
된 목록 형태의 자료형
•tuple은 문자열, 정수, 실수 등 모든 자료형을 섞어서 저
장할 수 있음
•list와 달리 내용을 변경 할수 없음(immutable)
•()를 사용함


student = ('전정국', '인공지능학과', 3, 175.3, 3.5, True)
print(student)
print(student[0])
car = ('Tesla', 'model3', 'red', 500)
print(car)


#range를 이용한 tuple 생성

#range1 = range(10)
#tuple1 = tuple(range1)
#print(tuple1)

# input
#사용자의 입력을 받을때 사용
#입력값은 문자열로 반환

input("프롬프트 문자열")
age = input('나이를 입력하시오')
print(age)
num = 3
diff = input('변화량을 입력하시오')
print(num + diff)
"""
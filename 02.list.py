"""
list
•list는 일련번호로 구분되는 순서에 따
라 데이터가 정렬된 목록 형태의 자료
형
•리스트는 문자열, 정수, 실수 등 모든
자료형을 섞어서 저장할 수 있음
score01=30
score02=50
score03=90
.
.
score30=89
•리스트의 값은 변경가능(mutable)


scores = [30, 50, 90, 89, 56, 87 ]
score0 = scores[0]
print(score0)
print(scores[5])
print(scores[-1])
print(scores[-3])
scores[1] = 100
print(scores)

list활용
•list는 +, * 연산자 사용가능


scores.append(99)
scores.append('Hello')
scores.insert(1, 33)
scores.insert(2, 'World')
print(scores)

"""

list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
print(list1 + list2)
print(list2 + list1)
print(list1 *3 )
print(list2 *3 )
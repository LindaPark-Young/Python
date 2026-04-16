# 딕셔너리
# 생성
"""
dic1 = {} #빈 딕셔너리 생성
print(dic1)

dic2 = dict() #생성자를 이용해서 딕셔어리 생성
print(dic2)
dic3 = {'name': 'item', 1:3.5, False:[1,2,3]}
print(dic3)
dic4 = dict(name='홍길동', height=180, age=20)
print(dic4)

# 아이템 값가져오기
student = {'name': '홍길동', 'major': '정통과', 'score':3.5}
print(student['name'])
print(student['score'])
scores = {1:3.5, 2:4.0, 3:4.3, 4:4.2}
print(scores[1])
print(scores[2])



#아이템 수정, 추가
student = {'name': '홍길동', 'major': '정통과', 'score':3.5}
student['major'] ='정보통신과'
print(student)
student['grade'] = 4
print(student)

# 아이템 삭제
del student['name']
print(student)


"""

#Key, Value 가져오기
student = {'name': '홍길동', 'major': '정통과', 'score':3.5}

print(list(student.items())) #[('name', '홍길동'), ('major', '정통과'), ('score', 3.5)]
print(list(student.keys())) # ['name', 'major', 'score']
print(list(student.values())) # ['홍길동', '정통과', 3.5]
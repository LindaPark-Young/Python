#if 조건문
"""
adult = 18
age = 17
if age < adult :
    print('당신은 미성년자입니다.')
    print('당신은 입장할 수 없습니다.')

#if~else 조건문

if age < adult :
    print('당신은 미성년자입니다.')
else :
    print('당신은 성인입니다.')

gender = 'male'
if gender == 'male' :
    print('당신은 남자입니다.')
else :
    print('당신은 남자가 아닙니다.')

#if~elif

score = 90
if score >= 90:
    result = 'A'
elif score >= 80:
    result = 'B'
elif score >= 70:
    result = 'C'
elif score >= 60:
    result = 'D'
else :
    result = 'F'
print(result)


#for ~ in 구문
for i in range(10):
    print('Hello World!')

print('===================')
for i in range(1, 10):
    print('Hello World!')

for i in range(10, 0, -1):
    print(i)

print('===================')





# for ~ in 구문
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 10]
for num in list1:
    print(num)

fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)

  

#for ~ in 구문
#input 함수를 이용해서 입력받은 횟수만큼 반복
str_count = input('반복할 횟수를 입력하세요:')
count = int(str_count)

for i in range(count):
    print('Hello, world!', i)






# 구구단 출력

gugu = input('단을 작성하세요:')
dan = int(gugu)

for i in range(1 , 10):
    print(' {} X {} = {}'.format(dan, i, dan * i))
   
 """

for i in range(10):
    if i % 2 == 0 :
        continue
    print('{}'.format(i))
    



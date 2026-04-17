#클래스의 정의
"""
class Person:
    def hello(self):
        print('Hello')

person = Person()
person.hello()
person1 = Person()
person1.hello()




# 속성 정의

class Person:
    def __init__(self):
        self.hi = 'Hello'
    def hello(self):
        print(self.hi)
    

person = Person()
person.hello()
print(person.hi)




# 속성 정의와 초기화

class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def hello(self):
        print('Hello {}'.format(self.name))
        print('당신은 {}살입니다.'.format(self.age))

Person = Person('홍길동', 20)
Person.hello()



클래스 정의 실습
• 학생 클래스를 정의하라.
• 학년, 반, 이름의 세 가지 속성을 가진다.
• 속성은 생성자를 통해서 설정된다.
• '몇학년 몇반 누구입니다.' 라고 출력하는 introduce
라는 메소드를 정의하라

class Student:
    def __init__(self, grade, cla, name):
        self.gra =  grade
        self.cl = cla
        self.na = name
        
    def intro(self):
        print(' {}학년 {}반 {}입니다.'.format(self.gra, self.cl, self.na))

st = Student(3, 2, '이나나')
st.intro()



#비공개 속성 정의


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def hello(self):
        print('Hello {}'.format(self.name))
        print('당신은 {}살입니다.'.format(self.__age))

person = Person('홍길동', 20)
person.hello()
print(person.__age)
person.__age = 100



#비공개 속성 사용
class Person:
    def __init__(self, name, age):
        self.name = name
        if 0 <= age <= 20: self.__age = age
        else: self.__age = 0
    def inc_age(self):
        self.__age += 1
    def info(self):
        print(self.__age)
person = Person('홍길동', 20)
person.inc_age()
person.info()


# 클래스 속성 사용
#클래스(class) 메서드 정의
#정적(static) 메서드 정의




class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def sub(a, b):
        return a - b
print(Math.add(4,5))
print(Math.sub(9,5))



class squ:
    def __init__(self, width, height):
         self.width = width
         self.height = height
    def area(self):
         return self.width * self.height
    
    def double(self):
        self.width *= 2
        self.height *= 2

rect = squ(10, 20)
print(rect.area())
rect.double()
print(rect.width, rect.height)






class Vehicle:
    def __init__(self, speed):
        self.speed = speed
    
    def speed_up(self):
        self.speed += 10
    def speed_dn(self):
        self.speed -= 10


#===============================

class Car(Vehicle):
    def __init__(self, speed, wheels, seats):
        Vehicle.__init__(self, speed)
        self.wheels = wheels
        self.seats = seats

    def info(self):
         print(self.speed, self.wheels, self.seats)

car = Car(100, 4, 4)
car.speed_up()
car.info()

#================================
class Truck(Car):
    def __init__(self, speed, wheels, seats, loadage):
        Car.__init__(self,speed, wheels, seats)
        self.loadage = loadage

    def load(self):
        print('load')
    
    
    def unload(self):
        print('unload')

    def info(self):
        print(self.speed, self.wheels, self.seats, self.loadage)

truck = Truck(100, 6, 2, 30)
truck.load()
truck.unload()
car.info()
truck.info()

#참조변수랑 인스턴스 관계

#======== 내장 함수 ==========
"""

"""
max_value = max(1, 30, 50)
print(max_value)

min_value = min(1, 30, 50)
print(min_value)

max_str = max('AAC', 'ABC', 'ACC')
print(max_str)

min_str = min('AAC', 'ABC', 'ACC')
print(min_str)

#============================


length = len("안녕하세요")
print(length)

result = eval("10+20+30+40")
print(result)

result = eval("not 40>50")
print(result)

list = [2, 5, 5, 3, 9, 1]
result = sorted(list)
print(result)


#========================
str1 = "안녕하세요"
str_id = id(str1)
print(str_id)

list_id = id([1,2,3,4,5])
print(hex(list_id))
print(oct(list_id))

print(type(3.14))
print(type([1,2,3,4,5]))

print(abs(-5))
        

#====== 내장모듈 활용 - datetime ============
print('===============')
import datetime

today = datetime.date.today()
print(today)

now = datetime.datetime.now()
print(now)

print(now.year)

print(now.month)

print(now.day)

dir(datetime)



print('========================')
import datetime as dt


today = dt.date.today()
print(today)


now = dt.datetime.now()
print(now)

know = now + dt.timedelta(hours=9)
print(know)

time_diff = know - now
print(time_diff)

 
print('========================')
from datetime import datetime, date

xmas1 = datetime(2023, 12, 25, 0, 0, 0)
print(xmas1)

# 내장모듈 활용 - time
 
#===내장모듈 활용 - random

import random

print(random.random())# 0~1미만의 실수 난수 발생
print(random.randrange(1, 7)) #1~6까지의 정수 난수 발생
print(random.randint(1, 7)) #1~7까지의 정수 난수 발생

list1 = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(list1) # list의 아이템 순서를 바꿈
print(list1)

print(random.choice(list1)) # list의 아이템 중 하나를 임의로 선택

print(random.sample(list1, 5)) # list의 아이템 중 5개의 아이템을 임의로 선택
print(random.sample(list1, 3)) # list의 아이템 중 5개의 아이템을임의로 선택

# ramdom 모듈을 이용해서 두 가지 방법으로 lotto 발생 함수 만들기


set1 = set()
while len(set1) < 6 :
    set1.add(random.randint(1, 45))

print(set1)
result = sorted(set1)
print(type(result))
print(result)

# shuffle 함수 이용

list1 = list(range(1, 46))
random.shuffle(list1)
result = list1[0:6]
result.sort()
print(result)

list1 = list(range(1, 46))
result = random.sample(list1, 6)
result.sort()
print(result)


#내장모듈 활용 - os
import os


dir(os)
print(os.sep) # 경로구분자

cur_dir = os.getcwd() # 현재 작업경로
print(cur_dir)
print('=======================')
test_dir = os.path.join(cur_dir, 'text') # 경로 생성
print(test_dir)

cur_dir = os.getcwd() # 현재 작업경로
print(cur_dir)
print(os.path.exists(test_dir)) #경로 유무
if not os.path.exists(test_dir):
    os.mkdir(test_dir) #디렉터리 생성
print(os.path.exists(test_dir))


#====== file 읽기 ==============

with open('test.txt', 'r+') as f:
    text = f.read()
    print(text)
    """

# 디렉토리 만들어보기

"""

# 예외처리
str1 = input('피젯수를 입력하시오')
str2 = input('젯수를 입력하시오')

try:
    num1 = int(str1)
    num2 = int(str2)
    result = num1 / num2
    print('{}/{} = {}'.format(num1, num2, num1/num2))
except:
    print('입력값을 확인하시오')


str1 = input('피젯수를 입력하시오')
str2 = input('젯수를 입력하시오')

try:
    num1 = int(str1)
    num2 = int(str2)
    result = num1 / num2
    print('{}/{} = {}'.format(num1, num2, num1/num2))
except Exception as e:
    print("exception:", e)

except ValueError:
    print(' 숫자를 입력하시오.')
except ZeroDivisionError:
    print('0으로 나눌수 없습니다.')
except Exception as e:
    print('excpetion:', e)


str1 = input('젯수를 입력하시오.')
str2 = input('피젯수를 입력하시오.')
try:
    num1 = int(str1)
    num2 = int(str2)
    result = num1 / num2
except Exception as e:
    print("excpetion:", e)
else :
    print('{}/{} = {}'.format(num1, num2, num1/num2))
finally:
    print('처리가 완료되었습니다.')

"""

# ====== 람다 =========

# def add(x, y):
#     return x + y

# f = lambda x, y: x + y

# print(add(1,2))
# print(f(1,2))
# text = "안녕하세요.\n 파이썬입니다.\n 반갑습니다."
# with open('test1.txt', 'w') as f:
#    f.write(text)

# def add(x,y):
#     return x + y

# f = lambda x, y: x + y

# print(add(1,2))
# print(f(1,2))

# f = lambda x: x if x % 3 ==0 else 0

# print(f(3))
# print(f(4))

# # 맵(map) 함수 사용 전역함수
# nums = [1, 2, 3, 4, 5]
# def pow(x):
#     return x ** 2
# f = lambda x: x**2
# print(list(map(pow, nums)))
# print(list(map(f, nums)))
# print(list(map(lambda x: x**2, nums)))

# # 맵(map) 함수 사용
# nums1 = [1, 2, 3, 4, 5]
# nums2 = [6, 7, 8, 9, 10]

# print(list(map(lambda x, y: x*y, nums1, nums2)))


# # 실습해보기 
# map과 lambda를 이용해서 1~10 list의 각 아이템에 5배를
# 가진 list를 만들고 출력하시오.



# 필터(filter) 함수
# ages = [18, 19, 39, 12, 43, 13, 21, 25]

# def adult_func(age):
#     if age >= 19:
#         return True
#     else:
#         return False
    
# for age in filter(adult_func, ages):
#     print(age)

# print()
# for age in filter(lambda age: age >= 19, ages):
#     print(age)

# ages = [18, 19, 39, 12, 43, 13, 21, 25]

# adult_ages = list(filter(lambda age: age >= 19, ages))

# print(adult_ages)

# 실습
# 1 부터 10 사이의 정수를 가진 리스트에서 짝수만 나오게 필
# 터링한 결과 리스트의 모든 원소에 대해 제곱을 수행해서 리
# 스트로 반환하는 코드를 필터와 맵과 람다를 이용해서 작성
# 하시요.

# nums = list(range(1,11))
# result = list(map(lambda x: x**2, filter(lambda num: num % 2 == 0, nums)))
# print(result)
#from functools import reduce

# nums = [1, 2, 3, 4]
# sum = reduce(lambda x, y: x+y, nums )
# print(sum)

# mul = reduce(lambda x, y: x*y, nums)
# print(mul)

# 실습
# 1부터 10 사이의 정수를 가진 리스트에서 짝수만 나오게 필
# 터링한 결과 리스트의 모든 원소의 곱을 구하는 코드를
# lambda, filter, reduce 함수를 사용해서 작성하시요.

# from functools import reduce

# nums = list(range(1, 10))
# result = reduce(lambda x, y: x*y,
# filter(lambda num: num %2 == 0, nums))

# print(result)

#====
# from functools import reduce

# nums = list(range(1, 10))
# fresult = filter(filter(lambda num: num %2 == 0, nums))
# result = reduce(lambda x, y: x*y,)

# print(result)



# # list축약표현
# list1 = list(range(1,10))

# list2 = list(map(lambda x: x**2, list1))
# print(list2)

# list3 = [x**2 for x in list1]
# print(list3)

# list4 = [x**2 for x in range(1, 10)]
# print(list4)

# # 조건문에 따라 5보다 큰 값만 필텨링
# list5 = [x**2 for x in list1 if x>5]
# print(list5)

# # 짝수 값만 필터링
# list6 = [x**2 for x in range(1, 10) if x%2==0]
# print(list6)

# 실습
# 축약표현으로 다음의 리스트를 만드시오.
# 1. 1~10까지 숫자의 제곱을 포함하는 리스트

list6 = list(range(1, 11)) 
list7 = list(map(lambda x: x**2, list6))
print(list7)

list8 = [ x for x in range(1,21) if x%2==0]

# 2. 1~20까지의 짝수를 포함하는 리스트
# 3. 1~20까지의 숫자중 3의 배수를 포함하는 리스트
# 4. 1~20까지의 숫자중 5의 배수의 제곱을 포함하는 리스트







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


"""



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

        
 













#함수 Function
"""
•프로그램의 기본적인 구성요소
•어떤 작업을 수행하는 문장의 그룹
•하나의 프로그램은 여러 개의 함수들이 모여서 이루어진다
•프로그램에서 레고 블럭과 같은 요소
•가독성의 증대, 유지관리가 쉽다.



def hello():
    print('Hello World')
hello() #함수 호출


def hello1(name):
    print('Hello World', name)
hello1('홍길동') #함수 호출
hello1('트와이스')


# 가변 매개변수가 있는 함수, *를 사용
def hello4(greeting, *names):
    for name in names:
        print(greeting, name)
hello4('안녕', "진", "슈가", "제이홉", "RM", "지민")



# 함수 호출시 매개변수명을 사용

def function(first, second, third):
    return first + second + third
print(function(3,5,7))
print(function(first=3, second=5, third=7))
print(function(second=5, first=3, third=7))




#  함수 정의
def function1(first=1, second=3, third=5):
    return first + second + third

print(function1())
print(function1(1,2,3))
print(function1(1,2))
print(function1(1))
print(function1(first=1))


def function1(first, second, third=5):
    return first + second + third

print(function1(1,2,3))
print(function1(first=1, second=2, third=10))
print(function1(1, second=5))
print(function1(second=5, first=2))



#반환형이 콜렉션일때 unpacking

def function():
    return 1, "Hello", True

a, b, c = function()
print(a, b, c)
a = function()
print(a)


def ret_list():
    return[1, 2]
l = ret_list()
print(l)

n1, n2 = ret_list()
print(n1, n2)

n1, _ = ret_list()
print(n1)


def ret_tuple():
    return (1,2)
t = ret_tuple()
print(t)
n1, n2 = ret_tuple()
print(n1, n2)
n1,_ = ret_tuple()
print(n1)
"""

def fun2(fir, sec):
    a = fir // sec
    b = fir % sec
    return(a, b)
t = fun2(25, 6)
print(t)

a, b = fun2(25, 6)
print(a, b)

a, _ = fun2(25,6)
print(a)

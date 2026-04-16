

"""
type(10)
print(type)

num = 3
print(num+5)


print('Hello'+ 'World!')


num = 4
print(num)

print( 5 < 6 )
print( 5 > 6 )
print( 11 <= 11 )
#print( 11 != 5 )
print( 'Hello' > 'World!')
result = 13==4
print(result)

print('==========')
print(True and True)
print(True or False)
print(5 <6 and True)
num1=3
num2=5
print(not(num1>num2))


age = 10
if age == 10:
    print('10살')
    print('입니다.')
print('여기는 다른 블럭입니다.')

age = 20
name = '홍길동'
print('이름은', name, '나이는', age)
print('이름은' + name + '나이는' +str(age))

# string. format()

str1 = "{}".format(10)
print(str1)

str2 = "{}과 {}".format(10, 20)
print(str2)

age = 20
name = ' 홍길동 '
str4 = '이름은 {} 나이는 {}'.format(name, age)
print(str4)

str5 ='이름은 {0} 나이는 {1}'.format(name, age)
print(str5)

str6 ='이름은 {1} 나이는 {0}'.format(age, name)
print(str6)

print('이름은 {1} 나이는 {0}'.format(age, name))


age = 20
name = ' 홍길동 '
str7 = '이름은 {:s} 나이는 {:d}'.format(name , age)
print(str7)
"""
age = 20
name = ' 홍길동 '
print('pi = {:f}'.format(3.141592))  # pi = 3.141592
# :f → 기본 실수(float) 출력
# 기본적으로 소수점 아래 6자리까지 출력
print('pi = {:10f}'.format(3.141592)) #pi =   3.141592
#10 → 전체 자리수(width)를 10칸으로 맞춤
#숫자가 10칸보다 작으면 왼쪽에 공백 추가


# string 서식 지정자
print('이름은 %s 나이는 %d'%(name ,age))
print('이름은 %s 나이는 %5d'%(name, age))
print('이름은 %s 나이는 %05d'%(name, age)) #이름은  홍길동  나이는 00020
#정수를 5자리로 만들고 빈자리는 0으로 채움

print('pi = %f'%3.141592)
print('pi = %5.2f'%3.141592) #pi =  3.14
#5 → 전체 자리수 최소 5칸
#.2 → 소수점 아래 2자리까지 표시 (반올림됨)
#f → 실수 형식


print('pi = %.2f'%3.141592)#pi = 3.14
#소수점 아래 2자리까지 출력


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

"""
age = 20
name = ' 홍길동 '
str7 = '이름은 {:s} 나이는 {:d}'.format(name , age)
print(str7)

print('pi = {:f}'.format(3.141592))
print('pi = {:10f}'.format(3.141592))

# string 서식 지정자
print('이름은 %s 나이는 %d'%(name ,age))
print('이름은 %s 나이는 %5d'%(name, age))
print('이름은 %s 나이는 %05d'%(name, age))
print('pi = %f'%3.141592)
print('pi = %5.2f'%3.141592)
print('pi = %.2f'%3.141592)
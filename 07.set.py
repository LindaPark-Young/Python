"""

Set
•중복되지 않은 데이터들이 모인 집합 형태의 자료형
•순서가 없음
•{ } 를 사용하고 아이템들은 ‘,’(쉼표)로 구분





#packing, unpacking

nums = 1,2,3 # packing
print(nums)
print(type(nums))
num1, num2, num3 = nums # unpacking
print(num1, num2, num3)


#unpacking
nums = [1, 2, 3, 4, 5]

num1, num2, num3, num4, num5 = nums
print(num1, num2, num3, num4, num5)

num1, num2, *num3 = nums
print(num1, num2, num3)

nums = (1, 2, 3)
num1, num2, num3 = nums
print(num1, num2, num3)

num1, num2, _ = nums
print(num1, num2)


_, _, num3 = nums
print(num3)

"""
student = {'name': '홍길동', 'major': '정통과', 'grade':3}
a, b, c = student
print(a, b, c)

set1 = {1, 2, 3, 4}
a, *b, c = set1
print(a, b, c)
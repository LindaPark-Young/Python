# range()
"""
range([start], stop, [step])
# start, step 생략가능
# start의 기본값 0
# step의 기본값 1
# 범위를 생성할때 stop값은 포함되지 않음

"""

#range(10)
#r1 = range(10)
#range(1, 10)
#r2 = range(1, 10)
#print(r1)

#print(r2)

# 10 ~ 1까지 1씩 감소하는 범위
#r4 =range(10, 0, -1)
#print(r4)

#r5 = range(10, 0, -2)
#print(r5)

#range를 이용한 list 생성

list1 = list(range(10))
print(list1)

list2 = list(range(1, 10))
print(list2)

list3 = list(range(1, 10, 2))
print(list3)

list4 = list(range(10, 0, -1))
print(list4)


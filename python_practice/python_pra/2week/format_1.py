# 일반
"""
name="hyuck";age=24
print(name,"님의 나이는",age,"입니다.")

# C 스타일
print("%s님의 나이는 %d입니다."%("hyuck",24))

# Python 스타일
print("{}님의 나이는 {}입니다.".format("hyuck",24))
"""

# C 스타일
print("%s님의 나이는 %.2f입니다."%("hyuck",23.5))

# Python 스타일
print("{}님의 나이는 {:.2f}입니다.".format("hyuck",23.5))

# 10000원, 200000원(C스타일)
print("%10d원 \n%10d원"%(10000, 200000))

# 10000원, 200000원(Python)
print("{:10}원 \n{:10}원".format(10000, 200000))

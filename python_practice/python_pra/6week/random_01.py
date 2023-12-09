from random import random

# 0.0 ~ 1.0 미만의 임의의 값 생성
print("0.0 ~ 1.0 미만의 임의의 값 생성", random())

# 0.0 ~ 10.0 미만의 임의의 값 생성
print("0.0 ~ 10.0 미만의 임의의 값 생성", random()*10)

# 0 ~ 10 미만의 임의의 정수 값 생성
print("0 ~ 10 미만의 임의의 값 생성", int(random()*10))

# 1 ~ 10 까지의 임의의 정수 값 생성
print("1 ~ 10 까지의 임의의 값 생성", int(random()*10)+1)

# 1 ~ 45 까지의 임의의 값 출력
print("1 ~ 45 까지의 임의의 값 생성", int(random()*45)+1)

# 1 ~ 45 까지의 임의의 값 6개 출력
for i in range(6):
    print(int(random()*45)+1)

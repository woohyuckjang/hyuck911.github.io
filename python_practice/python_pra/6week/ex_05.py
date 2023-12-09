# 숫자 맞추기
'''
while 시도횟수 < 10:
    숫자 입력받기
    시도횟수 증가
    판별
'''

import random
tries = 0 #시도횟수
aa = int(input("난이도 선택 : 1.상 100, 2.중 50, 3.하 10 => "))
if aa == 1:
    n = 100
elif aa == 2:
    n = 50
elif aa == 3:
    n = 10
else:
    print("error")
com = random.randint(1, n) # 1~100
print("1~%d사이 숫자 맞추기"%n)

while tries<10:
    player = int(input("숫자 입력 : "))
    tries += 1
    if com < player:
        print("down")
    elif com > player:
        print("up")
    else:
        break
if com == player:
    print("ok count =", tries)
else:
    print("answer =", com)

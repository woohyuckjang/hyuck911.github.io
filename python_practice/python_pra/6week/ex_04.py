import random
'''

2. 숫자 추측 프로그램
컴퓨터 = 숫자
사용자 = 맞추기
3-1. 시도 횟수 제한 5, 몇번에 맞췄냐
3-2 몇번에 맞췄냐
'''
count = 0
com = random.randrange(1,11)
print("com:",com)
print("1~10 숫자맞추기")

for i in range(5): #시도 횟수 제한 5
    player=int(input("숫자 입력 : "))


if com==player:
    print("player Win")
elif com>player: # com이 크다
    print("작다")
else:
    print("크다")

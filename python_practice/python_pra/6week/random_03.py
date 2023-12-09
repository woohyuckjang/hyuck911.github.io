import random

# random.randrange(시작, 끝+1):시작부터 끝-1까지
# random.randint(0,9):0~9까지 무작위 정수

# 7번 2개씩
# 1. 두 사람이 주사위를 던져서 높은 숫자가 나오면 이김
player_1 = random.randrange(1,7)
print("palyer1 : %d"%player_1)
#print("player1 : {}".format(player_1))
player_2 = random.randrange(1,7)
print("palyer2 : %d"%player_2)
# print("player2 : {}".format(player_2))

if player_1 > player_2:
    print("player1 Win")
elif player_1 < player_2:
    print("player2 Win")
else:
    print("player1 == player2")

# 2. 두 사람이 주사위를 2번씩 던져서 합한 숫자로 체크
a1 = random.randrange(1,7)
a2 = random.randrange(1,7)
player_1 = a1 + a2
print("A -> 1 : %d, 2: %d, tot: %d" % (a1, a2, player_1))

b1 = random.randrange(1,7)
b2 = random.randrange(1,7)
player_2 = b1 + b2
print("B -> 1 : %d, 2: %d, tot: %d" % (b1, b2, player_2))


if player_1 > player_2:
    print("player1 Win")
elif player_1 < player_2:
    print("player2 Win")
else:
    print("player1 == player2")

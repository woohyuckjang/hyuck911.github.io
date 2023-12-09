# 주사위 여러 개를 동시에 던지기
# 같은 숫자가 나올 때까지 주사위 6개를 동시에 무한 반복해서 던진다.같은 숫자가 나올 때 까지
# 몇번 던졌는지, 1부터 6까지 연속된 숫자는 몇 번 나왔는지 출력


import random


# 전역변수 선언
dice1, dice2, dice3, dice4, dice5, dice6 = [0]*6 # 주사위 리스트 선언
throwCount, serialCount = 0, 0 # 던진 횟수와 1~6연속으로 나온 횟수의 변수 초기화


if __name__ == "__main__" :
    print("-"*40)
    print("2021136114-주사위 여러개 동시에 던지기-장우혁")
    print("-"*40)
    while True :
        throwCount += 1 # 던진 횟수 1 증가

        # 주사위를 6번 던져서 나온 숫자를 각각 저장.(1~6까지 숫자 중 하나 반환)
        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
        dice3 = random.randrange(1, 7)
        dice4 = random.randrange(1, 7)
        dice5 = random.randrange(1, 7)
        dice6 = random.randrange(1, 7)

        if dice1 == dice2 == dice3 == dice4 == dice5 == dice6 : # dice의 값이 모두 같으면 값 출력 후
                                                                                          #반복문 빠져나감
            print("6개의 주사위가 모두 동일한 숫자가 나옴 => ", dice1, dice2, dice3, dice4,
                      dice5, dice6)
            break
        # 주사위 숫자가 1~6인지 확인 후 맞으면 serialCount를 1 증가시킴
        elif (dice1 == 1 or dice2 == 1 or dice3 == 1 or dice4 == 1 or dice5 == 1 or dice6 == 1) and \
             (dice1 == 2 or dice2 == 2 or dice3 == 2 or dice4 == 2 or dice5 == 2 or dice6 == 2) and \
             (dice1 == 3 or dice2 == 3 or dice3 == 3 or dice4 == 3 or dice5 == 3 or dice6 == 3) and \
             (dice1 == 4 or dice2 == 4 or dice3 == 4 or dice4 == 4 or dice5 == 4 or dice6 == 4) and \
              (dice1 == 5 or dice2 == 5 or dice3 == 5 or dice4 == 5 or dice5 == 5 or dice6 == 5) and \
              (dice1 == 6 or dice2 == 6 or dice3 == 6 or dice4 == 6 or dice5 == 6 or dice6 == 6) :
                serialCount += 1
    # 6개가 동일한 숫자가 나오면 반복문을 종료 후 throwCount와 serialCount 횟수 출력
    print("6개가 동일한 숫자가 나올 때까지 주사위를 던진 횟수 =>", throwCount)
    print("6개가 동일한 숫자가 나올 때까지, 1~6의 연속번호가 나온 횟수 =>", serialCount)
              

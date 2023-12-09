print("-"*40)
print("동전 교환 프로그램 : 2021136114-woohyuck")
print("-"*40)

## 변수 선언 부분 ##
money, c500, c100, c50, c10 = 0,0,0,0,0
# money=c500=c100=c50=c10=c1=0


## 메인 코드 부분 ##
# 1. 돈 입력받기
money = int(input("교환할 돈을 입력하세요 : "))

# 2. 동전 계산
# 500원 동전 계산
c500 = money//500
money = money%500

# 100원 동전 계산
c100 = money//100
money = money%100

# 50원 동전 계산
c50 = money//50
money = money%50

# 10원 동전 계산
c10 = money//10
money = money%10

# 잔돈 계산
c1 = money//1
money = money%1

## 출력하기
print("500원 개수 : {:d}개".format(c500))
print("100원 개수 : {:d}개".format(c100))
print("50원 개수 : {:d}개".format(c50))
print("10원 개수 : {:d}개".format(c10))
print("잔돈 개수 : {:d}개".format(c1))

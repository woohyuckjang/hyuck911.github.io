'''
# 문제 1
# 나이에 따른 입장료 구하기
# 입장료 정가 5000원
# 8세 미만 무료
# 8세이상 ~ 60세 미만 정가
# 60세이상 정가의 50%
money = 5000
age = int(input("나이 입력 : "))

if age < 8:
    print("무료입니다.")
if  8 <= age < 60:
    print("입장료 : ",money)
if age >= 60:
    print("입장료 : ",money*0.5)

# 문제 2 - if문 한번만 사용
# 나이에 따른 입장료 구하기
# 입장료 정가 5000원
# 8세 미만 무료
# 8세이상 ~ 60세 미만 정가
# 60세이상 무


if 8<=age<60:
    print("입장료 : ", money)
else:
    print("입장료 무료")
'''
money = 5000
age = int(input("나이 입력 : "))
if age>=8 and age<60:
    print("정가")
else:
    print("무료")

# 사용자로부터 이름, 키, 체중 값을 입력받아 비만도를 구하고 출력하는 코드를 작성하시오.
# 비만도 계산식 : 비만도(%) = 현재 체중 / 표준 체중 *100
# 표준 체중 계산 식 : 표준 체중 = (현재 키 - 100) * 0.9

print("-"*40)
print("비만도 구하기2021136114_woohyuck")
print("-"*40)

# 1. 데이터 입력받기
name = input("이름 입력 : ")
tall = float(input("키 입력 : "))
weight = float(input("체중 입력 : "))

# 2. 비만도와 체중 계산하기
std_weight = (tall-100) * 0.9
pat = (weight/std_weight) * 100

# 3. 출력하기
print("%s님의 비만도는 %.2f입니다."%(name, pat))
print("{}님의 비만도는 {:.2f}%입니다.".format(name, pat))

print("-"*30)
print("2021136114-장우혁")
print("-"*30)
# 1. 전화번호에서 하이픈 제거하기
phone_number = "010-1234-5678"

# 전화번호 처음부터 끝까지 '-' 아닌것 찍기
for i in phone_number:
    if i != "-":
        print(i,end="")
print()
# 2. 전화번호에 하이픈 삽입하기
number = "01012345678"
phone = "" # 하이픈 삽입한 번호
# 번호의 길이를 알수 없다. len()함수 이용
for i in range(0,len(number)):
    if i == 2:
        phone = phone + (number[2] + "-")
    elif i == 6:
        phone = phone + (number[6] + "-")
    else:
        phone = phone + number[i]
print(phone)

# 3. 입력받은 숫자가 3의 배수이면서 짝수인지 판별하기
a=int(input("숫자 입력 : "))
if a % 3 == 0:
    if a % 2 == 0:
        print("3의 배수이면서 짝수")

# 3-1. 3번에서 if문을 한번만 사용해서 작성하기
if a%3==0 and a%2==0:
     print("3의 배수이면서 짝수")
else:
    print("해당사항X")

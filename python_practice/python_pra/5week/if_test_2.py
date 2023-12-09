# 입력받아 계산하는 계산기 프로그램
# 1. 숫자와 수식을 같이 입력받아서
# 2. 수식에 따라 계산하기
# 3. 1번과 2번을 같이 작성. 선택하는 번호에 따라 실행
print("-"*48)
print("   계산기 프로그램 : 2021136114-장우혁")
print("-"*48)

select = int(input("방식 선택 : 1. 수식같이, 2. 따로입력"))
if select==1: #수식같이
    a=input("수식을 입력하세요.(예:2+5) : ")
    aa=eval(a)
    print(a,"=",aa)
    print("%d %c %d = %d" % (a,aa))
elif select==2: #따로입력
    num1=int(input("첫번째 숫자 : "))
    num2=int(input("두번째 숫자 : "))

    if op=="+":
        result = num1+num2
    elif op=="-":
        result = num1-num2
    elif op=="*":
        result = num1*num2
    elif op=="/":
        result = num1/num2
    else:
        print("수식 입력 오류")
    #print(num1,op,num2,"=",result)
    #print("%d %c %d = %d" % (num1,op,num2,result))
    print("{} {} {} = {}".format(num1,op,num2,result))
else:
    print("방식 선택 오류")


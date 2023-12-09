# 입력받아 계산하는 계산기 프로그램
# 1. 숫자와 수식을 같이 입력받아서
# 2. 수식에 따라 계산하기
print("-"*48)
print("   계산기 프로그램 : 2021136114-장우혁")
print("-"*48)
# 1. 숫자와 수식을 같이 입력받아서
# eval(수식) 함수 사용
'''
a=input("수식을 입력하세요.(예:2+5) : ")
aa=eval(a)
print(a,"=",aa)
print("%s = %d" % (a,aa))
print("{:s} = {:d}".format(a,aa))
'''

# 2. 수식에 따라 계산하기
# 1) 숫자 입력 받기 2개
num1=int(input("첫번째 숫자 : "))
num2=int(input("두번째 숫자 : "))
# 2) 수식 입력 받기
op=input("수식 입력 : (예: +,-,*,/ 중 한개) : ")
# 3) 수식에 따라 계산하기(if문 이용)
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
print(num1,op,num2,"=",result)
print("%d %c %d = %d" % (num1,op,num2,result))
print("{} {} {} = {}".format(num1,op,num2,result))



print("-"*40)
print("기본 계산기(입력받아) : 2021136114-woohyuck")
print("-"*40)
# input() 함수로 입력받기 : 문자로 인식
# int() 함수 이용해서 숫자로 변환


a=int(input("input a: "))
b=int(input("input b: "))
c=int(input("input c: "))
print("a=",a,",b=",b,",c=",c)

# 더하기
result=a+b+c
print(a,"+",b,"+",c,"=",result)
# 빼기
result=a-b-c
print(a,"-",b,"-",c,"=",result)
# 곱하기
result=a*b*c
print(a,"*",b,"*",c,"=",result)
# 나누기
result=a/b/c
print(a,"/",b,"/",c,"=",result)

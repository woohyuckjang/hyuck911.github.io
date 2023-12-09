# 변수 4개에 값을 입력받아 합계 구하기
# 1. 일반적인 프로그램
'''
a,b,c,d,hap=0,0,0,0,0
#a=b=c=d=0
a=int(input("in a:"))
b=int(input("in b:"))
c=int(input("in c:"))
d=int(input("in d:"))
hap=a+b+c+d
print("hap=",hap)

# 2. 리스트 이용 기본
aa = [0,0,0,0]
hap=0

aa[0]=int(input("in a:"))
aa[1]=int(input("in b:"))
aa[2]=int(input("in c:"))
aa[3]=int(input("in d:"))
hap=aa[0]+aa[1]+aa[2]+aa[3]
print("hap=",hap)
'''
# 3. for문 이용
aa=[0,0,0,0]
hap=0

for i in range(len(aa)):
    aa[i]=int(input(str(i+1)+"번째 숫자 : "))
    hap+=aa[i]
print(hap)





    

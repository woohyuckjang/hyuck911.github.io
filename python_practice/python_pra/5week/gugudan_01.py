print("-"*35)
print("구구단 찍기 : 2021136114-장우혁")
print("-"*35)
# 구구단 찍기
dan = 5 # 5단 찍기
print(" ",dan,"단")
print("="*10)
for s in range(1, 10):
    #print(dan,"*",s,"=",dan*s)
    #print("%2d * %2d = %2d % (dan,s,dan*s))
    print("{:2} * {:2} = {:2}".format(dan,s,dan*s))

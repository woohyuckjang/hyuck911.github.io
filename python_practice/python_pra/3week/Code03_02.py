print("-"*35)
print("서식문자(정렬)2021136114-woohyuck")
print("-"*35)

#서식 문자 (정렬)
# > 오른쪽 정렬, < 왼쪽 정렬, ^ 가운데 정렬
print("서식문자 정렬하기")
print("-"*25)
print("%10s, %-10s"%("오른쪽","왼쪽"))
print("{:>10}, {:<10}".format("오른쪽","왼쪽"))
print("{:^10}".format("가운데"))
print("-"*35)

print("서식문자 정렬하기(빈 여백 채우기)")
print("-"*35)
print("%5d, %05d"%(1,1))
print("{:5}, {:05}".format(1,1))
print("-"*35)

print("서식문자 천단위 구분")
print("-"*35)
print("{:,}".format(10000000000))
print("-"*35)



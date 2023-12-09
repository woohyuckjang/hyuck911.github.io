print("%d" % 123)
print("%5d" % 123)
print("%05d" % 123)

print("%f" % 123.45)
print("%7.1f" % 123.45)
print("%7.3f" % 123.45)

print("%s" % "Python")
print("%10s" % "Python")

print("{0:d} {1:5d} {2:05d}".format(123, 123, 123))
print("{:d} {:5d} {:05d}".format(123, 123, 123))
print("{2:d} {1:5d} {0:05d}".format(123, 456, 789))

a=10

a+=5; print("a+=5 => ", a)
a-=5; print("a-=5 => ", a)
a*=5; print("a*=5 => ", a)
a/=5; print("a/=5 => ", a)
a//=5; print("a//=5 => ", a)
a%=5; print("a%=5 => ", a)
a**=5; print("a**=5 => ", a)

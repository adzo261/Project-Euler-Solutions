a=2
b=8
sum=0
while a<4000000:
    sum += a
    a,b=b,4*b+a
print(sum)

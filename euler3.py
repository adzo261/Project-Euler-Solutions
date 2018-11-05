n=600851475143
i=2
ans=0
while i*i<=n:
    while n%i==0:
        n//=i
        ans=i
    i=i+(1 if i==2 else 2)
if n!=1:
    ans=n
print(ans)
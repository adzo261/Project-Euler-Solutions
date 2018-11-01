
def sum_of_multiples(n,r):
    return n*(r*(r+1))//2

print(sum_of_multiples(5,999//5)+sum_of_multiples(3,999//3)-sum_of_multiples(15,999//15))

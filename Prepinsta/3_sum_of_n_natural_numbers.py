'''n = 5
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)

n = 5
print(n*(n+1)/2)'''


def getsum(n):
    if n == 0:
        return n;
    return n+getsum(n-1);

n = 5
sum = getsum(n);
print(sum)


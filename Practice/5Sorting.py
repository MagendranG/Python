n=int(input("Enter total Number : " ))
a=[]
print("Enter the numbers : ")
for i in range(0,n):
  x=int(input())
  a.append(x)

for i in range(0,n):
  for j in range(i,n):
    temp = a[i]
    a[i]=a[j]
    a[j]=temp

print(a)
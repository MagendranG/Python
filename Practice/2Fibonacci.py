n = int(input("Enter a Num : " ))
n1,n2 = 0,1

for i in range (0,n):
    print(n1, end = " ")
    n3 = n1 + n2
    n1 = n2 
    n2 = n3
    

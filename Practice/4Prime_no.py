num = 5

if num > 1:

    for i in range(2,int(num/2)+1):
        if(num % i == 0):
            print("Not a prime")
            break
    else:
        print("Prime number")
else:
    print("Not a prime")
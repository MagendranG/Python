def Fib(n):
    if n < 0 :
        print("NIL")
    elif n == 0:
        return 0
    elif n ==1 or n ==2:
        return 1
    else :
        return Fib(n-1) +Fib(n-2)
    
n = int(input())
print(Fib(n))

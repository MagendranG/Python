num1,num2,num3 = 10,200,30
if(num1>num2 and num1>num3):
    print(num1)

elif(num2>num1 and num2>num3):
    print(num2)

else:
    print(num3)



num1,num2,num3 = 10,200,30
if num1 > num2:
    if num1>num3:
        print(num1)
elif(num2>num3):
    if(num2>num1):
        print(num2)
    else:
        print(num3)


num1,num2,num3 = 10,20,30
print(max(num1,num2,num3))
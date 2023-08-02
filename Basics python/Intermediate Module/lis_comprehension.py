'''
fruits=["apple","bananas","doctor","doggy"]
New=[]

for x in fruits:
    if "a" in x:
        New.append(x)

print(New)
'''
'''
fruits=["apple","bananas","doctor","doggy"]
New=[x for x in fruits if "a" in x ]
print(New)
'''
'''
#first 5 even numbers
fruits=["apple","bananas","doctor","doggy"]
New=[x for x in range(0,11,2)]
print(New)
'''
fruits=["apple","bananas","doctor","doggy"]
New=[x.upper() for x in fruits]
print(New)

fruits=["apple","bananas","doctor","doggy"]
New=[x if x!="doctor" else "oranges" for x in fruits]
print(New)



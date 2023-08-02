#ordered,unchangeable and allows duplicates
#tuple=("bus","car","bike",30,40,5.0)
#print(tuple)
t=("car","bike",30,20,3,1.2,3.4,"car")

#print(len(t))
#print(type(t))
#print(t)

#indexing
#print(t[0])
#print(t[:])

#Slicing
#print(t[1:3])
#print(t[-1])
#print(t[2:-1])



#how to change values in tuple
t=list(t)
print(type(t))

t.append("joker")
t.insert(2,"drink")

t=tuple(t)
print(t)
print(type(t))
'''
def add(x,y):
    print(x+y)
add(3,4)
'''
'''
list=['car','bike','plane','bus']
def loop(x):
    print(x*3)
loop(list)
'''
list=['car','bike','plane','bus']
def loop(x):
    print(x*3)

def looping(blah,list):
    for things in list:
        blah(things)

looping(loop,list)
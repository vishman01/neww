import time


# numlist = [] #todo to check for list
def numgen(num):
    for i in range(num):
        yield i



#t1 = time.clock()
l = numgen(10)
#t2 = time.clock()
for x in l:
    print(x)
print("The time taken is : ")

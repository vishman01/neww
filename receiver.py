import pickle
f = open("emp.dat",'rb')
print('Deserialising Employee Objects..\n------------------------------')
while True:
    try:
        obj = pickle.load(f)
        obj.display()
        print("-----------------------------\n")
    except EOFError:
        print("End Of File..!!")
        break
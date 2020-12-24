import pickle
from emp import *
f= open('emp.dat','wb')
while True:
    eno = int(input('Enter Employee Number : '))
    ename = input('Enter Employee Name : ')
    esal = float(input('Enter Employee Salary : '))
    eaddr = input('Enter Employee Address : ')
    e = Employee(eno,ename,esal,eaddr)
    pickle.dump(e,f)
    option = input("Do you wqnt to enter more?? [Yes|No]").lower()
    if option == 'no':
        break
print('All Employees Serialised..!!!')
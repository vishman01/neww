class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print("ENO : {} \nENAME : {} \nESAL : {} \nEADDR : {}".format(self.eno,self.ename,self.esal,self.eaddr))
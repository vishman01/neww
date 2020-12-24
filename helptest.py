import pymysql

con = pymysql.connect(user='root', password='mysql', host='localhost')
if con is not None:
    print("Connection Established..!!")

    #print("Version : ", con.version)
else:
    print("Connection Error..!!!")


con.close()

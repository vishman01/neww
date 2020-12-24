import os
fname = input("Enter file name : ")
if os.path.isfile(fname):
    print("File Exixts...!!",fname)
    f= open(fname,'r')
    print("The file content is :\n")
    print(f.read(),"\n")
    f.seek(0)   #dont forgot to put this line as the cursor will reach to last to file and then the output will show 0 lines, 0 words, 0 chars
    lcount = wcount = ccount =0
    for line in f:
        lcount =lcount+1
        words = line.split()
        wcount = wcount+len(words)
        ccount=ccount+len(line)
    print('No. of Lines : ',lcount," Lines")
    print("No. of Words : ",wcount," Words")
    print("No. of Characters : ",ccount,' Characters')
else:
    print("File Not Found..!!!", fname)

l1 = [['A',100,1000,'RNC'],['B',200,2000,'BLR'],['C',300,3000,'RPR']]
for item in l1:
    print(item[0],item[1],item[2],item[3],sep='\t')



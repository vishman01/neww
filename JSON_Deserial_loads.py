import json
import JSON_Serial_dumps as jsd
x = jsd.json_string
e = json.loads(x)
#if __name__ =='__main__':
def printing():
    print("NAME : ",e['name'])
    print("AGE : ",e['age'])
    print("SALARY : ",e['salary'])
    print("MARRIED OR NOT : ",e['isMarried'])
    print("CURRENT LAPTOP : ",e['currentLaptop'])
    print("---------------------------------")
    for k, v in e.items():
        print('{} : {}'.format(k, v))
printing()


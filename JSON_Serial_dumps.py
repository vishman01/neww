import json
Employee = {"name": "ABC",
            "age" : 35,
            "salary" : 1000.00,
            "isMarried" : True,
            "currentLaptop" : None
}
json_string = json.dumps(Employee , indent=4)
if __name__ == '__main__':
    print(json_string)
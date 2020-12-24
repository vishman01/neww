import json
import JSON_Deserial_loads as jdl
with open('Emp.json','r') as f:
    emp_dict = json.load(f)
jdl.printing()

import json
emp_dict={'eid': 101, 'ename': 'Rahul', 'avail': True, 'loc': 'undefined', 'esal': None}
print(emp_json)
emp_dict=json.loads(emp_json)
print(type(emp_dict))  #<class,dict>
print(emp_dict)
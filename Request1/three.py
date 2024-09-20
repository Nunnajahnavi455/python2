# import json
import csv
#python data is converting into json file
customers=[
    {'id':101,'name':'Rahul','avail':True},
    {'id':102,'name':'Sonia','avail':False},
    {'id':103,'name':'Priya','avail':False},
]
#  fp1=open('emp.json','w')
#  fp2=open('emp.csv','w')
# # json.dump(customers,fp1)
# # print('JSON file created module')
# fp1.close()

#python data to convert into csv file

fp1=open('emp.csv','w',newline="")
wr=csv.writer(fp1)
wr.writerow(['id','name','avail'])
for cust in customers:
    wr.writerow([cust['id'],cust['name'],cust['avail']])

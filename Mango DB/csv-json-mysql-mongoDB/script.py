import requests
import csv
import json 
import mysql.connector
import pymongo 

users = None 

users_data=requests.get('https://jsonplaceholder.typicode.com/users')
users=users_data.json()
print(users)
print(type(users))

fp1=open('user.json','w')
json.dump(users,fp1)
print("user Data - write into json file successfully")
fp1.close()


con=mysql.connector.connect(host='localhost',user='root',)
cursor=con.cursor()
sql_st='insert into user() values()'


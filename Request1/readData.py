import requests
import json
import csv
api.url='https://jsonplaceholder.typicode.com/users'
user_Data=None
try:
    user_Data=request.get(api-url)
except:
    fp=open('user.json','r')
    user_Data=fp.load(fp)
#analyse data[users]
# write into csv file
# print(type(user_Data))

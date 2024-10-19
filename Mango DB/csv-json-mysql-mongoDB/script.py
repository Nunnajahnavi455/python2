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

try:
    fp1=open('user.json','w')
    json.dump(users,fp1)
    print("written successfully")
except Exception as e:
       print(e)
finally:
      fp1.close()

    
    
sql_st='insert into user(uid,uname,email,city,website,phone)values(%5,%5,%5,%5,%5,%5)'

new_users=[]
for user in users:
      new_users.append((user['id'],user['email'],user['address']['city'],user['website'],user[]))
print(new_users)

dbcon=None

try:
      dbcon=mysql.connector.connect(host='localhost',user='root',password='root',database='dasara')
      cursor = con.cursor()
      cursor.executemany(sql_st,new_users)
      dbcon.commit()
      print("Data Inserted Successfully mysql table")

except mysql.connector.Error as e:
      print(e)
finally:
      cursor.close()
      dbcon.close()

try:
    client=pymongo.MongoClient('')
    db=client['api_data']
    users_col=db['users']
    users_col.insert_many(users)
    print("Inserted Successfully")

except Exception as e:
      print(e)
finally:
      client.close()

fp2=None

try:
      fp2=open('user.csv','w',newline='\n')
      csv.writer=csv.writer(fp2)
      csvwriter.writerow('UID','UName')
      for user in users:
            csvwriter.writerow([user['id'],user['name'],user['email']])


except Exception as err:
      print(err)
finally:
      fp2.close()





# fp1=open('user.json','w')
# json.dump(users,fp1)
# print("user Data - write into json file successfully")
# fp1.close()


# # con=mysql.connector.connect(host='localhost',user='root',)
# # cursor=con.cursor()
# # sql_st='insert into user() values()'


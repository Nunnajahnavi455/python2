import requests

data=requests.get('https://dummyjson.com/users')

# users_data=data.json()

# print(type(data))
# print(type(data.json()))
print(data.content)
import json 
import requests

# customer = """{
#     "name": "Usman",
#     "email": "usman@example.com",
#     "age": 24,
#     "city": "Faisalabad"
# }"""
# customer = """{
#     "name": "Usman",
#     "contact": {
#         "email": "usman@example.com",
#         "phone": "03001234567"
#     },
#     "address": {
#         "city": "Faisalabad",
#         "country": "Pakistan"
#     }
# }"""
# data=json.loads(customer)
# name=data["name"]
# email=data["contact"]["email"]
# phone=data["contact"]["phone"]
# city=data["address"]["city"]
# country=data["address"]["country"]

# print("Name: ",name)
# print("email:", email)
# print("Phone: ",phone)
# print("City: ",city)
# print("Country: ",country)




# url="https://jsonplaceholder.typicode.com/users/5"
# response=requests.get(url)
# if response.status_code==200:
#     data=response.json()
#     name=data["name"]
#     email=data["email"]
    
#     city=data["address"]["city"]
#     company=data["company"]["name"]

#     print("Name: ",name)
#     print("email:", email)
    
#     print("City: ",city)
#     print("Company: ",company)




customers =""" [
    {
        "name": "Usman",
        "email": "usman@example.com",
        "address": {
            "city": "Faisalabad"
        }
    },
    {
        "name": "Ali",
        "email": "ali@example.com",
        "address": {
            "city": "Lahore"
        }
    },
    {
        "name": "Hassan",
        "email": "hassan@example.com",
        "address": {
            "city": "Islamabad"
        }
    }
]"""


data=json.loads(customers)
for customer in data:
    name=customer["name"]
    email=customer["email"]
    city=customer["address"]["city"]

    print("Name:",name)
    print("Email: ",email)
    print("City: ",city)
    print("="*10)
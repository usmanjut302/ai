import requests

# # Service A
# url_a = "https://jsonplaceholder.typicode.com/users/1"

# response = requests.get(url_a)

# customer = response.json()

# name = customer["name"]
# email = customer["email"]

# # Process
# message = f"Hello {name}, welcome to our system!"

# # Service B
# url_b = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "email": email,
#     "message": message
# }

# response = requests.post(url_b, json=data)

# print("Status:", response.status_code)
# print("Response:", response.json())



# step 1 Get customer data
customer_url="https://jsonplaceholder.typicode.com/users/5"
response=requests.get(customer_url)
if response.status_code==200:
    customer=response.json()

# Step 2 process data
    name=customer["name"]
    email=customer["email"]
    city=customer["address"]["city"]
    print(name)
    print(email)
    print(city)

    message=f"hello {name} , your email is {email}"
    print(message)
    

# step 3 Send data to another service
    notification_url="https://jsonplaceholder.typicode.com/posts"
    user_data={
        "email":email,
        "name":name,
        "city":city
        
    }
    send_response=requests.post(
        notification_url,
        json=user_data
    )


# step 4 check result
    if send_response.status_code==201:
        print("Notification sent successfully")
    else:
        print("Failed to send notification")
else:
    print("Failed to get customer data")        
import requests
import json

# message="I want a refund because the product I received is damaged."
# ai_response="""{
#     "intent":"refund",
#     "priority":"high",
#     "action":"human_support"
# }"""
# data=json.loads(ai_response)
# intent=data["intent"]
# priority=data["priority"]
# action=data["action"]

# print(intent)
# print(priority)
# print(action)

# if action=="human_support":
#     print("Ticket sent to human support")
# elif action=="auto_reply":
#     print("Automatic reply sent")
# else:
#     print("unknown action")    
# 
# 
# url="https://jsonplaceholder.typicode.com/users/5"    
# response=requests.get(url)
# if response.status_code==200:
#     user=response.json()

#     name=user["name"]
#     email=user["email"]
    
#     message=f"hello {name} , this is your email {email} !"
#     print(message)

#     ai_response="""{
#         "intent": "delivery_issue",
#         "priority": "high",
#         "action": "human_support"
#     }"""

#     data=json.loads(ai_response)
#     intent=data["intent"]
#     priority=data["priority"]
#     action=data["action"]

#     if priority=="high":
#         print("Send huamn support")
#     elif priority=="medium":
#         print("auto reply")
#     else:
#         print("need more info ")        



message = "I ordered a phone 10 days ago and it has not arrived."

ai_response="""
{
    "intent": "delivery_issue",
    "priority": "high",
    "action": "human_support"
}
"""
user=json.loads(ai_response)
intent=user["intent"]
priority=user["priority"]
action=user["action"]
print(message)
print("Intent: ", intent)
print("Priority: ",priority)
print("Action: ",action)

if action=="human_support":
    print("Ticket sent to human support")
elif action=="auto_reply":
    print("automatic reply sent")
else:
    print("unknown action")    

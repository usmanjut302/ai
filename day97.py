import json

# message = "I forgot my password and cannot login to my account."

# ai_response = """
# {
#     "category": "login_problem"
# }
# """
# data=json.loads(ai_response)
# category=data["category"]
# print("Message: ",message)
# print("Category: ",category)


# message = "I ordered a phone 12 days ago but I still haven't received it."
# ai_response = """
# {
#     "category": "delivery_issue",
#     "priority": "high"
# }
# """
# data=json.loads(ai_response)
# category=data["category"]
# priority=data["priority"]
# print("Message:",message)
# print("Category:",category)
# print("Priority:",priority)



# message = """
# I bought a smartphone from your store two weeks ago.
# When I received it, I noticed that the screen was damaged.
# I contacted customer support yesterday and explained the problem.
# They told me to contact the store, but I have not received any
# solution yet. I would like to return the phone and get a refund.
# """

# ai_response = """
# {
#     "summary": "Customer received a damaged smartphone and wants to return it for a refund."
# }
# """

# data=json.loads(ai_response)
# summary=data["summary"]
# print("Original Message: ",message)
# print("Summary: ",summary)



# message = """
# I bought a smartphone from your store two weeks ago.
# When I received it, I noticed that the screen was damaged.
# I contacted customer support yesterday and explained the problem.
# They told me to contact the store, but I have not received any
# solution yet. I would like to return the phone and get a refund.
# """
# ai_response = """
# {
#     "category": "product_damage",
#     "priority": "high",
#     "summary": "Customer received a damaged laptop after a 15-day delay and has not received support."
# }
# """

# data=json.loads(ai_response)
# category=data["category"]
# priority=data["priority"]
# summary=data["summary"]

# print("Original Message: ",message)
# print("Category:",category)
# print("Priority: ",priority)
# print("Summary: ",summary)



message="""
    I ordered a phone 8 days ago and it finally arrived,
    but the screen is broken. I contacted support but haven't
    received a response. I want a replacement.
"""

ai_response = """
{
    "category": "product_damage",
    "priority": "high",
    "summary": "Customer received a damaged phone after an 8-day delay and wants a replacement.",
    "action": "replacement"
}
"""

data=json.loads(ai_response)
category=data["category"]
priority=data["priority"]
summary=data["summary"]
action=data["action"]

print("Original Message: ",message)
print("Category:",category)
print("Priority: ",priority)
print("Summary: ",summary)
print("Action: ",action)

if action=="replacement":
    print("Replacement process started")
elif action=="refund":
    print("Refund process started ") 
else:
    print("Action requires human review")       
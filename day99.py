import json


# recipient="abc@gmail.com"
# subject="Order not recieved"
# body="Please check your order status"
# print("Recipient: ",recipient)
# print("Subject: ",subject)
# print("Body: ",body)



# name = "Usman"
# order_id = "ORD-101"
# status = "Delayed"
# body=(f"Hello {name}, your order {order_id} is {status}.")
# print(body)



# name = "Usman"
# order_id = "ORD-101"
# status = "Delayed"
# priority = "high"
# recipient="abc@gmail.com"
# if priority=="high":
#     print("Urgent email required")
#     print("Recipient: ",recipient)
#     print("Subject: ",f"Order {order_id} is {status}")
#     body=(f"Hello {name}, your order {order_id} is {status}.")
#     print("Body: ",body)

# else:
#     print("No urgent email required")



# name = "Usman"
# email = "usman@example.com"
# order_id = "ORD-101"
# status = "Delayed"
# priority = "high"

# if priority=="high":
#     print("Urgent email required")
#     print("Recipient: ",email)
#     print("Subject: ",f"Order {order_id} is {status}")
#     body=(f"Hello {name}, your order {order_id} is {status}.")
#     print("Body: ",body)

# else:
#     print("No urgent email required")



message="I ordered a phone 8 days ago and it still hasn't arrived."
ai_response = """
{
    "category": "delivery_issue",
    "priority": "high",
    "summary": "Customer's phone delivery is delayed."
}
"""
data=json.loads(ai_response)
category=data["category"]
priority=data["priority"]
summary=data["summary"]
recipient="abc@gmail.com"
if priority=="high":
    print("Urgent email required")
    print("Recipient: ",recipient)
    subject=f"High priority: {category}"
    print("Subject: ",subject)
    body=(f"{summary}")
    print("Body: ",body)
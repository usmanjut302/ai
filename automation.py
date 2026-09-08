# messages=[
#     "my order is late",
#     "i want to return my order",
#     "my payement failed"
# ]
# for message in messages:
#     if "late" in message:
#         category="Delivery"
#     elif "return" in message:
#         category="Return"
#     elif "payment" in message:
#         category="Payment"
#     else:
#         category="General"
#     print(message)
#     print("category:", category)
#     print() 



tasks=[
    "send email",
    "backup database",
    "generate report",
    "send notification"
]         
print("="*15)
print("TASK AUTOMATION")
print("="*15)

print("Automation started...")

for task in tasks:
    print(f"processing: {task}")
    print("Status: Completed")

print("="*25)
print("Automation Completed")
print("="*25)       
        
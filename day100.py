import json

message = """
I ordered a phone 8 days ago and it still hasn't arrived.
I contacted support yesterday but nobody replied.
"""
ai_response = """
{
    "category": "delivery_issue",
    "priority": "high",
    "summary": "Customer's phone delivery is delayed and previous support contact received no response.",
    "action": "human_support"
}
"""
data=json.loads(ai_response)
category=data["category"]
priority=data["priority"]
summary=data["summary"]
action=data["action"]
email=""
report=""
if action=="human_support":
    report="="*30+"\n"
    report+="CUSTOMER SUPPORT REPORT\n"
    report+="="*30+"\n"
    report+=f"Message: {message}\n"
    report+=f"Category: {category}\n"
    report+=f"Priority: {priority}\n"
    report+=f"Summary: {summary}\n"
    report+=f"Action: {action}\n"
    
    email+="="*30+"\n"
    email+="Preparing email ......"+"\n"
    email+="="*30+"\n"
    email+=f"Recipient: abc@gmail.com \n"
    # print("Recipient: ",email)
    email+=f"Subject: {category}\n"
    # print("Subject: ",email)
    email+=(f"Body: {summary}\n")
    report+="\n"
    report+=email
    print(report)
    print(email)
else: 
    print("no urgent email required")


with open("reports/support_report.txt", "w") as file:
    file.write(report)
 
import requests
import json

message = """
I ordered a phone 8 days ago and it still hasn't arrived.
I contacted support yesterday but nobody replied.
"""

ai_response = """
{
    "category": "general ",
    "priority": "low",
    "summary": "Customer's phone delivery is delayed and previous support contact received no response.",
    "action": "auto_reply"
}
"""

data = json.loads(ai_response)

category = data["category"]
priority = data["priority"]
summary = data["summary"]
action = data["action"]
support_data = {
    "category": category,
    "priority": priority,
    "summary": summary,
    "action": action
}
support_url = "https://jsonplaceholder.typicode.com/posts"

response = requests.post(
    support_url,
    json=support_data
)

print(response.json())
if response.status_code==201:
    print("Support ticket created successfully")
    print("Status code:", response.status_code)
    ai_data=response.json()
    # category = ai_data["category"]
    # priority = ai_data["priority"]
    # summary = ai_data["summary"]
    # action = ai_data["action"]
    api_data=response.json()
    email=""
    report=""
    if action=="human_support":
        report="="*30+"\n"
        report+="CUSTOMER SUPPORT REPORT\n"
        report+="="*30+"\n"
        
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
        
    else: 
        print("no urgent email required")


    with open("reports/support_report.txt", "w") as file:
        file.write(report)
 

else:
    print("Failed to create support ticket")

    
# ai_response = {
#     "category": "delivery_issue",
#     "priority": "urgent",
#     "action": "human_support"
# }
ai_response = {
    "category": "product_damage",
    "priority": "high",
    "action": "delete_customer"
}

category = ai_response["category"]
priority = ai_response["priority"]
action = ai_response["action"]

print("Category:", category)
print("Priority:", priority)
print("Action:", action)


allowed_actions = [
    "replacement",
    "refund",
    "human_support",
    "auto_reply"
]
allowed_priorities = [
    "high",
    "medium",
    "low"
]

if action in allowed_actions:
    print("Action is allowed")
    if priority in allowed_priorities:
        print("Priority is allowed")
        if action == "human_support":
            if priority == "high":
                print("Urgent: Ticket sent to human support")
            elif priority == "medium":
                print("Create normal support ticket")    
            elif priority == "low":
                print("Add to support queue")
        elif action == "auto_reply":
            print("Send automatic response")
        elif action == "replacement":
            if priority == "high":
                print("Urgent: Start replacement process")
            elif priority == "medium":
                print("Start replacement process")
            elif priority == "low":    
                print("put replacement process in queue")
        elif action == "refund":
            if priority == "high":
                print("Urgent: Start refund process")
            elif priority == "medium":
                print("Start refund process")
            elif priority == "low":    
                print("put refund process in queue")
    else:
        print("invalid priority")  
        print("Human review required")     
else:
    print("Unknown Action")
    print("Human review required")
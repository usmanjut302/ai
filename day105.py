
ai_response = {
    "category": "product_damage",
    "priority": "high",
    "action": "replacement"
}
print("Step 1: AI response received")

allowed_actions = [
    "replacement",
    "refund",
    "human_support",
    "auto_reply"
]
allowed_priority=[
    "high",
    "medium",
    "low"
]
action= ai_response["action"]
print("Step 2: Validate action")
if ai_response["action"] in allowed_actions:
    print("Step 3: Validate priority")
    if ai_response["priority"] in allowed_priority:
        if action=="human_support":
            print("Step 4: Create human support Ticket")
            save_success=False
            if save_success:
                print("Step 5: Save support ticket")
                print("Step 6: Notify support team")
                print("Step 7: Workflow completed")
            else:
                print("Workflow stopped")    
        elif action == "replacement":
            print("Step 4: Start replacement process")
            save_success=False
            if save_success:
                print("Step 5: Save replacement request")
                print("Step 6: Notify customer")
                print("Step 7: Workflow completed")
            else:
                print("Stop workflow")
        elif action == "refund":
            print("Step 4: Start refund process")
            save_success=False
            if save_success:
                print("Step 5: Save refund request")
                print("Step 6: Notify customer")
                print("Step 7: Workflow completed")
            else:
                print("Stop workflow")
        elif action == "auto_reply":
            print("Step 4: Generate automatic response")     
            print("Step 5: send response")
            print("Step 6: Workflow completed")   

        
       
    else:
        print("Step 3: Priority is not allowed")
        print("Workflow stopped")    
else:
    print("Step 3: Action is not allowed")
    print("Workflow stopped")
    raise Exception("Invalid action")
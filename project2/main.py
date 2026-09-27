from ai_engine import analyze_customer_message
from database import save_customer_request,update_request_status
import logging


logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_human_support(request_id):
    print(f"Human support request created for customer request {request_id}")
    logging.warning(
        f"Request {request_id}: transferred to human support"
    )
def execute_action(action, request_id):
    max_attempts = 3
    action_success = False
    for attempt in range(1, max_attempts + 1):
        try:
            logging.info(f"Request {request_id}: attempt {attempt}")
            # if attempt < 3:
                # raise Exception("Temporary action failure")
                
            logging.info(f"Request {request_id}: action started: {action}")

            if action == "replacement":
                print("Replacement process started")
                # raise Exception("Replacement service unavailable")

            elif action == "refund":
                print("Refund process started")

            elif action == "human_support":
                print("Human support request created")

            elif action == "auto_reply":
                print("Automatic reply generated")

            action_success = True
            break    

        except Exception as e:
            print("Action failed")
            logging.error(
                f"Request {request_id}: attempt {attempt} failed: {e}"
                )
            if attempt == max_attempts:
                try:
                    update_request_status(request_id, "human_support")
                except Exception as db_error:
                    logging.error(
                        f"Request {request_id}: failed to update status: {db_error}"
                    )

            # return

    if not action_success:
        print("All attempts failed")
        return False 
    logging.info(f"Request {request_id}: action succeeded")

    try:
        update_request_status(request_id, "completed")
        # raise Exception("Database update failed")
        logging.info(f"Request {request_id} completed successfully")
        return True

    except Exception as db_error:
        print("Action succeeded, but status update failed")
        logging.error(
            f"Request {request_id}: status update failed: {db_error}"
        )
            


customer_message = input("Enter customer message: ")
logging.info("Customer request received")
ai_result = analyze_customer_message(customer_message)
# ai_result = {
#     "category": "product_damage",
#     "priority": "high",
#     "action": "replacement"
    
# }
# ai_result = ["product_damage", "high", "replacement"]

if ai_result is None:
    print("AI analysis failed. Workflow stopped.")
    logging.error("AI analysis failed. Workflow stopped.")
    exit()
if not isinstance(ai_result, dict):
    print("Invalid AI response structure")
    logging.error("AI response is not a dictionary")
    exit()
required_fields = [
    "category",
    "priority",
    "action"
]

for field in required_fields:
    if field not in ai_result:
        print(f"Missing AI field: {field}")
        logging.error(f"Missing AI field: {field}")
        exit()
if set(ai_result.keys()) != set(required_fields):
    print("Unexpected AI fields")
    logging.error("AI returned unexpected fields")
    exit()
logging.info(f"AI result: {ai_result}")

if not isinstance(ai_result["category"], str):
    print("Invalid category type")
    logging.error("Invalid AI category type")
    exit()

if not isinstance(ai_result["priority"], str):
    print("Invalid priority type")
    logging.error("Invalid AI priority type")
    exit()

if not isinstance(ai_result["action"], str):
    print("Invalid action type")
    logging.error("Invalid AI action type")
    exit()
if not ai_result["category"].strip():
    print("Category is empty")
    logging.error("AI returned empty category")
    exit()

if not ai_result["priority"].strip():
    print("Priority is empty")
    logging.error("AI returned empty priority")
    exit()

if not ai_result["action"].strip():
    print("Action is empty")
    logging.error("AI returned empty action")
    exit()    
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
allowed_categories = [
    "product_issue",
    "product_damage",
    "delivery_issue",
    "account_issue"
]

category = ai_result["category"].strip().lower()
priority = ai_result["priority"].strip().lower()
action = ai_result["action"].strip().lower()
if action in allowed_actions:
    print("Action is valid")
    if priority in allowed_priorities:
        print("Priority is valid")
        if category in allowed_categories:
            print("Category is valid")
            request_id= save_customer_request(
                customer_message,
                category,
                priority,
                action
                )  

            logging.info(f"Request {request_id} saved to database")  
            action_result = execute_action(action, request_id)
            if action_result is False:
                create_human_support(request_id)
        else:
            print("Invalid category")
            logging.warning(f"invalid ai category: {category}")
    else:
        print("Invalid priority")
        logging.warning(f"Invalid AI priority: {priority}")   
else:
    print("Invalid action")
    logging.warning(f"Invalid AI action: {action}")
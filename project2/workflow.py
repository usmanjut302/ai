import logging

from ai_engine import analyze_customer_message
from validator import validate_ai_result
from database import save_customer_request
from actions import (
    execute_action,
    create_human_support,
    SUCCESS,
    ACTION_FAILED,
    STATUS_UPDATE_FAILED,
    INVALID_AI_RESULT,
    DATABASE_SAVE_FAILED
)

def process_customer_request(customer_message):
    
    logging.info("Customer request received")
    try:
        
        ai_result = analyze_customer_message(customer_message)

        if not validate_ai_result(ai_result):
            print("Invalid AI result. Workflow stopped.")
            logging.error("AI result validation failed")
            
            return INVALID_AI_RESULT
    except Exception as e:
        print("Error occur during analyzing customer message")
        logging.error(f"Error occur during analyzing customer message: {e}")
        return "AI_ANALYSIS_FAILED"
    
    category = ai_result["category"]
    priority = ai_result["priority"]
    action = ai_result["action"]

    print("AI result is valid")
    print("Category:", category)
    print("Priority:", priority)
    print("Action:", action)


    request_id = save_customer_request(
        customer_message,
        category,
        priority,
        action
    )
    if request_id is None:
            print("Customer request was not saved. Workflow stopped.")
            logging.error("Customer request saving failed. Workflow stopped.")
            return "DATABASE_SAVE_FAILED" 

    logging.info(f"Request {request_id} saved to database")

    action_result = execute_action(action, request_id)
       


    if action_result == ACTION_FAILED:
        create_human_support(request_id)
        return ACTION_FAILED

    if action_result == STATUS_UPDATE_FAILED:
        print("Action succeeded, but database status update failed.")
        return STATUS_UPDATE_FAILED

    return SUCCESS
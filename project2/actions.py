import logging
from database import update_request_status
SUCCESS = "SUCCESS"
ACTION_FAILED = "ACTION_FAILED"
STATUS_UPDATE_FAILED = "STATUS_UPDATE_FAILED"
DATABASE_SAVE_FAILED = "DATABASE_SAVE_FAILED"
INVALID_AI_RESULT = "INVALID_AI_RESULT"

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
        return ACTION_FAILED
    logging.info(f"Request {request_id}: action succeeded")

    try:
        update_request_status(request_id, "completed")
        logging.info(f"Request {request_id} completed successfully")
        # raise Exception("Database update failed")
        return SUCCESS

    except Exception as db_error:
        print("Action succeeded, but status update failed")
        logging.error(
            f"Request {request_id}: status update failed: {db_error}"
        )
        return STATUS_UPDATE_FAILED
    
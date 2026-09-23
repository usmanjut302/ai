# import logging
# logging.basicConfig(level=logging.INFO)

# logging.debug("Debug message")
# logging.info("Normal workflow running")
# logging.warning("Something unusual happened")
# logging.error("Something failed")
# logging.critical("Critical system failure")



# import logging

# logging.basicConfig(level=logging.INFO)

# logging.info("Step 1: Workflow started")
# logging.info("Step 2: AI response received")
# logging.info("Step 3: AI decision validated")
# logging.info("Step 4: Action executed")
# logging.info("Step 5: Workflow completed")


# import logging

# logging.basicConfig(
#     filename="automation.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     )

# logging.info("Workflow started")
# logging.info("AI response received")
# logging.warning("Something unusual happened")
# logging.error("Something failed")
# logging.info("Workflow completed")


# import logging

# logging.basicConfig(level=logging.DEBUG)

# logging.debug("Debug message")
# logging.info("Normal workflow running")
# logging.warning("Something unusual happened")
# logging.error("Something failed")
# logging.critical("Critical system failure")



# import logging
# import time

# logging.basicConfig(
#     filename="automation.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

# logging.info("Workflow started")
# for attempt in range(1,4):
#     logging.info(f"Attempt {attempt} started")
#     try:
#         # result = 10 / 0
#         # logging.info("Calculation completed")
#         # break

    
#         if attempt <3:
            
#             raise Exception("Temporary failure")
#         else:
#             result = 100
        
#         logging.info(f"Operation successful: {result}")
#         break   
#     except Exception as e:
#             logging.error(f"Attempt {attempt} failed: {e}")
#             if attempt<3:
#                 logging.info("Retrying...")
#                 time.sleep(2)
#             else:
#                 logging.error("All attempts failed")     

# logging.info("Workflow finished")







import logging 
import time

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Workflow started")
ai_response = {
    "intent": "refund",
    "priority": "high",
    "action": "human_support"
}

allowed_actions = [
    "replacement",
    "refund",
    "human_support",
    "auto_reply"
]
action=ai_response["action"]
if action in allowed_actions:
    logging.info(f"Action validated: {action}")
    for attempt in range(1,4):
        logging.info(f"Attempt {attempt} started")
        try:  
            if attempt <3:
                        
                raise Exception("Temporary failure")    
            if action == "human_support":
            
                logging.info("Ticket sent to human support")
            elif action == "auto_reply":
                logging.info("Automatic reply sent")
            elif action == "replacement":
                logging.info("Start replacement process")
            elif action == "refund":
                logging.info("Start refund process")
              

            logging.info(f"Operation successful: {action}")    

            break    
        except Exception as e:
            logging.error(f"Attempt {attempt} failed: {e}")
            if attempt<3:
                logging.info("Retrying....") 
                time.sleep(2)
            else:
                logging.error("All attempts failed")
                logging.warning("Human review required")       
else:
    logging.error(f"Invalid action: {action}")        

logging.info("Workflow completed")  
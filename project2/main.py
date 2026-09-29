import logging
from workflow import process_customer_request

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


        
customer_message = input("Enter customer message: ")

# process_customer_request(customer_message)
result = process_customer_request(customer_message)
print("Workflow result:", result)
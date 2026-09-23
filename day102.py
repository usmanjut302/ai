import time

# def task():
#     print("Generation daily report ...")
#     print("Report generated successfully")
# while True:
#     task()
#     time.sleep(5)    
    
# def backup_database():
#     print("Starting database backup...")
#     print("Database backup completed")

# while True:
#     backup_database()
#     time.sleep(10)    



# print("Current hour: ",hour)
# print("Current minutes: ",minute)
# print("Current seconds: ",second)


# def task():
#     print("Generation daily report ...")
#     print("Report generated successfully")
# task_completed=False
# while True:  
#     current_time=datetime.now()
#     print("Current time: ",current_time)
#     hour=current_time.hour
#     minute=current_time.minute
#     second=current_time.second  
    
#     if hour==10 and minute==24 and task_completed==False:
#         print("Scheduled task is running")
#         task()
#         task_completed=True
#     time.sleep(10)
    
from datetime import datetime
import time
import threading
# def generate_report():
#     print("Report generation started") 
#     time.sleep(5)
#     print("Report generated successfully")
# print("Response Sent to user")
# thread=threading.Thread(target=generate_report)   
# thread.start()
# print("Generating report request received")   



message = "My order is damaged"
# def analyze_message():
#     print("Analyzing message...")
#     time.sleep(5)
#     print("Message analyzed successfully")
# thread=threading.Thread(target=analyze_message)
# thread.start()
# print("Customer Request received")
# thread.join()
# print("Response Sent to user: Your request is being processed")  
# 
# 
import time
import threading
from datetime import datetime


def generate_report():
    print("Report generation started")

    time.sleep(5)

    print("Report generated successfully")  


task_completed=False
while True:
    current_time = datetime.now()

    print("Current time: ", current_time)

    hour = current_time.hour

    minute = current_time.minute

    second = current_time.second
    if hour==11 and minute==20 and task_completed==False:
        print("Scheduled task is running")
        thread=threading.Thread(target=generate_report)
        thread.start()
        task_completed=True
        print("Scheduled report task started")
        
    time.sleep(10)
            
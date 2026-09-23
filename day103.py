# tasks = [
#     {"id": 1, "name": "Generate report", "status": "pending"},
#     {"id": 2, "name": "Send email", "status": "completed"},
#     {"id": 3, "name": "Backup database", "status": "pending"}
# ]

# for task in tasks:
#     if task["status"] == "pending":
#         print("Running task:",task["name"])
#         task["status"] = "completed"
#         print(tasks)



# tasks = [
#     {"id": 1, "name": "Send email", "status": "pending"},
#     {"id": 2, "name": "Backup database", "status": "completed"},
#     {"id": 3, "name": "Generate report", "status": "pending"},
#     {"id": 4, "name": "Send notification", "status": "pending"}
# ]

# for task in tasks:
#     if task["status"]=="pending":
#         print("Running task:",task["name"])
#         task["status"]="completed"
# print(tasks)

import mysql.connector
try:
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="automation_db"
    )
    print("Database connected successfully")


    cursor=db.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks=cursor.fetchall()

    print(tasks)
    for task in tasks:
        if task[2]=="pending":
            print("Running task:",task[1])
        
            cursor.execute("UPDATE tasks SET status=%s WHERE id= %s",
                   ("completed",task[0])
                   )
    db.commit()
    print("Automation completed successfully")
except Exception as e:
    print("Error:",e)
    db.rollback()



# import mysql.connector

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="automation_db"
# )

# cursor = db.cursor()

# try:
#     cursor.execute(
#         "UPDATE tasks SET status=%s WHERE id=%s",
#         ("pending", 1)
#     )

#     print("Change made")

#     raise Exception("Something went wrong")

#     db.commit()

# except Exception as e:
#     db.rollback()
#     print("Error:", e)
#     print("Changes rolled back")
import mysql.connector
from config import DB_PASSWORD

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=DB_PASSWORD,
    database="automation_project2"
)

print("Database connected successfully")
def save_customer_request(message, category, priority, action):

    cursor = connection.cursor()

    query = """
    INSERT INTO customer_requests
    (message, category, priority, action, status)
    VALUES (%s, %s, %s, %s, %s)
    """

    data = (
        message,
        category,
        priority,
        action,
        "pending"
    )

    cursor.execute(query, data)
    connection.commit()
    request_id=cursor.lastrowid

    print("Customer request saved successfully")
    print("Request ID:", request_id)

    return request_id

def update_request_status(request_id, status):

    cursor = connection.cursor()

    query = """
    UPDATE customer_requests
    SET status = %s
    WHERE id = %s
    """

    data = (status, request_id)

    cursor.execute(query, data)
    connection.commit()

    print("Request status updated")

# update_request_status(8, "completed")
 
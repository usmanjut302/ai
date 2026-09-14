import os

# with open("reports/tasks.txt","w") as file:
    # file.write()


# with open("reports/tasks.txt","a") as file:
#     file.write("send email\n")
#     file.write("backup database\n")
#     file.write("generate report\n")
#     file.write("send notification\n")
    

# with open("reports/tasks.txt","r") as file:
#     lines=file.readlines()
#     for line in lines:
#         print("Processing :",line.strip())


# with open("reports/employees.txt","w") as file:
#     file.write("Usman,2122225\n")
#     file.write("Ali,300000\n")
#     file.write("josan,450000\n")
#     file.write("Hassan,70000\n")

with open("reports/employees.txt","r") as file:
    lines=file.readlines()
    results=[]
    for line in lines:
        name,salary=line.strip().split(",")
        salary=int(salary)
        if salary>=60000:
            level="high"
        elif salary>=50000:
            level="medium"
        else:
            level="low"
        result=(f"{name}-{salary}-{level}")
        results.append(result)

    with open("reports/employee_report.txt","w") as file:
        for result in results:
            file.write(f"{result}\n")        
        
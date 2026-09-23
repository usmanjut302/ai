# employees = [
#     {"name": "Usman", "salary": 65000},
#     {"name": "Ali", "salary": 45000},
#     {"name": "Hassan", "salary": 70000}
# ]
employees = [
    {"name": "Usman", "salary": 65000},
    {"name": "Ali", "salary": 48000},
    {"name": "Hassan", "salary": 75000},
    {"name": "Jutt", "salary": 55000},
    {"name": "Ahmed", "salary": 90000}
]
report = ""

high_count=0
medium_count=0
low_count=0
report+="="*30 +"\n"
report+="EMPLOYEE REPORT" + "\n"
report+="="*30 + "\n"
for employee in employees:

    name = employee["name"]
    salary = employee["salary"]

    if salary >= 60000:
        level = "High"
        high_count+=1
    elif salary >= 50000:
        level = "Medium"
        medium_count+=1
    else:
        level = "Low"
        low_count+=1
    
    report += f"{name} - {salary} - {level}\n"
report +="="*30+"\n"    
report += (
        f"STATISTICS\n"
        f"Total Employees: {len(employees)}\n"
        f"High: {high_count}\n"
        f"Medium: {medium_count}\n"
        f"Low: {low_count}\n"
    )

print(report)


# print("-"*30)
# print("STATISTICS")
# print("-"*30)
# print(f"Total Employees: {len(employees)}")
# print(f"High: {high_count}")
# print(f"Medium: {medium_count}")
# print(f"Low: {low_count}")

with open("employee_report.txt", "w") as file:
    file.write(report)
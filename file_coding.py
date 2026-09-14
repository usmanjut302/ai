import os

with open("reports/students.txt","r") as file:
    lines=file.readlines()

results=[]

for line in lines:
    name,score=line.strip().split(",")
    score=int(score)
    if score>=80:
        level="Excellent"
    elif score>=60:
        level="Good"
    else:
        level="Need Improvement"

    result=f"{name}-{score}-{level}"
    # print(results)
    results.append(result)

with open("reports/results.txt","w") as file:
    for result in results:
        file.write(f"{result}\n")
print("processing is completed")        
import os

# os.mkdir("reports")

# check the folder exists or not 
# if os.path.exists("reports"):
#     print("Folder already exists")
# else:
#     os.mkdir("reports")
#     print("Folder created")

# Create folder automatically
# if not os.path.exists("reports"):
#     os.mkdir("reports")
#     print("Folder created")
# else:
#     print("Folder already exists")


# List files in a folder 
# files= os.listdir("reports")
# print(files)


# Data Processing
# with open("reports/students.txt","r") as file:
#     lines=file.readlines()

# for line in lines:
#     name,score=line.strip().split(",")
#     score=int(score)
#     print(name,score)


# processing the score

with open("reports/students.txt","r") as f:
    lines=f.readlines()

for line in lines:
    name,score=line.strip().split(",")
    score=int(score)
    if score>=80:
        level="Excellent"
    elif score>=60:
        level="Good"
    else:
        level="Need Improvement"

    print(name,score,level)        
import csv
import datetime

userFile = "user_Master.csv"

userFilter = ""

outputFolder = "Generated Filters"

count = 0

def gen_Elif_Filter(email, code):
    temp_Filter = f"ELIF USERNAME() = {email} THEN {code} = [insertRowField]\n"
    return temp_Filter

def gen_if_Filter(email, code):
    temp_Filter = f"IF USERNAME() = {email} THEN {code} = [insertRowField]\n"
    return temp_Filter



with open(userFile, "r") as master:
    file = csv.reader(master, delimiter=",")
    for row in file:
        if count == 0:
            count = count + 1
        elif count == 1:
            count = count + 1
            userFilter = userFilter + str(gen_if_Filter(row[0], row[1]))
        else:
            userFilter = userFilter + str(gen_Elif_Filter(row[0], row[1]))

    master.close()
userFilter = userFilter + "END"


output = open(f"{outputFolder}/Filter {str(datetime.date.today())} {str(datetime.datetime.now().hour)}{str(datetime.datetime.now().minute)}{str(datetime.datetime.now().second)}.txt", "w")
output.write(userFilter)
output.close()

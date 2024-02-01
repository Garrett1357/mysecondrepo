## employee_report.py -  Use employee_data.csv. Management would like to know 
## which of their employees are highly efficient and which are not. Efficiency
## can be calculated by dividing the productivity by hours worked. An employee
## is considered highly efficient if the efficiency factor is greater than 2. 
## An employee is considered inefficient if the efficiency factor is below 1. 
## Management would also like to know who and how many are in different age categories - 
## 20s, 30s and 40s. Reproduce the report as show below (print statements).

import csv
employee = open('employee_data.csv','r')
csv_file = csv.reader(employee)
next(csv_file) #skips header and starts on the next line
for rec in csv_file:    #This brings each record into a list format 
    prod = int(rec [6])
    hrs = int(rec [5])
    efficiency = (prod / hrs)
    if efficiency >= 2:
        eff_rate = "Highly Efficient"
    elif efficiency <= 1:
        eff_rate = "Inefficient"
    print(f"Name:   {rec[1]}")
    input()
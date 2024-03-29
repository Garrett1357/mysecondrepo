## employee_report.py -  Use employee_data.csv. Management would like to know 
## which of their employees are highly efficient and which are not. Efficiency
## can be calculated by dividing the productivity by hours worked. An employee
## is considered highly efficient if the efficiency factor is greater than 2. 
## An employee is considered inefficient if the efficiency factor is below 1. 
## Management would also like to know who and how many are in different age categories - 
## 20s, 30s and 40s. Reproduce the report as show below (print statements).

import csv

ages = {'20s': [], '30s': [], '40s': []} #Establishes list for age
categories = {'Highly Efficient': [], 'Inefficient': []} # Establishes list for efficiency categories

employee = open('employee_data.csv','r')
csv_file = csv.reader(employee)
next(csv_file) #skips header and starts on the next line

for rec in csv_file:    #This brings each record into a list format 
    name = rec[1]
    age = int(rec[2])
    prod = int(rec[5])
    hrs = int(rec[4])
    efficiency = (prod / hrs)

#efficiency calculations     
    if efficiency >= 2:
        categories['Highly Efficient'].append(name)
    elif efficiency <= 1:
        categories['Inefficient'].append(name)

#age calculation
    if 20 <= age < 30:
            ages['20s'].append(name)
    elif 30 <= age < 40:
            ages['30s'].append(name)
    elif 40 <= age < 50:
            ages['40s'].append(name)

    #print(f"Name:   {rec[0]}")
    #input()
print("Efficiency Categories:")
for category, names in categories.items():
    print(f"\nEmployees who are {category}:")
    for name in names:
        print(f"{name}")



print("\nAge Groups:")
for group, names in ages.items():
    print(f"\nEmployees in their {group}:")
    for name in names:
        print(f"{name}")
    print(f"Total number of employees in their {group}: {len(names)}")

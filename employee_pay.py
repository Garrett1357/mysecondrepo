import csv
employee = open('employee_data.csv','r')
#infile = open('customer_country.csv')
csv_file = csv.reader(employee)
#to skip the header and start on the next lone
next(csv_file)
for rec in csv_file:    #This brings each record into a list format
    #print (rec) 
    salary = float(rec [3])
    bonus = float(rec [7])
    total_bonus= (salary * bonus)
    total = salary + total_bonus
    print("Name: ", {rec [2]})
    print("Salary: ", {rec [4]})
    print("Bonus: ", {total_bonus})
    print("Total Salary: ", {total})#NAME SALARY BONUS PAY
    input()
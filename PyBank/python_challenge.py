import os
import csv

budgetdataCSV = os.path.join("budget_data.csv")
with open(budgetdataCSV, 'r') as csvfile:
    # Split the data on commaas
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    print(header)
#budget_data_csv = os.path.join('C:/Users/colep/OneDrive/Desktop/python_challenge/PyBank/Resources/budget_data_csv')

# Open and read csv
# #with open(budget_data_csv, "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter = ",")

#     # Read the header row first (skip this part if there is no header)
#     csv_header = next(csv_file)
#     print(f"Header: {csv_header}")
    total_amount = 0 
    row_count = 0
    change_list  =[]
    prev = 0
    max_list = ["",999999]
    min_list = ["", 0]
    for row in reader:
        row_count = row_count + 1
        total_amount = int(row[1]) + total_amount
        difference  = int(row[1])- prev
        change_list.append(difference)
        prev = int(row[1])
        if difference > max_list[1]:
            max_list[0]=row [0]
            max_list[1] = difference
        if difference < min_list[1]:
            min_list[0]=row [0]
            min_list[1] = difference
    print(row_count)
    print(total_amount)
    # print(change_list)
    average = sum(change_list[1:]) / (len(change_list)-1)
    print(average)
    print(max_list[0], max_list[1])
    print(min_list[0], min_list[1])



        
        
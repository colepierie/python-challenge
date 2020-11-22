# import os
# import csv

# electiondata_csv = os.path.join("..", "Resources", "election_data.csv")
# with open(electiondata_csv) as csv_file:
#     # Split the data on commaas
#     cvs_reader = csv_reader(csv_file, delimiter =',')
#     header = next(reader)
#     print(header)

import os
import csv

election_data_csv = os.path.join("..", "Resources", "election_data.csv")
with open("election_data.csv") as csvfile:
    # Split the data on commaas
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    print(header)
# row_count = 0
# for row in cvs_reader:
#     row_count = row_count + 1

# print(row_count)
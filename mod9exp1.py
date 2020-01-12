import csv

first_row = True
csv_reader = csv.reader(open('people.csv'))

# loop over each row from the CSV reader
for row in csv_reader:
  if first_row:
    first_row = False
  else:
    # print just field 0 (name)
    print(row[0])


import csv

# create a new file called `output.csv` for writing to
output_file = open('output.csv', 'w')

# create a new CSV writer which writes to our new file
csv_writer = csv.writer(output_file)

# write some rows to the CSV file
csv_writer.writerow(['Hello', 1234])
csv_writer.writerow(['Goodbye', 5678])
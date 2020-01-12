import csv

csv_reader = csv.reader(open('climate_data_Dec2017.csv'))
output_file = open('output.csv', 'w')
csv_writer = csv.writer(output_file)

first_line = True
for line in csv_reader:
  if first_line:
    csv_writer.writerow(line)
    first_line = False
  else:
    state = line[1]
    if state == 'NSW':
      csv_writer.writerow(line)
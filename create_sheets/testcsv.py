import csv

with open('test.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

   
#    with open('newtest.csv','w') as newfile:
#        csv_writer = csv.writer(newfile, delimiter= '\t')
   
#        for line in csv_reader:
#            csv_writer.writerow(line)
#            print(line[2])
   
#   next(csv_reader)
    for line in csv_reader:
        print(line[0])
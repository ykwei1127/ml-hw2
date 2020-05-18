import shutil
import csv

# train data split
root = '/home/ykwei/Downloads/C1-P1_Train Dev_fixed/'
fn = '/home/ykwei/Downloads/C1-P1_Train Dev_fixed/train.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    data = list(csvReader)
    data = data[1:]
for row in data:
    src = root + 'C1-P1_Train/' + row[0]
    dest = root + 'train/' + row[1] + '/' + row[0]
    shutil.copy(src, dest)

# dev test data split
fn2 = '/home/ykwei/Downloads/C1-P1_Train Dev_fixed/dev.csv'
with open(fn2) as csvFile2:
    csvReader = csv.reader(csvFile2)
    data = list(csvReader)
    data = data[1:]
for row in data:
    src = root + 'C1-P1_Dev/' + row[0]
    dest = root + 'test/' + row[1] + '/' + row[0]
    shutil.copy(src, dest)
    
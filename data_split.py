import shutil
import csv
root = r'd:/機器學習/HW2/C1-P1_Train/'
fn = r'd:/機器學習/HW2/test.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    data = list(csvReader)
    data = data[1:]
for row in data:
    src = root + row[0]
    dest = root + row[1] + '\\' + row[0]
    shutil.copy(src, dest)
    
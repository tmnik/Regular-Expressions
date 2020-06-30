#extract all the numbers in the file and compute the sum of the numbers
import re
name = input("Enter file:")
if len(name) < 1 : name = "ex.txt"
han = open(name)

numbs = list()
for line in han:
    line = line.rstrip()
    part = re.findall('[0-9]+',line)
    if len(part)==[] : continue
    for i in range(len(part)):
        numb = int(part[i])
        numbs.append(numb)
all_numb = sum(numbs)
count = len(numbs)
print('Sum:',all_numb)
print('Count:',count)

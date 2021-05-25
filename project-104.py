import csv
from collections import Counter

with open('height-weight.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_data = [] 
for i in range(len(file_data)):
    in_num = file_data[i][2]
    new_data.append(float(in_num))
n = len(new_data)
total = 0
for x in new_data:
    total += x
mean = total/n
print("mean",mean)
new_data.sort()
if n%2==0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2-1])
    median = (median1+median2)/2
else:
    meadian = new_data[n//2]
print("median",median)
data = Counter(new_data)
range1 = {"50-60":0,"60-70":0,"70-80":0}
for height,occurance in data.items():
    if 50<float(height)<60:
        range1["50-60"]+=occurance
    elif 60<float(height)<70:
        range1["60-70"]+=occurance
    elif 70<float(height)<80:
        range1["70-80"]+=occurance
mode_range, mode_occurence = 0, 0
for range, occurence in range1.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode",mode)
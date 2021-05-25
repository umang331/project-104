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
range1 = {"75-85":0,"85-95":0,"95-105":0,"105-115":0,"115-125":0,"125-135":0,"135-145":0,"145-155":0,"155-165":0,"165-175":0,}
for height,occurance in data.items():
    if 75<float(height)<85:
        range1["75-85"]+=occurance
    elif 85<float(height)<95:
        range1["85-95"]+=occurance
    elif 95<float(height)<105:
        range1["95-105"]+=occurance
    elif 105<float(height)<115:
        range1["105-115"]+=occurance
    elif 115<float(height)<125:
        range1["115-125"]+=occurance
    elif 125<float(height)<135:
        range1["125-135"]+=occurance
    elif 135<float(height)<145:
        range1["135-145"]+=occurance
    elif 145<float(height)<155:
        range1["145-155"]+=occurance
    elif 155<float(height)<165:
        range1["155-165"]+=occurance
    elif 165<float(height)<175:
        range1["165-175"]+=occurance
mode_range, mode_occurence = 0, 0
for range, occurence in range1.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode",mode)

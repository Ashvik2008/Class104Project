import csv
from collections import Counter

file=open("SOCR-HeightWeight.csv")
read_file=csv.reader(file)

new_list=list(read_file)
new_list.pop(0)

content=[]

for i in range(len(new_list)):
    weight_data=new_list[i][2]
    content.append(float(weight_data))

total=0

for j in content:
    total=total+j

mean=total/len(content)

#printing mean
#Mean in this case will be 127.07942116079916
print(mean)

content.sort()

if len(content) % 2 == 0:
    median1 = float(content[len(content)//2])
    median2 = float(content[len(content)//2 -1])
    median=(median1+median2)/2
else:
    result = content[len(content)//2]

#printing median
#Median in this case will be 127.15775
print(median)

#mode
#in this case mode is 130.0
sorted_data = []
total_weight = 0

for person_data in new_list:
    total_weight += float(person_data[2])
    sorted_data.append(float(person_data[2]))

sorted_data.sort()

def get_mode(sorted_data):
    #Calculating Mode
    data = Counter(sorted_data)
    mode_data_for_range = {
                            "75-85": 0,
                            "85-95": 0,
                            "95-105": 0,
                            "105-115": 0,
                            "115-125": 0,
                            "125-135": 0,
                            "135-145": 0,
                            "145-155": 0,
                            "155-165": 0,
                            "165-175": 0
                        }
    for weight, occurence in data.items():
        if 75 < weight < 85:
            mode_data_for_range["75-85"] += occurence
        elif 85 < weight < 95:
            mode_data_for_range["85-95"] += occurence
        elif 95 < weight < 105:
            mode_data_for_range["95-105"] += occurence
        elif 105 < weight < 115:
            mode_data_for_range["105-115"] += occurence
        elif 115 < weight < 125:
            mode_data_for_range["115-125"] += occurence
        elif 125 < weight < 135:
            mode_data_for_range["125-135"] += occurence
        elif 135 < weight < 145:
            mode_data_for_range["135-145"] += occurence
        elif 145 < weight < 155:
            mode_data_for_range["145-155"] += occurence
        elif 155 < weight < 165:
            mode_data_for_range["155-165"] += occurence
        elif 165 < weight < 175:
            mode_data_for_range["165-175"] += occurence
    mode_range, mode_occurence = 0, 0
    for range, occurence in mode_data_for_range.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode = float((mode_range[0] + mode_range[1]) / 2)
    print(mode)

get_mode(sorted_data)
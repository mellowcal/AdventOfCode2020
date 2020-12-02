import pandas as pd

data = pd.read_csv('data.csv',header=None)
data_list = []
for i in data[0]:
    data_list.append(i)

input_data = data_list
input_data.sort(reverse=True)

def twenty_twenty_sum(data):
    new_list = []
    for i in range(len(data)):
        leftover = 2020 - data[i]
        new_list.append(leftover)

    for i in range(len(data)):
        for z in range(len(data)):
            if data[i] + data[z] in new_list:
                return data[i],data[z],2020-data[i]-data[z]
            else:
                continue


def multiply_output(list):
    num = len(list)
    output = 1
    for i in range(num):
        output = output * list[i]
    return output

numbers = twenty_twenty_sum(input_data)
print(numbers)
answer = multiply_output(numbers)
print(answer)




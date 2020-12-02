import pandas as pd

data = pd.read_csv('data.csv',header=None)
data_list = []
for i in data[0]:
    data_list.append(i)

input_data = data_list #[1721,979,366,299,675,1456]

def twenty_twenty_sum(data):
    for i in range(len(data)):
        n = len(data)
        while n > i:
            if data[i]+data[n-1] == 2020:
                return [data[i],data[n-1]]
            else:
                n=n-1

def multiply_output(list):
    return list[0]*list[1]

print(multiply_output(twenty_twenty_sum(input_data)))




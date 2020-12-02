
with open('./data.txt') as f:
    data = f.read().splitlines()

def extract_parameters(line):
    '''
    :param line: takes a string of the information on each line, usually i.
    :return: [[low_num,high_num],letter,password]
    '''

    sep = line.split()
    letter = sep[1].split(':')
    sep.pop(1)
    sep.insert(1, letter[0])
    range = sep[0].split('-')
    sep.pop(0)
    sep.insert(0, range)
    return sep


def policy_test(params):
    split_pass = list(params[2])
    letter = params[1]
    lower_num = int(params[0][0])
    higher_num = int(params[0][1])

    if letter == split_pass[lower_num-1] and letter != split_pass[higher_num-1]:
        return True
    elif letter != split_pass[lower_num-1] and letter == split_pass[higher_num-1]:
        return True
    else:
        return False


true_count = 0

for i in data:
    params = extract_parameters(i)
    if policy_test(params) == True:
        true_count += 1
    else:
        continue

print(true_count)





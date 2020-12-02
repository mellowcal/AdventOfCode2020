
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
    lower_num = params[0][0]
    higher_num = params[0][1]
    letter_count = 0

    for i in split_pass:
        if i == letter:
            letter_count += 1
        else:
            continue

    if letter_count >= int(lower_num) and letter_count <= int(higher_num):
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





import pandas as pd

with open('D3_data.txt') as f:
    lines = f.readlines()
    cleaned = []
    table_form = []
    for line in lines:
        cleaned.append(line.strip())
    for elem in cleaned:
        table_form.append(list(elem))
    f.close()

df = pd.DataFrame(table_form)

slope = [3,1] # [x,y]

def trees_hit(slope,df):
    tree_count = 0
    x, y = 0, 0
    up_y = df.shape[0]  # this is the rows

    while y <= up_y:
        x = x + slope[0]
        x = x % 31
        y = y + slope[1]

        try:
            if df[x][y] == '#':
                tree_count += 1

        except KeyError:
            break
    return tree_count


print(trees_hit(slope,df))



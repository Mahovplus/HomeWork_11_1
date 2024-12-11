import numpy as np

def creation_array_number(up,  to,  step, line):
    list = []
    while len(list) <= line:
        gene = [np.arange(up, to, step)]
        list.append(gene)
    return np.concatenate((list), axis=0)

array_num = creation_array_number(2, 11, 1, 5)
print(array_num)
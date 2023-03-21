with open('dataset.txt') as journal:
    lst = []
    lst_result = []

    for line in journal:
        data = line.strip().split(';')
        lst.append(data)

    average_value = 0
    for el in lst:
        average_value = ((float(el[1]) + float(el[2]) + float(el[3])) / 3)
        lst_result.append(round(average_value, 9))

    mat, fiz, rus = 0, 0, 0
    for el in lst:
        mat += float(el[1])
        fiz += float(el[2])
        rus += float(el[3])
    mat /= len(lst)
    fiz /= len(lst)
    rus /= len(lst)

with open('dataout.txt', 'w') as out:
    for i in lst_result:
        out.write(f'{str(i)}\n')
    out.write(f'{str(round(mat, 9))} {str(round(fiz, 9))} {str(round(rus, 9))}')

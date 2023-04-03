with open('text.txt') as inf:
    list1 = []
    list2 = []
    result_line = []
    for line in inf:
        line = line.strip()

        for i in range(len(line)):

            if '0' <= line[i] <= '9':
                if line[i - 1] not in '0123456789':
                    list2.append(line[i])
                else:
                    n = list2[-1]
                    list2[-1] = n + line[i]

            else:
                list1.append(line[i])

    for i in range(len(list1)):
        result_line.append(list1[i] * int(list2[i]))


with open('text1.txt', 'w') as out:
    out.write(str(''.join(result_line)))

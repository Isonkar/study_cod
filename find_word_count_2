result_set = {}

with open('text.txt') as inf:
    lst = inf.read().lower().strip().split()

    for i in range(len(lst)):
        cnt = lst.count(lst[i])
        result_set[lst[i]] = cnt

    max_v = max(result_set.values())

    final_dict = {k: v for k, v in result_set.items() if v == max_v}

    a = min(final_dict.keys())
    b = final_dict[a]

with open('text1.txt', 'w') as out:
    out.write(f'{a} {b}')

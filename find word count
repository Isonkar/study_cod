string = 'UYYZp UYYZp Xd YYbdT ZTZY YcYTa UTYUT'

lst = [str(i) for i in string.lower().split()] 
result_set = {} 

for i in range(len(lst)):
    cnt = lst.count(lst[i])
    result_set[lst[i]] = cnt
    
max_v = max(result_set.values())

final_dict = {k: v for k, v in result_set.items() if v == max_v}      
a = sorted(final_dict)

print(a[0], final_dict[a[0]])

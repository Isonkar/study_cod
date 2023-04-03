lst = input().lower().split() #['a', 'aa', 'abc', 'aa', 'ac', 'abc', 'bcd', 'a'] 
    
result_dict = {}
cnt = 0

for i in range(len(lst)):
    cnt = lst.count(lst[i])
    result_dict[lst[i]] = cnt    
    
for key,value in result_dict.items():
    print(key, value)

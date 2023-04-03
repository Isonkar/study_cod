one = input()
s = input()
two = ''.join(set(str(item) for item in one))
n = 0
for i in range(len(two)):
    x = two[i]
    for j in range(len(s)):
      if x == s[j]:
          n += 1
print(n)

journal = {str(key): [] for key in range(1,12)}
journal_set = []
with open('dataset.txt') as data:
  for line in data:
    journal_set.append(line.strip().split())

for i in range(len(journal_set)):
  if journal_set[i][0] in journal:
    journal[journal_set[i][0]].append(int(journal_set[i][2]))
  
with open('dataout.txt', "w") as out:
  
  for key,value in journal.items():
      try:
         out.write(f'{key} {float(sum(value)/ len(value))}\n')
      except ZeroDivisionError:
          out.write(f'{key} - \n')

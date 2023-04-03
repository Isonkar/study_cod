import requests

with open('dataset.txt') as data:
  url = data.readline().strip()
txt = requests.get(url)
while True:
  if not txt.text.startswith('We'):
    txt = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + txt.text)
  else:
    print(txt.text)
    break

with open('dataout.txt', 'w') as out:
  out.write(txt.text)

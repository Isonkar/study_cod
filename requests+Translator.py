import requests
from googletrans import Translator, constants 
from pprint import pprint

with open('dataset.txt') as data:
    url = data.readline().strip()
r = requests.get(url)
print(len(r.text.splitlines()))

translator = Translator()
translation = translator.translate(r.text, dest='ru')
print(f"{translation.text}")

with open('dataout.txt', 'w') as out:
    out.write(r.text)

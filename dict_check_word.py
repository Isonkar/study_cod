d = int(input('Введите количество слов, используемых в словаре: '))
dictionary, for_check = [], []
result = set()

for i in range(d):
    word = str(input('Введите слово для записи в словарь: ').lower())
    dictionary.append(word)
l = int(input('Количество строк для проверки: '))

for i in range(l):
    word1 = input('Введите строку для проверки в словаре: ').split()
    for i in range(len(word1)):  
        if word1[i].lower() not in dictionary:
            result.add(word1[i].lower())

for el in result:
    print(el)

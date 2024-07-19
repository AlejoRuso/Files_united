import os

os.remove("Final.txt")

files = {}
#Получаем список текстовых файлов и вносим название в ключ словаря
for x in os.listdir():
    if x.endswith(".txt"):
        files.setdefault(x)
#считаем кол-во строк в каждом файле и вносим его в значение словаря
        with open(rf'{x}', 'r', encoding = 'utf-8') as f:
            for count, line in enumerate(f):
                pass
            files[x] = count + 1

#сортируем словарь по кол-ву строк в файлах (значениям)
sorted_files = {}
for key in sorted(files, key=files.get):
    sorted_files[key] = files[key]
 
print(sorted_files)



for file, quantity in sorted_files.items():
    with open(rf'{file}', 'r', encoding='utf-8') as f:
        text = f.read()

        with open('Final.txt', 'a', encoding='utf-8') as ff:
            ff.write(f'{file} \n')
            ff.write(f'{quantity} \n')
            ff.write(f'{text} \n')
    #print(file)
    #print(quantity)
    #print(text)
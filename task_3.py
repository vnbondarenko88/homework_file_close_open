import os

directory = os.getcwd()
file_name = os.listdir(directory)
files_list = []
dict_1 = {}
dict_2 = {}
new_txt = open('4.txt', 'a', encoding='UTF-8')
for files in file_name:
    if files.endswith('.txt'):
        files_list.append(files)
for file in files_list:
    with open(file, encoding='UTF-8') as f:
        data = f.read().split('\n')
        count = 0
    for line in data:
        count += 1
        if file in dict_2:
            dict_2[file].append(line)
        else:
            dict_2[file] = [line]
    dict_1[file] = count
answer = sorted(dict_1.items(), key=lambda item: item[1], reverse=False)
for new_text in answer:
    name_file = new_text[0]
    count_line = new_text[1]
    new_txt.write(name_file + "\n" + str(count_line) + "\n" + str(dict_2[new_text[0]]) + "\n")
new_txt.close()
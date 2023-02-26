import datetime
import json




#BD=[12345,true,"яблоко",{"Миша": [898981646,464654654] }]
#идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки.
#pythnotic_name = load('pythnotic.json')
pythnotic_name = 'pythnotic.json'

notes = {
    "first record":
        {"body": "this is example for the note",
        "date": "21.2.21 17:05"},
    "second record":
        {"body": "2. this is example for the note",
        "date": "23.2.21 11:45"}
}
 
def save(pythnotic_name, save_mode):
    with open(pythnotic_name, mode=save_mode, encoding='utf-8') as file:
        file.write(json.dumps(notes, ensure_ascii=False))


def load(l_file):
    with open(l_file, mode='r', encoding='utf-8') as file:
        lst = json.load(file)
    return lst



# for n in note:
#     print (n)



# print(notes.get('first record',0))
# print(notes.get('second record',0))

# print(notes.get('second record',0).get('body'))
# print(notes.get('second record',0).get('date'))



# print('----------------')
# print(datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S"))


    
# print(note['second record'])
# print(note.get('second record',0))

notes = load(pythnotic_name)

def show(notes):
    sorted_notes = sorted(notes.items(), key=lambda x: x[1].get('date'),reverse = True)
    for k,v in sorted_notes:
        print('---------------------------------------------------------------------------')
        print('title: ',k)
        print('body: ', v.get('body'))
        print('date: ', v.get('date'))

def add(title, body):
    notes[title] = {"body": body,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")}
    print('\n---> note with title: "',title,'" is added\n')
    
def delete(title):
    if notes.get(title) != None: notes.pop(title)
    print('\n---> note with title: "',title,'" is deleted\n')
    print(sorted(notes.items(), key=lambda x: x[1].get('date')))
    
def edit(title,msg):
    print(title,msg,"deleted")
    
show(notes)
delete('second record')
add('4-th record', "это пример добавления треtьей строки")
show(notes)

 
# Opening JSON file

# with open('data.json') as json_file:
#     data = json.load(json_file)
 
#     # for reading nested data [0] represents
#     # the index value of the list
#     print(data['people1'][0])
     
#     # for printing the klue pair of
#     # for printing the key-value pair of
#     # nested dictionary for loop can be used
#     print("\nPrinting nested dictionary as a key-value pair\n")
#     for i in data['people1']:
#         print("Name:", i['name'])
#         print("Website:", i['website'])
#         print("From:", i['from'])
#         print()

#сохранением, чтением, добавлением, редактированием и удалением заметок
#python notes.py add --title "новая заметка" –msg "тело новой заметки"


# dict.clear() - очищает словарь.

# dict.copy() - возвращает копию словаря.

# classmethod dict.fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value (по умолчанию None).

# dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).

# dict.items() - возвращает пары (ключ, значение).

# dict.keys() - возвращает ключи в словаре.

# dict.pop(key[, default]) - удаляет ключ и возвращает значение.
# Если ключа нет, возвращает default (по умолчанию бросает исключение).

# dict.popitem() - удаляет и возвращает пару (ключ, значение). 
# Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.

# dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ со значением default (по умолчанию None).

# dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).

# dict.values() - возвращает значения в словаре.
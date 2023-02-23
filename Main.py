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
        file.write(json.dumps(note, ensure_ascii=False))


def load(l_file):
    with open(l_file, mode='r', encoding='utf-8') as file:
        lst = json.load(file)
    return lst


note = load(pythnotic_name)

for n in note:
    print (n)


    
print(note['second record'])

def show(pythnotic_name):
    print(note)

def add(title, msg):
    print(title,msg,"added")
    
def delete(title,msg):
    print(title,msg,"deleted")
    
def edit(title,msg):
    print(title,msg,"deleted")
    

 
# Opening JSON file

# with open('data.json') as json_file:
#     data = json.load(json_file)
 
#     # for reading nested data [0] represents
#     # the index value of the list
#     print(data['people1'][0])
     
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

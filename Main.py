import datetime
import json


# notes = {
# 1: 
#     {"title": "first record",
#     "body": "3.this is example fo the note",
#     "date": "2023-02-24 20.01.08"
#     },
# 2:
#     {"title":"second record",
#     "body": "2. this is example for the note",
#     "date": "2023-02-25 20.01.08"
#     }
# }
 
def save(pythnotic_name):
    with open(pythnotic_name,'w',encoding='utf-8') as file:
        file.write(json.dumps(notes, ensure_ascii=False))


def load(l_file):
    with open(l_file, mode='r', encoding='utf-8') as file:
        lst = json.load(file)
    return lst

#notes = load(pythnotic_name)

def show():
    sorted_notes = sorted(notes.items(), key=lambda x: x[1].get('date'),reverse = True)
    for k,v in sorted_notes:
        print('---------------------------------------------------------------------------')
        print('ID: ',k)
        print('title: ', v.get('title'))
        print('body: ', v.get('body'))
        print('date: ', v.get('date'))
        print('---------------------------------------------------------------------------')

def autoincrement_id():
    sorted_notes = sorted(notes.items(), key=lambda x: int(x[0]),reverse = True)
    for k,v in sorted_notes:
        id = int(k)+1
        break
    return id

def add():
    id = autoincrement_id()
    title = input("\n введите заголовок редактируемой записи ...:")
    body = input("\n введите текст редактируемой записи ...:")
    notes[id] = {"title": title, "body": body,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")}
    show()
    
def delete(id):
    if notes.get(id) != None: 
        n = notes.pop(id)
        print('\n---> note with title: "',n.get('title'),'" is deleted\n')
    else:
        print('note with id=',id,'not found')
    print(sorted(notes.items(), key=lambda x: x[1].get('date')))
    
def edit():
    id = input("\n введите id редактируемой записи ...:")
    print(notes[id].get('title'))
    title = input("\n введите заголовок редактируемой записи ...:")
    if "".__eq__(title):
        title = notes.get(id).get('title')
    print(notes.get(id).get('body'))
    body = input("\n введите текст редактируемой записи ...:")
    if "".__eq__(body):
        body = notes[id].get('body')
    notes[id] = {"title": title, "body": body,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")}
    show()

def dialog_help():
    print("\nчтение - 1\nредактирование - 2\nдобавление - 3\nудаление заметок - 4\nсохранение - 5\nвыход без сохранения - 6")
    
pythnotic_name = 'pythnotic.json'
notes = load(pythnotic_name) 
action = '1'   
while action != '6':
    if action == '1':
        show()
    if action == '2':
        edit()
    if action == '3':
        add()
    if action == '4':
        delete(input("\n введите id удаляемой строки ...:"))
    if action == '5':
        save(pythnotic_name)        
    if action == '6':
        save(pythnotic_name)
    dialog_help()  
    action = input("\n Сделайте Ваш выбор ...:")
      





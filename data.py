import sqlite3

def create(name, age):
    conn = sqlite3.connect("data.sqlite")
    cur = conn.cursor()
    cur.execute('''
        insert into Student(name, age)
        values(?,?)
    ''',(name, age))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("data.sqlite")
    cur = conn.cursor()
    cur.execute('''
        delete from Student where id = (?)
    ''',(id,))
    conn.commit()
    conn.close()


def update(id, name, age):
    conn = sqlite3.connect("data.sqlite")
    cur = conn.cursor()
    cur.execute('''
        update student
        set name = (?), age = (?)
        where id = (?)
    ''',(name, age,id))
    conn.commit()
    conn.close()


def read():
    conn = sqlite3.connect("data.sqlite")
    cur = conn.cursor()
    data = cur.execute('''
        select id, name, age from student
    ''')
    list = []
    for s in data:
        list.append({
            'id': s[0],
            'name': s[1],
            'age': s[2]
        })
    conn.close()
    return list


def student(id):
    conn = sqlite3.connect("data.sqlite")
    cur = conn.cursor()
    data = cur.execute('''
        select id, name, age from student
        where id = (?)
    ''',(id,))
    conn.commit()
    for s in data:
        student = {"id":s[0], "name":s[1], "age":s[2]}
    conn.close()
    return student

print(read())
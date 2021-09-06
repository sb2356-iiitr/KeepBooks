import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("create table if not exists book(id integer primary key, title text, author text, year integer, isbn varchar(20))")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("insert into book values(NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("select * from book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    query = "select * from book where"
    if title:
        if len(query) > 24:
            query += ' and lower(title) like lower("%{}%")'.format(title)
        else:
            query += ' lower(title) like("%{}%")'.format(title)
    if author:
        if len(query) > 24:
            query += ' and lower(author) like lower("%{}%")'.format(author)
        else:
            query += ' lower(author) like("%{}%")'.format(author)
    if year:
        if len(query) > 24:
            query += ' and year={}'.format(year)
        else:
            query += ' year={}'.format(year)
    if isbn:
        if len(query) > 24:
            query += ' and lower(isbn) like lower("%{}%")'.format(isbn)
        else:
            query += ' lower(isbn) like("%{}%")'.format(isbn)
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("delete from book where id=?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("update book set title=?, author=?, year=?, isbn=? where id=?",(title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()

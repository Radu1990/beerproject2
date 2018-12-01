import sqlite3
from sqlite3 import Error

# SQLITE DB operations


def create_connection(db_file='beervendor.sqlite'):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def table_init(conn):

    cur = conn.cursor()

    # creation of table
    cur.execute('DROP TABLE IF EXISTS beer_range')

    cur.execute('CREATE TABLE beer_range (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, header TEXT, flavour TEXT)')

    # insertion of first beers
    cur.execute('INSERT INTO beer_range (name, header, flavour) VALUES (?, ?, ?)',
                ('PUNK IPA', 'POST MODERN CLASSIC', 'SPIKY. TROPICAL. HOPPY.'))

    cur.execute('INSERT INTO beer_range (name, header, flavour) VALUES (?, ?, ?)',
                ('DEAD PONY CLUB', 'WEST COAST KICKS', 'CITRUSY. ZESTY. BRIGHT.'))

    cur.execute('INSERT INTO beer_range (name, header, flavour) VALUES (?, ?, ?)',
                ('5AM SAINT', 'OATMEAL MILK STOUT', 'DEEP. DARK. ABYSS.'))

    cur.execute('INSERT INTO beer_range (name, header, flavour) VALUES (?, ?, ?)',
                ('INDIE', '21ST CENTURY CRAFT', 'TRUE INDEPENDENT CRAFT.'))

    conn.commit()


def select_return_all_ids(conn):
    """
    Query all ids in the beer_range table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT id FROM beer_range")

    rows = cur.fetchall()

    ids_lst = []
    for row in rows:
        idnumber = row[0]
        ids_lst.append(idnumber)
    conn.close()
    return ids_lst


def select_return_all(conn):
    """
    Query all ids in the beer_range table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM beer_range")

    data = cur.fetchall()

    conn.close()
    return data


def insert_new_beer(conn, data):
    """conn is connection
    name, header, flavour are strings
    """
    cur = conn.cursor()

    name = data['name']
    header = data['header']
    flavour = data['flavour']

    cur.execute('INSERT INTO beer_range (name, header, flavour) VALUES (?, ?, ?)',
                (name, header, flavour))
    conn.commit()
    conn.close()


def select_item(conn, id):
    cur = conn.cursor()
    cur.execute('SELECT id, name, header, flavour FROM beer_range WHERE id=%s' % id)
    row = cur.fetchone()
    data = {"id": row[0],
            "name": row[1],
            "header": row[2],
            "flavour": row[3]}
    conn.close()
    return data


def delete_item(conn, id):
    cur = conn.cursor()
    cur.execute('DELETE FROM beer_range WHERE id=%s' % id)
    conn.commit()
    conn.close()


def update_item(conn, id, data):
    """
    update item, name, header and flavour
    :param conn:
    :param name: string
    :param header: string
    :param flavour: string
    :param id: string
    """
    sql = ''' UPDATE beer_range
              SET name = ? ,
                  header = ? ,
                  flavour = ?
              WHERE id = ?'''

    name = data['name']
    header = data['header']
    flavour = data['flavour']

    cur = conn.cursor()
    cur.execute(sql, (name, header, flavour, id))
    conn.commit()
    conn.close()


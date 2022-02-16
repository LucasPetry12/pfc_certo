from .connection import connect
from ..utils import hash_str
from mysql.connector import Error


def get_a_teacher(email):

    con = connect()
    cursor = con.cursor()
    sql__check = str(
        'select * from teachers where email = "{}"').format(email)
    cursor.execute(sql__check)
    records = cursor.fetchall()

    return records


def create_new_teacher(name, password_hash, email):
    con = connect()
    cursor = con.cursor()

    sql_insert = 'INSERT INTO teachers (name, password, email) VALUES (%s, %s, %s)'
    values = (name, password_hash, email)
    try:
        verify = get_a_teacher(email)
        if len(verify) > 0:
            return 'Usuário ja existe'
        else:
            cursor.execute(sql_insert, values)
            con.commit()
            cursor.close()
            con.close()
            return get_a_teacher(email)
    except Error as error:
        return 'Error' + error


def get_all_teachers():
    con = connect()
    cursor = con.cursor()
    try:
        cursor.execute('select * from teachers')
        records = cursor.fetchall()
        cursor.close()
        con.close()

        return records
    except Error as error:
        return 'Error' + error


def edit_a_teacher(_id, body):
    try:
        con = connect()
        cursor = con.cursor()
        sql_edit = 'UPDATE teachers SET email = %s, name = %s, password = %s where id = %s '
        cursor.execute(
            sql_edit, (body['email'], body['name'], hash_str.hash_str(body['password']), int(_id)))
        con.commit()

        cursor.execute("SELECT * FROM teachers where id = %s ", [_id])
        updated = cursor.fetchall()
        cursor.close()
        con.close()
        return updated
    except Error as error:
        return error


def delet_a_teacer(_id):
    try:
        query = 'DELETE FROM teachers WHERE id= %s'
        con = connect()
        cursor = con.cursor()
        cursor.execute(query, [int(_id)])
        con.commit()
        return {"Message": "Usuário deletado"}
    except:
        return {
            "error": 'error'
        }

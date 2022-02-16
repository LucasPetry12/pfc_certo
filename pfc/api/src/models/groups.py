from .connection import connect
import re
from mysql.connector import Error
from .activity import get_a_activity_from_code


def set_group(data):
    con = connect()
    cursor = con.cursor()
    activitye_id = get_a_activity_from_code(data['code'])

    query = "INSERT INTO groups(name, code, activitye_id ) values(%s,%s,%s)"
    values = data['name'], data['code'], activitye_id[0][0]
    cursor.execute(query, values)
    con.commit()
    _id = cursor.lastrowid

    cursor.execute(
        'select * from groups where id = %s', [_id])
    records = cursor.fetchall()
    return records


def define_group(group, _id):

    con = connect()
    cursor = con.cursor()
    query = 'UPDATE groups SET _group = %s where id = %s'
    values = [group, _id]
    cursor.execute(query, values)
    con.commit()

    cursor.execute(
        'select * from groups where id = %s', [_id])
    records = cursor.fetchall()

    return records


def get_group(_id):
    con = connect()
    cursor = con.cursor()
    cursor.execute(
        'select * from groups where id = %s', [_id])
    records = cursor.fetchall()
    return records


def get_all():
    con = connect()
    cursor = con.cursor()
    cursor.execute(
        'select * from groups where _group = 0')
    records = cursor.fetchall()
    return records


def get_all__code(code):
    con = connect()
    cursor = con.cursor()
    cursor.execute(
        'select * from groups where code = %s', [code])
    records = cursor.fetchall()

    return records

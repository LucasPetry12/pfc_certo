from .connection import connect
from mysql.connector import Error


def get_question(_id):
    print(_id)
    con = connect()
    cursor = con.cursor()

    cursor.execute('select * from questions where id = "{}"'.format(_id))
    records = cursor.fetchall()
    return records


def create_a_question(data, _id):
    con = connect()
    cursor = con.cursor()

    sql = 'INSERT INTO questions (question, answer_1, answer_2, answer_3, correct, author_name, author_id ,activitye_key) VALUES ("%s","%s","%s","%s","%s", "%s", "%s","%s")'
    cursor.execute(sql, (data['question'], data['answer_1'],
                   data['answer_2'], data['answer_3'], data['correct'], data['author_name'], data['author_id'], _id[0]))
    con.commit()
    created = get_question(cursor.lastrowid)
    cursor.close()
    con.close()

    return created


def edit_question(data):

    body = data['body']
    con = connect()
    cursor = con.cursor()

    sql_edit = "UPDATE questions SET question= %s, answer_1 = %s,answer_2 = %s, answer_3= %s, correct=%s where id = %s"

    cursor.execute(
        sql_edit, [body['question'], body['answer_1'], body['answer_2'], body['answer_3'], body['correct'], int(body['id'])])
    con.commit()

    cursor.execute(
        "SELECT * FROM questions "+"where id = '%s' ", [body['id']])
    updated = cursor.fetchall()
    cursor.close()
    con.close()
    return updated


def delete_question(_id):
    try:
        query = 'DELETE FROM questions WHERE id= %s'
        con = connect()
        cursor = con.cursor()
        cursor.execute(query, [_id])
        con.commit()
        return {"Message": "question deleted"}
    except:
        return {
            "Message": 'question ot found'
        }


def get_all(key):
    con = connect()
    cursor = con.cursor()
    query = ('select * from questions where activitye_key  = %s')
    cursor.execute(query, [key])
    records = cursor.fetchall()
    cursor.close()
    con.close()
    return records

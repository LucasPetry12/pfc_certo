from .connection import connect
from mysql.connector import Error


def get_a_activity(act_id):
    con = connect()
    cursor = con.cursor()

    cursor.execute('select * from activityes where id = "{}"'.format(act_id))
    records = cursor.fetchall()
    return records


def get_my_activityes(teacher_id):
    con = connect()
    cursor = con.cursor()
    query = ('select * from activityes where teacher_id = %s')
    cursor.execute(query, [teacher_id])
    records = cursor.fetchall()
    cursor.close()
    con.close()
    return records


def create_activity(data, code):

    con = connect()
    cursor = con.cursor()
    body = data['body']
    headers = data['headers']
    sql = 'INSERT INTO activityes(subject, matter, 	series, qtds_groups, show_author,punctuation_type, teacher_id, code) values("%s","%s","%s","%s","%s","%s","%s","%s")'
    cursor.execute(sql, (body['subject'], body['matter'], body['series'],
                   body['qtds_groups'], body['show_author'], body['punctuation_type'], headers['id'], code[0]))
    con.commit()

    created = get_a_activity(cursor.lastrowid)
    cursor.close()
    con.close()

    return created


def get_a_activity_from_code(code):
    con = connect()
    cursor = con.cursor()

    cursor.execute('select * from activityes where code = "{}"'.format(code))
    records = cursor.fetchall()

    return records


def update_a_activity(body):
    try:
        body = body['body']
        con = connect()
        cursor = con.cursor()
        sql_edit = 'UPDATE activityes SET subject= %s, matter = %s, series = %s, qtds_groups= %s, show_author=%s, punctuation_type=%s  where code = %s '
        cursor.execute(
            sql_edit, [body['subject'], body['matter'], body['series'], body['qtds_groups'], body['show_author'], body['punctuation_type'], body['code']])
        con.commit()

        cursor.execute(
            "SELECT * FROM activityes where code = %s ", [body['code']])
        updated = cursor.fetchall()
        cursor.close()
        con.close()
        return updated
    except:
        return {"Message": "Atividade não deletada"}


def delet_activity(code):
    try:
        query = 'DELETE FROM activityes WHERE code= %s'
        con = connect()
        cursor = con.cursor()
        cursor.execute(query, [code])
        con.commit()
        return {"Message": "Atividade deletada"}
    except:
        return {
            "error": 'error'
        }

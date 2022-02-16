from ..models import questions
from ..models import activity
from ..helpers.skeletons import question_skeleton
from ..helpers.serializer import serializer


def create(body):

    activity_id = activity.get_a_activity_from_code(body['code'])
    response = questions.create_a_question(body, activity_id[0])
    return {"main": serializer.serialize(question_skeleton.question_skeleton(), response[0])}


def get(data):
    return serializer.serialize__many(question_skeleton.question_skeleton(), questions.get_all(data['_id']))


def edit(data):
    return serializer.serialize(question_skeleton.question_skeleton(), questions.edit_question(data)[0])


def delete(data):
    return questions.delete_question(data['_id'])


def get_from_key(key):
    try:
        return serializer.serialize__many(question_skeleton.question_skeleton(), questions.get_all(key))
    except:
        return {"Message": "Não uma questão"}

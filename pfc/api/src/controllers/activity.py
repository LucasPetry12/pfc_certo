from urllib import response
from ..models import activity
from ..helpers.serializer import serializer
from ..helpers.skeletons import activity_skeleton
import re
import uuid


def get_from_code(code):

    return serializer.serialize(activity_skeleton.activity_skeleton(), activity.get_a_activity_from_code(code)[0])


def create(data):
    try:
        code = uuid.uuid4().hex
        result = re.search('(.{8}$)', code)

        activity_create = activity.create_activity(data, result.groups(1))
        response = serializer.serialize(
            activity_skeleton.activity_skeleton(), activity_create[0])
        response['headers'] = data['headers']
        return response
    except:
        return {'message': 'erro'}


def get_my_all(body):
    response = activity.get_my_activityes(body['headers']['id'])
    return serializer.serialize__many(activity_skeleton.activity_skeleton(), response)


def login(body):
    try:
        response = activity.get_a_activity_from_code(body['code'])
        return {'activity': serializer.serialize(activity_skeleton.activity_skeleton(), response[0])}
    except:
        return 'not found'


def update_activity(body):
    try:
        return {'activity': serializer.serialize(activity_skeleton.activity_skeleton(), activity.update_a_activity(body)[0])}
    except:
        {"Message": "Invalida filleds"}


def delet_activity(body):

    compare = serializer.serialize(
        activity_skeleton.activity_skeleton(),  activity.get_a_activity_from_code(body['code'])[0])
    if(int(compare['teacher_id']) == int(compare['teacher_id'])):
        return activity.delet_activity(body['code'])
    else:
        return {"Message": "Essa atividade não e sua"}

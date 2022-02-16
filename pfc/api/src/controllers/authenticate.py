from urllib import response
from ..models.teachers_model import create_new_teacher, get_a_teacher, edit_a_teacher, delet_a_teacer
from ..utils import hash_str, render
from ..helpers.serializer import serializer
from ..helpers.skeletons import teacher_skeleton
from ..middlewares import auth_middleware


def register(body):

    name = body['name']
    password = body['password']
    email = body['email']
    confirm_password = body['confirm_password']

    if confirm_password != password:
        return 'As senhas não são as mesmas'

    if len(name) < 3:
        return 'name is very small'
    if len(password) < 6:
        return 'Senha muito pequena!'

    name = name.lower()
    password = hash_str.hash_str(password)

    teacher = create_new_teacher(name, password, email)
    return render.render__one(teacher, auth_middleware.create(teacher))


def login(body):

    email = body['email']
    password = body['password']

    teacher = get_a_teacher(email)
    try:
        compare_hashs = hash_str.compare(password, teacher[0][3])
        if compare_hashs == "Senha errada":
            return compare_hashs
        else:
            return render.render__one(teacher, auth_middleware.create(teacher))
    except:
        return 'Este usuário não existe'


def forgot_password(body):
    return {'message', "calma"}


def edit_teacher(body):
    try:
        response = serializer.serialize(teacher_skeleton.teacher_skeleton(
        ), edit_a_teacher(body['headers']['id'], body['body'])[0])
        response.pop('password', None)
        return response
    except:
        return {
            "_Message": "Error in params",
            "Expected": {
                "name": "string",
                "email": "string",
                "password": "string"
            },
            "recive": body['body']
        }


def delet_teacher(body):
    if int(body['headers']['id']) == int(body['route_id']):
        return delet_a_teacer(body['route_id'])
    else:
        return {
            "Message": "Ivavlid id"
        }

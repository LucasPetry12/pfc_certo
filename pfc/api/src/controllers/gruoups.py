from ..models import groups
from ..helpers.skeletons import group_skeleton
from ..helpers.serializer import serializer


def set_group(body):

    return serializer.serialize(group_skeleton.group_skeleton(),   groups.set_group(body)[0])


def get_group(_id):
    return serializer.serialize(group_skeleton.group_skeleton(),  groups.get_group(int(_id))[0])


def define_group(data):
    return serializer.serialize(group_skeleton.group_skeleton(), groups.define_group(data['group'], data['id'])[0])


def all_groups():
    return serializer.serialize__many(group_skeleton.group_skeleton(), groups.get_all())


def all_code(code):

    return serializer.serialize__many(group_skeleton.group_skeleton(), groups.get_all__code(code['code']))

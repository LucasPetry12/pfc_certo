def serialize(skeleton, values):

    serialized = dict()
    for i, key in enumerate(skeleton):
        serialized[key] = values[i]
    return serialized


def serialize__many(sekeleton, values):
    serialized_many = []
    for key in values:
        temp = serialize(sekeleton, key)
        serialized_many.append(temp)
    return serialized_many

def render__one(argument, token):
    
    if isinstance(argument, str):
        return argument
    else:
        render = list(argument[0])
        render = render[:-1]

        response = dict(id=render[0], name=render[1],
                        email=render[2], token=token)
    return response


def render_many(array):
    elements = []

    for element in array:
        elements.append(element[:-1])
    return elements

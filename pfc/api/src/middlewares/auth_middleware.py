import jwt
import datetime


def create(user):

    if isinstance(user, str):
        return 0
    user_control = user[0]
    payload = {
        "id": user_control[0],
        "user": user_control[2],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
    }

    token = jwt.encode(payload, 'miranha', algorithm='HS256')
    return token


def authorization(token):
    if token.find('Bearer') == -1:
        return 'token mal formatado'
    else:
        token = token.replace('Bearer ', '')

        def return__jwt():
            try:
                carga = jwt.decode(token, 'miranha', algorithms=['HS256'])
                data = []
                data.append(carga.get('id'))
                data.append(carga.get('user'))

                data_new_token = dict(
                    id=data[0], email=data[1], token=create([[data[0], '', data[1]]]))
                return data_new_token
            except:
                return 'Token não validado!'
    return return__jwt()

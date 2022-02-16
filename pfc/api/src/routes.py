from .controllers import authenticate, activity, questions, gruoups
from flask import request, jsonify
from flask_cors import cross_origin
from .middlewares import auth_middleware


def routes(app):
    @app.route('/auth/register', methods=['POST'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def register():
        body = request.get_json()
        return jsonify(authenticate.register(body))

    @app.route('/auth/login', methods=['POST'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def login():
        body = request.get_json()
        return jsonify(authenticate.login(body))

    @app.route('/auth/edit', methods=['PUT'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def edit_teacher():
        try:
            body = request.get_json()
            token = request.headers['Authorization']
            autorized = auth_middleware.authorization(token)
            full_data = dict(headers=autorized, body=body)

            if isinstance(autorized, dict):
                return jsonify(authenticate.edit_teacher(full_data))
            else:
                return autorized
        except:
            return jsonify(
                {
                    "Message": "Token não aprovada!"
                })

    @app.route('/auth/delete/<_id>', methods=['DELETE'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def delet_teacher(_id):
        try:
            body = request.get_json()
            token = request.headers['Authorization']
            autorized = auth_middleware.authorization(token)
            full_data = dict(headers=autorized, body=body, route_id=_id)

            if isinstance(autorized, dict):
                return jsonify(authenticate.delet_teacher(full_data))
            else:
                return autorized
        except:
            return jsonify(
                {
                    "Message": "Tokens não aprovada"
                })

    @app.route('/activity/create', methods=['POST'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def create_activity():
        try:
            body = request.get_json()
            token = request.headers['Authorization']
            autorized = auth_middleware.authorization(token)
            full_data = dict(headers=autorized, body=body)

            if isinstance(autorized, dict):
                return jsonify(activity.create(full_data))
            else:
                return autorized
        except:
            return jsonify(
                {
                    "Message": "Tokens não aprovada"
                })

    @app.route('/activity/code', methods=['POST'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def login_code():
        body = request.get_json()
        return jsonify(activity.login(body))

    @app.route('/activity/getcode/<code>', methods=['GET'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def get_from_code(code):
        return jsonify(activity.get_from_code(code))

    @app.route('/activity/get', methods=['GET'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def get_my():
        body = request.get_json()
        token = request.headers['Authorization']
        autorized = auth_middleware.authorization(token)
        full_data = dict(headers=autorized, body=body)
        return jsonify(activity.get_my_all(full_data))

    @app.route('/activity/update', methods=['PUT'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def update_activity():
        try:
            body = request.get_json()
            token = request.headers['Authorization']
            autorized = auth_middleware.authorization(token)
            full_data = dict(headers=autorized, body=body)

            if isinstance(autorized, dict):
                return jsonify(activity.update_activity(full_data))
            else:
                return autorized
        except:
            return jsonify({"Message": "Token não aprovada"})

    @app.route('/activity/delete/<code>', methods=['DELETE'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def delet_activity(code):
        try:
            token = request.headers['Authorization']
            autorized = auth_middleware.authorization(token)
            full_data = dict(headers=autorized, code=code)

            if isinstance(autorized, dict):
                return jsonify(activity.delet_activity(full_data))
            else:
                return autorized
        except:
            return jsonify({"Message": "Token não aprovada"})

    @app.route('/questions/create', methods=['POST'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def create_question():
        body = request.get_json()
        return jsonify(questions.create(body))

    @app.route('/questions/edit', methods=['PUT'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def edit_question():
        body = request.get_json()
        token = request.headers['Authorization']
        autorized = auth_middleware.authorization(token)
        full_data = dict(headers=autorized, body=body)

        if isinstance(autorized, dict):
            return jsonify(questions.edit(full_data))
        else:
            return autorized

    @app.route('/questions/delete/<_id>', methods=['DELETE'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def delete_question(_id):
        token = request.headers['Authorization']
        autorized = auth_middleware.authorization(token)
        full_data = dict(headers=autorized, _id=_id)

        if isinstance(autorized, dict):
            return jsonify(questions.delete(full_data))
        else:
            return autorized

    @app.route('/questions/get/<_id>', methods=['GET'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def get_many(_id):
        token = request.headers['Authorization']
        autorized = auth_middleware.authorization(token)
        full_data = dict(headers=autorized, _id=_id)

        if isinstance(autorized, dict):
            return jsonify(questions.get(full_data))
        else:
            return autorized

    @app.route('/questions/getall/<_key>', methods=['GET'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def get_all_from_key(_key):
        return jsonify(questions.get_from_key(_key))

    @app.route('/group/set', methods=['POST'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def set_group():
        body = request.get_json()
        return jsonify(gruoups.set_group(body))

    @app.route('/group/get/<_id>', methods=['GET'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def get_group(_id):
        return jsonify(gruoups.get_group(_id))

    @app.route('/group/getall/', methods=['GET'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def get_allgroup():
        return jsonify(gruoups.all_groups())

    @app.route('/group/define', methods=['POST'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def define_group():
        body = request.get_json()
        return jsonify(gruoups.define_group(body))

    @app.route('/group/code', methods=['POST'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def get_all_code():
        body = request.get_json()
        return jsonify(gruoups.all_code(body))

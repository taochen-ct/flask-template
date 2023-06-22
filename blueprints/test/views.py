import json
from flask import jsonify, views, request
from flask_api import status
from models import User
from extensions import db
from blueprints.test.serializer import UserSerializer


class UserViewSet(views.MethodView):

    def get(self, test_id):
        if test_id:
            user = db.session.query(User).filter_by(id=test_id).first()
            serializer = UserSerializer(instance=user)
            return jsonify(serializer.data), 200

        user = db.session.query(User).all()
        # user = User.query.all()
        serializer = UserSerializer(instance=user, many=True)
        return jsonify(serializer.data), status.HTTP_200_OK

    def post(self):
        data = json.loads(request.data)
        serializer = UserSerializer(data=data)
        try:
            new_ojb = serializer.save()
            return jsonify(new_ojb), status.HTTP_200_OK
        except Exception as e:
            print(e)
            return jsonify(e), status.HTTP_500_INTERNAL_SERVER_ERROR

    def put(self, test_id):
        data = json.loads(request.data)
        user = db.session.query(User).get(test_id)
        serializer = UserSerializer(instance=user, data=data)
        if user.id == serializer.valided_data['id']:
            new_obj = serializer.update()
            return jsonify(new_obj), status.HTTP_200_OK
        return {"msg":"修改失败"}, status.HTTP_200_OK

    def delete(self, test_id):
        user = db.session.query(User).get(test_id)
        try:
            db.session.delete(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        return jsonify({}), status.HTTP_200_OK
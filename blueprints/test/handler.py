import json
from flask_api import status
from flask_restful import Resource, request
from models import User
from extensions import db
from blueprints.test.serializer import UserSerializer


class UserListApi(Resource):
    def get(self):
        user = db.session.query(User).all()
        serializer = UserSerializer(instance=user, many=True)
        return {"data": serializer.data}, status.HTTP_200_OK

    def post(self):
        data = request.get_json()
        serializer = UserSerializer(data=data)
        try:
            new_ojb = serializer.save()
            return new_ojb, status.HTTP_200_OK
        except Exception as e:
            return {"msg": "注册失败", "error": str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR


class UserApi(Resource):
    def get(self, test_id):
        user = db.session.query(User).filter_by(id=test_id).first()
        serializer = UserSerializer(instance=user)
        return {"data": serializer.data} if serializer.data is not None else {"data": {}}, 200

    def put(self, test_id):
        data = json.loads(request.data)
        user = db.session.query(User).get(test_id)
        serializer = UserSerializer(instance=user, data=data)
        if user.id == serializer.valided_data["id"]:
            new_obj = serializer.update()
            return {"data": new_obj}, status.HTTP_200_OK
        return {"msg": "修改失败"}, status.HTTP_200_OK

    def delete(self, test_id):
        user = db.session.query(User).get(test_id)
        try:
            db.session.delete(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"msg": "删除失败", "error": str(e)}
        return {"data": {}}, status.HTTP_200_OK

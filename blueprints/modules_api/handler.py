# coding=utf-8
"""
@Modify Time :2023/6/11 11:28    
@Author      :tao.chen 
"""
import uuid
import datetime
import json
from flask_api import status
from flask_restful import Resource, request
from extensions import db
from models import Modules
from .serializer import ModulesSerializer


class ModuleListAPI(Resource):
    def get(self):
        module = db.session.query(Modules).all()
        serializer = ModulesSerializer(instance=module, many=True)
        return {
            "code": 200,
            "msg": "success",
            "data": {"data": serializer.data, "total": len(serializer.data)},
        }, status.HTTP_200_OK

    def post(self):
        data = {
            "uid": uuid.uuid4(),
            "create_time": str(datetime.date.today()),
            "modify_time": str(datetime.date.today()),
            **request.get_json(),
        }

        serializer = ModulesSerializer(data=data)
        try:
            new_ojb = serializer.save()
            return {"code": 200, "msg": "success", "data": new_ojb}, status.HTTP_200_OK
        except Exception as e:
            return {"code": 500, "msg": "failed", "data": str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR


class ModuleAPI(Resource):
    def get(self, module_uid):
        module = db.session.query(Modules).filter_by(uid=module_uid).first()
        serializer = ModulesSerializer(instance=module)
        return {
            "code": 200,
            "msg": "success",
            "data": {"data": serializer.data} if serializer.data is not None else {"data": {}},
        }, status.HTTP_200_OK

    def put(self, module_uid):
        data = json.loads(request.data)
        module = db.session.query(Modules).get(module_uid)
        serializer = ModulesSerializer(instance=module, data=data)
        if module.uid == serializer.valided_data["uid"]:
            new_obj = serializer.update()
            return {
                "code": 200,
                "msg": "success",
                "data": {"data": new_obj},
            }, status.HTTP_200_OK
        return {
            "code": 200,
            "msg": "failed",
            "data": {},
        }, status.HTTP_200_OK

    def delete(self, module_uid):
        module = db.session.query(Modules).get(module_uid)
        try:
            db.session.delete(module)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {
                "code": 200,
                "msg": "failed",
                "data": {"error": str(e)},
            }, status.HTTP_200_OK
        return {
            "code": 200,
            "msg": "success",
            "data": {},
        }, status.HTTP_200_OK

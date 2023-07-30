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
from models import Bugs
from .serializer import BugsSerializer


class BugListAPI(Resource):
    def get(self):
        bug = Bugs.query.all()
        serializer = BugsSerializer(instance=bug, many=True)
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

        serializer = BugsSerializer(data=data)
        try:
            new_ojb = serializer.save()
            return {"code": 200, "msg": "success", "data": new_ojb}, status.HTTP_200_OK
        except Exception as e:
            return {"code": 500, "msg": "failed", "data": str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR


class BugAPI(Resource):
    def get(self, bug_uid):
        bug = Bugs.query.filter_by(uid=bug_uid).first()
        serializer = BugsSerializer(instance=bug)
        return {
            "code": 200,
            "msg": "success",
            "data": {"data": serializer.data} if serializer.data is not None else {"data": {}},
        }, status.HTTP_200_OK

    def put(self, bug_uid):
        data = json.loads(request.data)
        bug = Bugs.query.get(bug_uid)
        serializer = BugsSerializer(instance=Bugs, data=data)
        if bug.uid == serializer.valided_data["uid"]:
            new_obj = serializer.update()
            return {
                "code": 200,
                "msg": "success",
                "data": {"data": new_obj},
            }, status.HTTP_200_OK
        return {
            "code": 500,
            "msg": "failed",
            "data": {},
        }, status.HTTP_500_INTERNAL_SERVER_ERROR

    def delete(self, bug_uid):
        bug = Bugs.query.get(bug_uid)
        try:
            db.session.delete(bug)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {
                "code": 500,
                "msg": "failed",
                "data": {"error": str(e)},
            }, status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "code": 200,
            "msg": "success",
            "data": {},
        }, status.HTTP_200_OK

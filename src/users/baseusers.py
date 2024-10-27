import requests
import json

from src.baseapi import BaseReq


class UserReq(BaseReq):
    @classmethod
    def get_list_users(cls) -> None:
        respone = cls.session.post(f"{cls.base_url}/panel/inbound/list")
        if respone.status_code == 200:
            data = respone.json()
            return data
        return None
    

    @classmethod
    def get_user_info(cls, user_id) -> None:
        response = cls.session.post(f"{cls.base_url}/panel/inbound/list")
        if response.status_code == 200:
            data = response.json()
            for client in data["obj"]:
                if client["remark"].split("=")[0] == user_id:
                    return client
            return {"status": "Client not founted"}
        

    @classmethod
    def onlines(cls):
        online = {}

        online_users = cls.session.post(f"{cls.base_url}/panel/inbound/onlines")
        users = cls.session.post(f"{cls.base_url}/panel/inbound/list")
        
        if online_users.status_code == 200 and users.status_code == 200:
            data = online_users.json()["obj"]
            for clinet_key in data:
                for user in users.json()["obj"]:
                    for key in user["clientStats"]:
                        if key["email"] == clinet_key:
                            online[clinet_key] = user["remark"]
            return online

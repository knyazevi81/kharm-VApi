import requests
from src.baseapi import BaseReq


class UserReq(BaseReq):

    @classmethod
    def get_list_users(cls) -> None:
        respone = cls.session.post(f"{cls.base_url}/panel/inbound/list")
        data = respone.json()
        return data
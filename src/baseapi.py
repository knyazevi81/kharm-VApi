from requests import Session, get, post
import json

from src.config import settings

class BaseReq:
    auth_data = {
        "username": settings.login,
        "password": settings.password
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }
    base_url: str = settings.base_url
    
    with Session() as session:
        session.headers.update(headers)
        resp = session.post(
            f"{base_url}/login",
            data=auth_data
        )
        
        
    
    @classmethod
    def get_list_users(cls) -> None:
        respone = cls.session.post(f"{cls.base_url}/panel/inbound/list")
        data = respone.json()
        return data
    

if __name__ == "__main__":
    print(BaseReq.get_list_users())


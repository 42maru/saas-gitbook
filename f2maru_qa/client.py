import json
import logging
from typing import List

import requests

logger = logging.getLogger(__name__)


class Client(object):
    def __init__(self, app_code: str, api_key: str, **kwargs):
        self._app_code: str = app_code
        self._api_key: str = api_key
        self._config: str = kwargs

        # todo domain setting 필요.
        self.__host = '13.209.5.247'
        self.__bulk_path = '/api/application/documents/bulk'
        self.__broker_path = '/api/broker'

        self.__headers = {'Content-Type': 'application/json; charset=utf-8'}
        self.__headers.update({
            'X-PLATFORM42-API-KEY': api_key,
            'X-PLATFORM42-APP-ID': app_code
        })

    def bulk_insert(self, data: List[dict]) -> bool:

        def validation(obj: dict):
            assert "title" in obj, "title is mandatory"
            assert "content" in obj, "content is mandatory"
            assert obj['content'], "content can not be empty"

        def validations(objects: List[dict]):
            [validation(obj) for obj in objects]

        validations(data)

        try:
            requests.post(self.__write_url, data=json.dumps(data), headers=self.__headers)
            return True
        except Exception as e:
            logger.error("fail add new object [Error Msg] ({})".format(str(e)))
            return False

    def insert(self, data: dict) -> bool:
        return self.bulk_insert([data])

    def inquiry(self, query: str, answer_count: int = 3):
        # todo debug없으면 동작안함.
        payload = {'query': query, 'count': answer_count, 'debug': False}
        res = requests.get(self.__read_url, params=payload, headers=self.__headers)
        return res.json() if res and res.status_code == 200 else None

    @property
    def __write_url(self):
        return "http://{}{}".format(self.__host, self.__bulk_path)

    @property
    def __read_url(self):
        return "http://{}{}".format(self.__host, self.__broker_path)

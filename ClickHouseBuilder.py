from __future__ import annotations
from ClickHouse import ClickHouse
from ClickHouseRequest import ClickHouseRequest


class ClickHouseBuilder:
    def __init__(self):
        self.clickHouseRequest = ClickHouseRequest()

    def set_host(self, host: str, port: str) -> ClickHouseBuilder:
        self.clickHouseRequest.host = host
        self.clickHouseRequest.port = port
        return self

    def set_user(self, user: str, password: str) -> ClickHouseBuilder:
        self.clickHouseRequest.user = user
        self.clickHouseRequest.password = password
        return self

    def set_db(self, db: str) -> ClickHouseBuilder:
        self.clickHouseRequest.db = db
        return self

    def set_ssl(self, ssl_path: str) -> ClickHouseBuilder:
        try:
            with open(ssl_path, 'r', encoding='utf-8') as file:
                assert (file.readable() is True), 'Сертификат пуст'
        except IOError as e:
            print(f'Файл {ssl_path} не найден!')
            return self
        except Exception as e:
            print('Сертификат пуст')
            print(e.args)
            return self
        self.clickHouseRequest.verify = ssl_path
        return self

    def build(self) -> ClickHouse:
        return ClickHouse(self.clickHouseRequest)
from __future__ import annotations

import requests


class ClickHouseRequest:
    def __init__(self):
        self.host = ""
        self.port = ""
        self.db = ""
        self.verify = ""
        self.user = ""
        self.password = ""

    def _request(self, url: str, auth: dict):
        res = requests.get(
            url,
            headers=auth,
            verify=self.verify)
        res.raise_for_status()
        return res.text

    def _get_url(self, query):
        return 'https://{host}:{port}/?database={db}&query={query}'.format(
                host=self.host,
                db=self.db,
                port=self.port,
                query=query)

    def _get_auth(self):
        return {
            'X-ClickHouse-User': self.user,
            'X-ClickHouse-Key': self.password,
        }

    def execute(self, sql: str):
        return self._request(self._get_url(sql), self._get_auth())

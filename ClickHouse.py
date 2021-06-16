from ClickHouseRequest import ClickHouseRequest


class ClickHouse:
    def __init__(self, clickHouseRequest: ClickHouseRequest):
        self.clickHouseRequest = clickHouseRequest

    def show_databases(self):
        return self.clickHouseRequest.execute('SHOW DATABASES')

    def create_person(self):
        return self.clickHouseRequest.execute("CREATE TABLE hibd.person('person_id' UInt32, "
                                              "                     'person_name' String)")

    def insert_person(self, person_id:str, name: str):
        return self.clickHouseRequest.execute(f"INSERT INTO PERSON(PERSON_ID, NAME) VALUES ({person_id}, '{name}')")

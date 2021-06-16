from ClickHouseBuilder import ClickHouseBuilder

if __name__ == "__main__":
    clickhouse = ClickHouseBuilder() \
        .set_host("rc1c-6u198mx1pjius40t.mdb.yandexcloud.net", "8443") \
        .set_user("dreamteam", "P@ssw0rd") \
        .set_db("hibd") \
        .set_ssl(".\\YandexInternalRootCA.crt") \
        .build()
    print(clickhouse.show_databases())

    print(clickhouse.create_person())


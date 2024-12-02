import pymysql


class TestFetchSmsRecord():
    """
    该类用于测试从数据库中获取最新的短信记录。
    """

    def test_1(self, db_connection):
        """
        测试从数据库中获取最新的短信记录，步骤包括：
        1. 连接数据库并执行查询，获取最新的短信记录。
        2. 如果有记录，打印记录的ID、验证码和手机号码；如果没有记录，打印提示信息。

        :param db_connection: pytest 提供的数据库连接对象。
        """
        connection = db_connection

        # 执行查询
        try:
            with connection.cursor() as cursor:
                query = """
                SELECT
                    id, 
                    `code`, 
                    phone_number
                FROM
                    sys_sms_record
                ORDER BY id DESC
                LIMIT 1
                """
                cursor.execute(query)
                result = cursor.fetchone()

                if result:
                    print(
                        f"Latest record - ID: {result[0]}, Code: {result[1]}, Phone Number: {result[2]}"
                    )
                else:
                    print("No records found.")
        except pymysql.MySQLError as e:
            print(f"Error executing query: {e}")

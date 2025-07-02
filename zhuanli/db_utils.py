import pymysql


class DBUtils:
    def __init__(self):
        self.connect = None

    def open_connect(self):
        try:
            self.connect = pymysql.connect(
                host='localhost',
                user='root',
                password='1234',
                database='zhuanli',
                charset='utf8mb4'
            )
        except Exception as ex:
            print('数据库连接异常', ex)

    def close_connect(self):
        if self.connect and self.connect.open:
            self.connect.close()

    def get_patent_sum(self):
        self.open_connect()
        try:
            with self.connect.cursor() as cursor:
                sql = 'SELECT COUNT(*) FROM `patent_info`'
                cursor.execute(sql)
                return cursor.fetchone()
        except Exception as ex:
            print('数据库操作异常', ex)
            return (0,)  # 返回默认值
        finally:
            self.close_connect()

    def get_type_count(self):
        self.open_connect()
        try:
            with self.connect.cursor() as cursor:
                sql = 'SELECT `keyword` FROM `patent_info`'
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as ex:
            print('数据库操作异常', ex)
            return []  # 返回空列表
        finally:
            self.close_connect()

    def get_patent(self):
        self.open_connect()
        try:
            with self.connect.cursor() as cursor:
                sql = 'SELECT * FROM `patent_info`'
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as ex:
            print('数据库操作异常', ex)
            return []  # 返回空列表
        finally:
            self.close_connect()

    def get_count_by_province(self):
        self.open_connect()
        try:
            with self.connect.cursor() as cursor:
                sql = 'SELECT province, nums FROM `province_patent`'
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as ex:
            print('数据库操作异常', ex)
        finally:
            self.close_connect()
import sqlite3


class Database(object):
    def __init__(self):
        """
        初始化函数，创建数据库连接
        """
        self.conn = sqlite3.connect('data.sqlite')
        self.c = self.conn.cursor()

    def update(self, sql):
        """
        数据库的插入、修改函数
        :param sql: 传入的SQL语句
        :return: 返回操作数据库状态
        """
        try:
            self.c.execute(sql)
            i = self.conn.total_changes
        except Exception as e:
            print('错误类型： ', e)
            raise  # 抛出异常，让调用程序捕获，以便在界面上显示异常信息
        finally:
            self.conn.commit()
        if i > 0:
            return True
        else:
            return False

    def delete(self, sql):
        """
        操作数据库数据删除的函数
        :param sql: 传入的SQL语句
        :return: 返回操作数据库状态
        """
        try:
            self.c.execute(sql)
            i = self.conn.total_changes
        except Exception as e:
            return False
        finally:
            self.conn.commit()
        if i > 0:
            return True
        else:
            return False

    def query(self, sql):
        """
        数据库数据查询
        :param sql: 传入的SQL语句
        :return: 返回操作数据库状态
        """
        return self.c.execute(sql)

    def close(self):
        """
        关闭数据库相关连接的函数
        :return:
        """
        self.c.close()
        self.conn.close()

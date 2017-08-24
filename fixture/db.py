import pymysql.cursors
from contextlib import contextmanager
from model.group import Group
from model.contact import Contact

class DbFixture:
    def __init__(self, host, name, user, password):
        self.name = name
        self.host = host
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host = host,
                                     database = name,
                                     user = user,
                                     password = password,
                                     autocommit=True)

    @contextmanager
    def cursor_(self):
        cursor = self.connection.cursor()
        yield cursor
        cursor.close()

    def get_group_list(self):
        list = []
        with self.cursor_() as cursor:
            try:
                cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
                for row in cursor:
                    (id, name, header, footer) = row
                    list.append(Group(id = str(id), name = name, header = header, footer=footer))
            finally:
                cursor.close()
        return list

    def get_contact_list(self):
        list = []
        with self.cursor_() as cursor:
            try:
                cursor.execute("select id, firstname, lastname from addressbook  where deprecated='0000-00-00 00:00:00'")
                for row in cursor:
                    (id, firstname, lastname) = row
                    list.append(Contact(id = str(id),
                                        firstname = firstname,
                                        lastname = lastname))
            finally:
                cursor.close()
        return list






    def destroy(self):
        self.connection.close()
# try:
#     cursor = connection.cursor()
#     cursor.execute("select * from group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()
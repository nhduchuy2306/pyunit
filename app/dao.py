from connectDB import *
from user import *

class DAO():
    def get_all_user(self):
        conn = ConnectDB().db_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tblUsers")
        data = []
        for row in cursor:
            u = User(row[0], row[1], row[2], row[3], row[4])
            data.append(u)
        cursor.close()
        conn.close()
        return data
    
    def get_user_by_id(self, user_id):
        conn = ConnectDB().db_connect()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM tblUsers WHERE userID = ?
            """,user_id)
        data = []
        for row in cursor:
            u = User(row[0], row[1], row[2], row[3], row[4])
            data.append(u)
        cursor.close()
        conn.close()
        return data

if __name__ == '__main__':
    d = DAO()
    # data = d.get_user_by_id("SE130363")
    data = d.get_all_user()
    for i in data:
        print(i.display())
    
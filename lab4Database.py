import pymssql

class Database:
    __connection = None

    @classmethod
    def connect(cls):
        if cls.__connection is None:
            cls.__connection = pymssql.connect(
                server='cisdbss.pcc.edu',
                user='275student',
                password='275student',
                database='NAMES'
            )
        return cls.__connection

    @classmethod
    def readNames(cls, year, gender):
        cls.connect()
        cursor = cls.__connection.cursor(as_dict=True)
        sql = """
              SELECT TOP 20 Name, Gender, Year, NameCount AS "Count"
              FROM all_data
              WHERE Year = %s
              AND Gender = %s; 
              """
        cursor.execute(sql, (year, gender))
        rows = cursor.fetchall()
        cursor.close()

        return rows


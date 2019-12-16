from db import config
from mysql.connector import (connection)
import time
import calendar


class ClassRoom:

    @staticmethod
    def getActualClass(classroom_nro):
        conex = connection.MySQLConnection(**config)
        cursor = conex.cursor()
        try:
            query = (
                "SELECT reservations.machid, resources.name, reservations.start_date, reservations.starttime, reservations.endtime, reservations.summary "
                "FROM reservations "
                "INNER JOIN	resources ON reservations.machid=resources.machid "
                "WHERE resources.name LIKE %s ESCAPE '' "
                "AND (%s BETWEEN (reservations.start_date + 60*reservations.starttime) AND (reservations.end_date + 60*reservations.endtime)) LIMIT 1")

            cursor.execute(query,('%{}%'.format(classroom_nro),calendar.timegm(time.localtime())))
            return cursor.fetchone()
        except cursor.Error as e:
            print("getActualClass: {}".format(e))
        finally:
            if cursor is not None:
                cursor.close()
                conex.close()



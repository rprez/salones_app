from db import cursor
import time
import calendar

class ClassRoom():

    @staticmethod
    def getActualClass(classroom_nro):
        query = (
            "SELECT reservations.machid, resources.name, reservations.start_date, reservations.starttime, reservations.endtime, reservations.summary "
            "FROM reservations "
            "INNER JOIN	resources ON reservations.machid=resources.machid "
            "WHERE resources.name LIKE %s ESCAPE '' "
            "AND (%s BETWEEN (reservations.start_date + 60*reservations.starttime) AND (reservations.end_date + 60*reservations.endtime))")

        cursor.execute(query,('%{}%'.format(classroom_nro),calendar.timegm(time.localtime())))
        return cursor.fetchone()




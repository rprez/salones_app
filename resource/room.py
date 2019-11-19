from db import cursor


class ClassRoom():

    @staticmethod
    def getActualClass(classroom_nro):
        query = (
            "SELECT reservations.machid, resources.name, reservations.start_date, reservations.starttime, reservations.endtime, reservations.summary "
            "FROM reservations "
            "INNER JOIN	resources ON reservations.machid=resources.machid "
            "WHERE resources.name LIKE %s ESCAPE '' "
            "AND (UNIX_TIMESTAMP(NOW()) BETWEEN (reservations.start_date + 60*reservations.starttime) AND (reservations.start_date + 60*reservations.endtime))")

        cursor.execute(query,(f'%{classroom_nro}%',))
        return cursor.fetchone()




from control.cursorDB import cursorDB

import os
import mysql.connector as mysql

class controlDB(cursorDB):
    def __init__(self, group_id, users_id_lastupdater=None):
        super().__init__()
        print('class getData')
        self.url = str(os.getenv('GLPI_URL'))+"/front/ticket.form.php?id="
        self.groups_id = group_id
        self.users_id_lastupdater = users_id_lastupdater

        if users_id_lastupdater==None:
             self.sql_query = ''' 
            SELECT
                gt.id as "id",
                concat("{}", gt.id) as "url",
                gt.date_mod as "last_update"
            FROM
                glpi_tickets gt, glpi_groups_tickets gpt
            WHERE
                gt.is_deleted = 0 AND 
                gt.`status` IN (1,2,3,4) AND 
                gpt.tickets_id = gt.id AND
                gpt.groups_id = {} AND
                gt.date_mod >= (NOW() - INTERVAL 3 DAY)
            '''.format(self.url, self.groups_id)
        else:
            self.sql_query = ''' 
                SELECT
                    gt.id as "id",
                    concat("{}", gt.id) as "url",
                    gt.date_mod as "last_update"
                FROM
                    glpi_tickets gt, glpi_groups_tickets gpt
                WHERE
                    gt.is_deleted = 0 AND 
                    gt.`status` IN (1,2,3,4) AND 
                    gpt.tickets_id = gt.id AND
                    gpt.groups_id = {} AND
                    gt.date_mod >= (NOW() - INTERVAL 3 DAY) AND
                    gt.users_id_lastupdater NOT LIKE {}
                '''.format(self.url, self.groups_id, self.users_id_lastupdater)

    def getData(self):
        self.mycursor.execute(self.sql_query)
        self.row_headers = [x[0] for x in self.mycursor.description]
        self.dataSqlFetchall = self.mycursor.fetchall()

        return(self.row_headers, self.dataSqlFetchall)
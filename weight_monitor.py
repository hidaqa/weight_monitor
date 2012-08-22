# -*- coding: utf-8 -*-

import gdata.calendar.service
import gdata.spreadsheet.text_db

class GoogleCalendar:
    def __init__(self, user, passwd):
        self.client = gdata.calendar.service.CalendarService()
        self.client.email = user
        self.client.password = passwd
        self.client.source = 'Google-Calendar_Python_Sample-1.0'
        self.client.ProgrammaticLogin()

    def GetWeightList(self, start, end):
        UNIT = 'kg'
        query = gdata.calendar.service.CalendarEventQuery(user, 'private', 'full', UNIT)
        query.start_min = start
        query.start_max = end
        query.orderby = 'starttime'
        query.sortorder = 'a'
        query.singleevents = 'false'
        feed = self.client.CalendarQuery(query)
        weightList = [ { 'date': event.when[0].start_time, 'weight':event.title.text.replace(UNIT,'') } for event in feed.entry]
        return weightList

class GoogleSpreadsheet:
    def __init__(self, user, passwd):
        self.client = gdata.spreadsheet.text_db.DatabaseClient(user, passwd)

    def UpdateRecords(self, weightList):
        db = self.client.GetDatabases(name='Weight Control')[0]
        tbl = db.GetTables(name='test')[0]
        
        for record in tbl.GetRecords(1, 1000):
            record.Delete()

        for weight in weightList:
            record = {u'日付': weight['date'], u'体重': weight['weight']}
            tbl.AddRecord(record)

#-------------------------------------------------------------------------------
if __name__ == '__main__':

    user = '<your google account>@gmail.com'
    passwd = '<your google password>'
    start = '2012-08-16'
    end   = '2013-08-16'

    weightList = GoogleCalendar(user, passwd).GetWeightList(start, end)
    GoogleSpreadsheet(user, passwd).UpdateRecords(weightList)

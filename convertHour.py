import re
import csv
import sys
import random
from datetime import datetime, timedelta


class HourConverter():
    def dateConverter(self, date):
        hour =  date.split(":")[0]
        minute = date.split(":")[1]
        minute = minute.split(" ")[0]
        day = date.split(" ")[2]
        month = self.monthConverter(date.split(" ")[3])
        year = date.split(" ")[4]
        newdate = datetime(int(year), int(month), int(day), int(hour), int(minute))
        return newdate

    def monthConverter(self, month):
        if month == 'janv.':
            return 1
        if month == 'févr.':
            return 2
        if month == 'mars':
            return 3
        if month == 'avri.':
            return 4
        if month == 'mai':
            return 5
        if month == 'juin':
            return 6
        if month == 'juil.':
            return 7
        if month == 'août':
            return 8
        if month == 'sept.':
            return 9
        if month == 'octb.':
            return 10
        if month == 'nove.':
            return 11
        if month == 'dece.':
            return 12
        return 0

    def reverseMonthConverter(self, month):
        if month == 1:
            return "janv."
        if month == 2:
            return 'févr.'
        if month == 3:
            return 'mars'
        if month == 4:
            return 'avri.'
        if month == 5:
            return 'mai'
        if month == 6:
            return 'juin'
        if month == 7:
            return 'juil.'
        if month == 8:
            return 'août'
        if month == 9:
            return 'sept.'
        if month == 10:
            return 'octb.'
        if month == 11:
            return 'nove.'
        if month == 12:
            return 'dece.'

    def add7h(self, date):
        sevenmorehour = date + timedelta(hours=7)
        return sevenmorehour
    
    def unConvert(self, date):
        strdate=str(date)
        print(strdate)
        dat = strdate.split(" ")[0]
        year = dat.split("-")[0]
        month = dat.split("-")[1]
        month = self.reverseMonthConverter(int(month))
        day = dat.split("-")[2]
        hours = strdate.split(" ")[1]
        hour = hours.split(":")[0]
        minute = hours.split(":")[1]
        turbodate = hour + ":" + minute + " - " + day + " " + month + " " + year
        return turbodate

    def convert7(self, data):
        csv100 = open('resUpdate7.csv', 'w', encoding="utf-8")
        for row in data:
            date = row.split(",")[1]
            newdate = self.dateConverter(date)
            date7 = self.add7h(newdate)
            date = self.unConvert(date7)
            texte = row.split(",")[2]
            user = row.split(",")[0]
            csv100.write("{},{},{},\n".format(user, date, texte))
        return 0

fichier = "resCarambarApres.csv"
f = open(fichier, 'rt', encoding='utf-8')
c = HourConverter()
thisdate = datetime(int(2013), int(3), int(31), int(22), int(30))
c.convert7(f)

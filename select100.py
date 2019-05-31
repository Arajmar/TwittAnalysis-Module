import re
import csv
import sys
import random
import datetime

class Selecter():
    def count(self, data):
        nb=0
        for row in data:
            nb += 1
        print(nb)
        return nb

    def select100(self, X):
        tab = []
        for i in range(0,100):
            tab.append(random.randint(1,X)) 
        tab.sort()
        return tab
    
    def write100(self, rTab, data):
        csv100 = open('echantillon100rand.csv', 'w', encoding="utf-8")
        nb=0
        for row in data:
            if (nb in rTab):
                texte = row.split(",")[2]
                user = row.split(",")[0]
                csv100.write("{},{},\n".format(user, texte))
            nb +=1
        return 0
    
    def compareDate(self, data, datelim):
        csv100 = open('echantillon100.csv', 'w', encoding="utf-8")
        nb = 0
        for row in data:
            date = row.split(",")[1]
            newdate = self.dateConverter(date)
            if newdate < datelim and nb < 100 and newdate < datetime.datetime(2018,3,21,17,25):
                nb += 1
                texte = row.split(",")[2]
                date = row.split(",")[1]
                user = row.split(",")[0]
                csv100.write("{},{},{},\n".format(user, date, texte))
        return 0
    
    def dateConverter(self, date):
        hour =  date.split(":")[0]
        minute = date.split(":")[1]
        minute = minute.split(" ")[0]
        day = date.split(" ")[2]
        month = self.monthConverter(date.split(" ")[3])
        year = date.split(" ")[4]
        newdate = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
        return newdate

    def inputDateConverter(self, date, heure):
        hour =  heure.split(":")[0]
        minute =  heure.split(":")[1]
        day =  date.split("/")[0]
        month =  date.split("/")[1]
        year =  date.split("/")[2]
        newdate = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
        print(newdate)
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

fichier = "resCarambarApres.csv"


print(sys.argv[1])
f = open(fichier, 'rt', encoding='utf-8')
s = Selecter()
dat = s.inputDateConverter(sys.argv[1], sys.argv[2])
nb = s.count(data = f)
tb = s.select100(X = nb)
f2 = open(fichier, 'rt', encoding='utf-8')
s.write100(rTab = tb, data = f2)
f3 = open(fichier, 'rt', encoding='utf-8')
#dat = newdate = datetime.datetime(2015,1,16,3,1)
s.compareDate(f3,dat)
import csv

class UAT:
    voturi=0
    peliste=0

def getsiruta (siruta, nume):
    di = {
        'BUCUREŞTI SECTORUL 1' : '179141',
        'BUCUREŞTI SECTORUL 2' : '179150',
        'BUCUREŞTI SECTORUL 3' : '179169',
        'BUCUREŞTI SECTORUL 4' : '179178',
        'BUCUREŞTI SECTORUL 5' : '179187',
        'BUCUREŞTI SECTORUL 6' : '179196',
    }
    if siruta!='179132':
        return siruta
    else:
        return di.get(nume)

rez={}
with open('/home/alex/rw.csv','w',encoding='utf8') as outputfile, \
     open('/home/alex/Downloads/presence_2020-12-06_23-00.csv','r',encoding='utf8') as csvfile:
    csvdata = csv.DictReader(csvfile)
    csvwriter = csv.writer(outputfile)
    for row in csvdata:
        siruta = getsiruta(row['Siruta'],row['UAT'])
        if not rez.get(siruta):
            rez.update({siruta:UAT()})
        rez[siruta].peliste += int(row['Votanti pe lista permanenta'])
        rez[siruta].voturi += int(row['LT'])
    for loc in rez:
        csvwriter.writerow([loc,str(round(rez[loc].voturi*100/rez[loc].peliste,2))])

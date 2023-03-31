import csv
import sys
import pickle

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
with open('/home/alex/rw.p','wb') as outputfile, \
     open('/home/alex/Downloads/pv_final_cnty_s_'+str(sys.argv[1])+'.csv','r',encoding='utf8') as csvfile:
    csvdata = csv.DictReader(csvfile)
    csvwriter = csv.writer(outputfile)
    for row in csvdata:
        siruta = getsiruta(row['uat_siruta'],row['uat_name'])
        if not rez.get(siruta):
            rez.update({siruta:{}})
        for key, value in row.items():
            if "-voturi" in key:
                if not key in rez[siruta]:
                    rez[siruta].update({key:0})
                rez[siruta].update({key:rez[siruta].get(key)+int(value)})
    pickle.dump(rez, outputfile)
    """
    for loc, uat in rez.items():
        print(loc)
        print(rez[loc])
        totalvoturi = 0
        maximvoturi = 0
        maximnume = "Egalitate"
        for key, value in rez[loc].items():
            totalvoturi += value
            if value == maximvoturi:
                maximnume = "Egalitate"
            if value > maximvoturi:
                maximvoturi = value
                maximnume = key
        csvwriter.writerow([loc,maximnume,str(round(maximvoturi*100/totalvoturi,2))])
"""
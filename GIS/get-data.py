import csv

def sirc (pa):
    di = {
        'BUCUREŞTI SECTORUL 1' : '179141',
        'BUCUREŞTI SECTORUL 2' : '179150',
        'BUCUREŞTI SECTORUL 3' : '179169',
        'BUCUREŞTI SECTORUL 4' : '179178',
        'BUCUREŞTI SECTORUL 5' : '179187',
        'BUCUREŞTI SECTORUL 6' : '179196',
    }
    return di.get(pa)
def nan (si,r1,r3):
    if r3 == '179132':
        return (si!=sirc(r1))
    else:
        return (si!=r3)
candidati = ['Egalitate','Klaus Iohannis','Viorica Dăncilă','Cătălin Ivan','Ninel Peia','Sebastian Popescu','John-Ion Banu','Mircea Diaconu','Bogdan Stanoevici','Ramona Bruynseels','Viorel Cataramă','Alexandru Cumpănașu']
voturi = [0] * 15
tvoturi = 0
tprez = 0
maxp = 0
siruta = "102543"
outputfile = open('/home/alex/rw.csv' ,'w', encoding='utf8')
csvfile = open('/home/alex/Downloads/presence_now.csv', 'r', encoding='utf8')
reader = csv.reader(csvfile)
for row in reader:
    if row[1]=='UAT':
        continue
    if nan(siruta,row[1],row[3]):
        outputfile.write('\"' + siruta + '\",\"' + str(round(tvoturi*100/tprez,2)) + '\"\n')
        if row[3] == '179132':
            siruta = sirc(row[1])
        else:
            siruta = row[3]
        tvoturi = 0
        tprez = 0
    tvoturi = tvoturi + int(row[13])
    tprez = tprez + int(row[7])
outputfile.write('\"' + siruta + '\",\"' + str(round(tvoturi*100/tprez,2)) + '\"\n')
csvfile.close()
outputfile.close()

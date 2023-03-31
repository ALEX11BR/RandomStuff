import csv

def charp (ch):
    return ch.replace('MUNICIPIUL ','').replace('ORAŞ ','').replace('Ş','ș').replace('Ţ','ț').lower()

name = input("Nume candidat: ")
outputfile = open('D:\\Lucru\\Grafic\\'+ name + '.txt', 'w', encoding='utf8')
csvfile = open('D:\\Lucru\\Grafic\\res.txt', 'r', encoding='utf8')
reader = csv.reader(csvfile)
i = 0
for row in reader:
    if row[1]==name:
        outputfile.write('\"natcode\" = \'' + row[0] + '\' OR \n')
        i = i + 1
        print(row[2])
    if (i>29):
        outputfile.write (str(0) + '\n')
        i=0
outputfile.write (str(0))
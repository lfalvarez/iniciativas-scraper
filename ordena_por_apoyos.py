import csv

reader = csv.reader(open("file.csv"), delimiter=",")

cabeceras = next(reader)
lista_ordenada = sorted(reader, key=lambda row: int(row[1]), reverse=True)
#print(sortedlist)

f = open('ordenadas.csv', 'w')

writer = csv.writer(f)
writer.writerow(cabeceras)
writer.writerows(lista_ordenada)
f.close()

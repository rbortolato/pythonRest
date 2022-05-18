import csv
from myApp.database import execute

def read():
    with open('movielist.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for row in csv_reader:
            if not row['winner']:
                continue

            #Aqui eu vou inserir separado os produtores, teve filme com mais de um produtor, entao tive que quebrar por virgula e por and
            produtorListV = row['producers'].split(',')
            produtorListA = produtorListV[len(produtorListV)-1].split(' and ')
            produtorList = produtorListV[:len(produtorListV)-1] + produtorListA

            for produtor in produtorList:
                if not produtor: #Na lista tem alguns casos que estavam com ", and", gerando um registro vazio
                    continue

                query = "insert into premiacao values ('%s', %s)" % (produtor.strip(), row['year'])
                execute(query)
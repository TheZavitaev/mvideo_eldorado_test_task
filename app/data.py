import csv


def update_recomendations():
    global RECOMENDATIONS
    recommends = read_recomendations()
    if recommends:
        RECOMENDATIONS = recommends


def read_recomendations():
    print('try to load data...')
    try:
        with open('data/recommends.csv', mode='r') as infile:
            reader = csv.reader(infile, delimiter=',')
            recommends = {}
            for row in reader:
                if row[0] in recommends.keys():
                    recommends[row[0]][row[2]] = row[1]
                else:
                    recommends[row[0]] = {row[2]: row[1]}
            return recommends
    except IOError:
        print('failed to load data')
        return None

import csv

def getAward(row):
    if row[0] == '':
        award = None
    else:
        award = row[0]
    return award

def getCounrty(row):
    if row[1] == '':
        country = None
    else:
        country = row[1]
    return country

def getYear(row):
    if row[14] == '':
        year = None
    else:
        year = int(row[14])
    return year

def getDirector(row):
    if row[3] == '':
        director = None
    else:
        director = row[3]
    return director


try:
    with open("Movie_Movies.csv", encoding="utf-8", mode='r') as file:
        file.readline()
        reader = csv.reader(file)
        dataset = {}
        line_number = 0
        for row in reader:
            line_number += 1
            if line_number > 100:
                break

            award = getAward(row)
            country = getCounrty(row)
            year = getYear(row)
            director = getDirector(row)

            if year not in dataset:
                dataset[year] = {country:{director:{"award": award}}}
                if country not in dataset[year]:
                    dataset[year][country] = {director:{"award": award}}
                    if director not in dataset[year][country]:
                        dataset[year][country][director] = {"award": award}
                    else:
                       dataset[year][country][director].update({"award": award})
                else:
                    dataset[year][country].update({director:{"award": award}})
            else:
                dataset[year].update({country:{director:{"award": award}}})
        print(dataset)


except IOError as e:
   print ("I/O error({0}): {1}".format(e.errno, e.strerror))

except ValueError as ve:
    print("Value error {0} in line {1}".format(ve, line_number))

"""
GRAPHS
"""

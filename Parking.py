class Parking:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    #Fonction pour trouver la distance la plus courte, retourne les donnees du stationnement
    def findParking(self):

        # valeur qui va se faire modifier chaque fois qu"une nouvelle distance plus courte est trouvee
        distanceMin = 1000000.0

        with open("infoneigelistedesstationnementsgratuits20152016.csv", "r") as csvfile:
            reader = csv.reader(csvfile, delimiter = ",", quotechar = '"')
            csvfile.readline()
            # boucle qui compare chaque nouvelle distance a la plus courte
            # la distance la plus courte trouvee retourne les donnees du stationnement a la fin
            for column in reader:
                lon2 = float(column[6].replace(",", "."))
                lat2 = float(column[7].replace(",", "."))
                #print(lon2, lat2, "\n")
                longitude, latitude, lon2, lat2 = map(radians, [self.longitude, self.latitude, lon2, lat2])

                # haversine formula (calcul de la distance)
                dlon = lon2 - longitude
                dlat = lat2 - latitude
                a = sin(dlat / 2) ** 2 + cos(latitude) * cos(lat2) * sin(dlon / 2) ** 2
                c = 2 * asin(sqrt(a))
                km = 6367 * c

                # compare si la distance est plus courte
                if km < distanceMin:
                    distanceMin = km
                    destination = [column[0], column[1], column[2], column[3], column[4], column[5], column[6],
                                        column[7], column[8]]
                    #print("Shortest distance :", distanceMin, "at parking #", column[0])

                #print("Current distance :", km)
        return destination

from math import radians, cos, sin, asin, sqrt
import csv


# parking1 = Parking(0.0, 0.0)
# print("Le parking le plus proche est : ", parking1.findParking())

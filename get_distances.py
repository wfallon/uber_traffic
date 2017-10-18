import googlemaps
import csv
import time

origin_loc = "Harborwalk, Waterfront, Boston"

def write(data):
    with open('boston_rush_hour_distances.csv', 'wb') as f:
        writer = csv.writer(f)
        for val in data:
            writer.writerow([val])

def read_destinations():
    with open('Travel_Times_Boston_Rush_Hour.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        count = 0
        data = []
        for row in spamreader:
            if(count==0):
                count = count + 1
            else:
                data.append(row[3])
                count = count + 1
        return data


def calculate_distance():
    data = read_destinations()
    data1 = []
    gmaps = googlemaps.Client(key='AIzaSyCQAtP5CPgnZcG2g5a20PrboA91JRfF2Rg')
    count = 0
    count1 = 0
    for val in data:
        count = count + 1
        count1 = count1 + 1
        if((count%20)==0):
            #print("Sleeping for 10 seconds")
            #time.sleep(10)
            count = count + 1
        print(count1)
        print(val)
        my_distance = gmaps.distance_matrix(origin_loc , val)
        
        data1.append(my_distance["rows"][0]["elements"][0]["distance"]["value"])

    return data1

write(calculate_distance())



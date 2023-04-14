from gmplot import gmplot
import csv

gmap=gmplot.GoogleMapPlotter(28.6891,77.32456,17)
gmap.coloricon="https://www.googlemapsmakers.com/v1/%s/"

with open('route.csv',"r") as f:
    reader=csv.reader(f)
    k=0

    for row in reader:
        lat=float(row[0])
        long=float(row[1])

        if(k==0):
            gmap.marker(lat,long,"yellow")
            k=1
        else:
            gmap.marker(lat,long,"blue")

gmap.marker(lat,long,'red')
gmap.draw("mymap.html")


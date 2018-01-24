import gmplot, pymysql

gmap = gmplot.GoogleMapPlotter(28.594257, -81.2224, 16)
db = pymysql.connect("localhost", "root", "pass", "iot")
cursor = db.cursor()
cursor.execute("SELECT timestamp, latitude, longitude FROM data")
res = sorted(cursor.fetchall(), key=lambda x: x[0])
latitude, longitude = [], []
for row in res:
    latitude.append(row[1])
    longitude.append(row[2])
#print(latitude, longitude)
gmap.heatmap(latitude[:-1], longitude[:-1])
gmap.marker(latitude[-1], longitude[-1])
gmap.draw("map.html")

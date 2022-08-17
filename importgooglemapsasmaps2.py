import googlemaps as gmaps 
import datetime
import os

SRC = input("Enter the source address :  ")
DEST = input("Enter destination address :  ")
CLIENT_KEY = os.getenv('AIzaSyDTcsfKiuU8p0sOg4PZQyPAyXFH6__agus')  # Set your directions api key as an env variable
gmaps_client = gmaps.Client(key='AIzaSyDTcsfKiuU8p0sOg4PZQyPAyXFH6__agus')

now = datetime.datetime.now()
directions = gmaps_client.directions(SRC, DEST, mode="driving",departure_time=now)

# debug
# print(directions)

directions = directions[0].get('legs')[0].get('duration_in_traffic').get('text')
print(directions)

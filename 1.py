# command to run this programme
# python 1-1.py

# for making JSON objects
import json

# for downloading the data from the web
import urllib.request

# for connecting to the database
import psycopg2

# Connect to the database
# Change the connection string accordingly (e.g. username, password, database name)
connection = psycopg2.connect(
    database="soundarya", user='postgres', password='Chanti143$', host='127.0.0.1', port='5432'
)

# Create a cursor to perform database operations
cursor = connection.cursor()

# Create a table in the database (if it does not exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS UFO (
id TEXT PRIMARY KEY NOT NULL, datetime TEXT, city TEXT, state TEXT, country TEXT, shape TEXT,
duration_sec TEXT, duration_hrs_min TEXT, comments TEXT, date_posted TEXT, latitude NUMERIC, longitude NUMERIC
)
''')

# Commit the changes to the database
connection.commit()

# Establish a connection to the data source and read the data
response = urllib.request.urlopen(
    "https://cs.msutexas.edu/~griffin/data/UfoData/ufos_export.json")

# Loop counter
counter = 0

while (True):
    # Read a single line from the data source
    json_data = response.readline()

    # If the line is empty, the end of the file has been reached
    # Break out of the loop
    if json_data == b'':
        break

    # convert the line to a JSON object
    json_data = json.loads(json_data.decode("utf-8"))

    # Check if the id is already present in the database
    cursor.execute("SELECT id FROM UFO WHERE id = %s",
                   (json_data['_id']['$oid'],))

    # If the id is not present in the database, insert the json_data
    if (cursor.fetchone() == None):
        counter = counter + 1
        print(str(counter) + " => Inserting json_data : " +
              json_data['_id']['$oid'])

        try:
            if (float(json_data['latitude'])):
                # Insert into database
                cursor.execute("INSERT INTO UFO ( id, datetime, city, state, country, shape, duration_sec, duration_hrs_min, comments, date_posted, latitude, longitude ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    json_data['_id']['$oid'], json_data['datetime'], json_data['city'], json_data['state'], json_data['country'], json_data['shape'], json_data['duration (seconds)'], json_data['duration (hours/min)'], json_data['comments'], json_data['date posted'], json_data['latitude'], json_data['longitude']))

                # Commit the changes to the database
                connection.commit()
        except:
            # If the latitude is not a number, ignore the record
            pass


# Close the connection to the database
connection.close()

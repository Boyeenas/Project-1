# for connect to the database
import json
import psycopg2

# for generating API in python
from fastapi import FastAPI
app = FastAPI()

# Connect to the database
# Change the connection string accordingly (e.g. username, password, database name)
connection = psycopg2.connect(
    database="soundarya", user='postgres', password='Chanti143$', host='127.0.0.1', port='5432'
)

# Create a cursor to perform database operations
cursor = connection.cursor()


@app.get("/findAll")
# to get all the data from the database
def findAll():
    all_data = cursor.execute("SELECT * FROM UFO")
    all_data = cursor.fetchall()
    return all_data


@app.get("/findOne")
# to find a particular data from the database (based on column key-value)
def findOne(id=None, city=None, state=None, country=None):

    if id is not None:
        get_data = cursor.execute("SELECT * FROM UFO WHERE id = %s", (id,))
        get_data = cursor.fetchone()

        json_data = {
            "id": get_data[0],
            "datetime": get_data[1],
            "city": get_data[2],
            "state": get_data[3],
            "country": get_data[4],
            "shape": get_data[5],
            "duration (seconds)": get_data[6],
            "duration (hours/min)": get_data[7],
            "comments": get_data[8],
            "date posted": get_data[9],
            "latitude": get_data[10],
            "longitude": get_data[11]
        }

        return json_data

    elif city is not None:
        get_data = cursor.execute("SELECT * FROM UFO WHERE city = %s", (city,))
        get_data = cursor.fetchone()

        json_data = {
            "id": get_data[0],
            "datetime": get_data[1],
            "city": get_data[2],
            "state": get_data[3],
            "country": get_data[4],
            "shape": get_data[5],
            "duration (seconds)": get_data[6],
            "duration (hours/min)": get_data[7],
            "comments": get_data[8],
            "date posted": get_data[9],
            "latitude": get_data[10],
            "longitude": get_data[11]
        }

        return json_data

    elif state is not None:
        get_data = cursor.execute(
            "SELECT * FROM UFO WHERE state = %s", (state,))
        get_data = cursor.fetchone()

        json_data = {
            "id": get_data[0],
            "datetime": get_data[1],
            "city": get_data[2],
            "state": get_data[3],
            "country": get_data[4],
            "shape": get_data[5],
            "duration (seconds)": get_data[6],
            "duration (hours/min)": get_data[7],
            "comments": get_data[8],
            "date posted": get_data[9],
            "latitude": get_data[10],
            "longitude": get_data[11]
        }

        return json_data

    elif country is not None:
        get_data = cursor.execute(
            "SELECT * FROM UFO WHERE country = %s", (country,))
        get_data = cursor.fetchone()

        json_data = {
            "id": get_data[0],
            "datetime": get_data[1],
            "city": get_data[2],
            "state": get_data[3],
            "country": get_data[4],
            "shape": get_data[5],
            "duration (seconds)": get_data[6],
            "duration (hours/min)": get_data[7],
            "comments": get_data[8],
            "date posted": get_data[9],
            "latitude": get_data[10],
            "longitude": get_data[11]
        }

        return json_data

    else:
        return "Invalid parameter"


@app.get("/findClosest")
# to find the closest data from the database (based on latitude and longitude)
def findClosest(lat=None, lon=None):
    if lat is not None and lon is not None:
        get_data = cursor.execute(
            "SELECT * FROM UFO ORDER BY (latitude - %s)^2 + (longitude - %s)^2 LIMIT 1", (lat, lon))
        get_data = cursor.fetchone()

        json_data = {
            "id": get_data[0],
            "datetime": get_data[1],
            "city": get_data[2],
            "state": get_data[3],
            "country": get_data[4],
            "shape": get_data[5],
            "duration (seconds)": get_data[6],
            "duration (hours/min)": get_data[7],
            "comments": get_data[8],
            "date posted": get_data[9],
            "latitude": get_data[10],
            "longitude": get_data[11]
        }

        return json_data
    else:
        return "Invalid parameter"

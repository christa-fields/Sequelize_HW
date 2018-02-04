import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify



#################################################
# Database Setup
#################################################

# Create the database connection engine
engine = create_engine("sqlite:///hawaii.sqlite") 

Base = automap_base() # Declare a Base using `automap_base()`
Base.prepare(engine,reflect=True)

conn = engine.connect()
Base.metadata.create_all(conn)

Base.classes.keys() # Print all of the classes mapped to the Base
measurements= Base.classes.measurements
stations= Base.classes.stations

# Create a session
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# Define what to do when a user hits the index route
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/"
    )

# /api/v1.0/precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
   
   # Return precipitation#
    
    # Query
    measurements = session.query(measurements).all()

    # Create a dictionary
    measurements = []
    for measure in measurments:
        measurement_dict = {}
        measurement_dict["date"] = measurements.date
        measurement_dict["temp"] = measurements.tobs
        measurements.append(measurement_dict)

    return jsonify(measurements)


# /api/v1.0/stations
@app.route("/api/v1.0/stations")
def precipitation():
 
    # Query
    stations = session.query(measurements.station).all()
    
    # Convert list of tuples into normal list
    stations_dict = list(np.ravel(stations))

    return jsonify(stations_dict)


#/api/v1.0/tobs
@app.route("/api/v1.0/tobs")

minimum = session.query(measurements.tobs).\
    filter(measurement.date >= start_date).all()
# Convert list of tuples into normal list
minimum_dict = list(np.ravel((minimum)))

    return jsonify(minimum_dict)



#/api/v1.0/ 
@app.route("/api/v1.0/")


minimum = session.query(func.min(measurements.tobs)).\
    filter(measurement.date >= start_date).all()
# Convert list of tuples into normal list
minimum_dict = list(np.ravel((minimum)))

    return jsonify(minimum_dict)


maximum = session.query(func.max(measurements.tobs)).\
    filter(measurement.date >= start_date).all()
# Convert list of tuples into normal list
maximum_dict = list(np.ravel((maximum)))

    return jsonify(maximum_dict)


average = session.query(func.avg(measurements.tobs)).\
    filter(measurement.date >= start_date).all()
# Convert list of tuples into normal list
maximum_dict = list(np.ravel((average)))

    return jsonify(average)


#/api/v1.0//
@app.route("/api/v1.0//")

start_date='2014/01/01'
end_date='2014/12/01'

minimum = session.query(func.min(measurements.tobs)).\
    filter(measurement.date between start_date and end_date).all()
# Convert list of tuples into normal list
minimum_dict = list(np.ravel((minimum)))

    return jsonify(minimum_dict)


maximum = session.query(func.max(measurements.tobs)).\
    filter(measurement.date between start_date and end_date).all()
# Convert list of tuples into normal list
maximum_dict = list(np.ravel((maximum)))

    return jsonify(maximum_dict)


average = session.query(func.avg(measurements.tobs)).\
    filter(measurement.date between start_date and end_date).all()
# Convert list of tuples into normal list
maximum_dict = list(np.ravel((average)))

    return jsonify(average)

app.run(debug=True)
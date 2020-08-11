##########################################
# # Flask Application
##########################################
# Dependencies and Setup
import os
from os import environ

import pandas as pd
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

##########################################
# Database Connection Set up
##########################################
# Setup SQLAlchemy with flask
# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL', '')
# # Create database and pass in the app 
# db = SQLAlchemy(app)

# # Create engine
# conn_str = "postgres://rilcwxqbdcttnx:6fbe02be55d33cf132b076fcec9f961162a0eb3ffc67aff912d8aedeabfcfe5e@ec2-34-237-89-96.compute-1.amazonaws.com:5432/d3c3p19kp6bchj"
# engine = create_engine(conn_str)

# # Reflect the database 
# Base = automap_base()

# Reflect the tables into SQLAlchemy classes
# Base.prepare(engine, reflect=True)
# allclasses = Base.classes.keys()

##########################################
# Flask Set up
##########################################
app = Flask(__name__)

###################################################################
# SET FLASK ROUTES
###################################################################
######################################################
# Render the Index HTML on the main route
######################################################
@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

#######################################################
# Render the database table 1 BDR
#######################################################
# @app.route("/nc1bdr")
# def nc1bdr():
#     """Query the database for 1 BDR houses"""

#     # Save references to each table in database 
#     Propertytypes = Base.classes.propertytypes

#     # Create session
#     session = Session(bind=engine)
    
#     # Query the table for columns of interest
#     propertytypes = session.query(Propertytypes).all()
    
#     # Create an empty list
#     property_types = []
    
#     # Loop through each row and create dictionaries for each column   
#     for listing in propertytypes:
#         ptypes_dict = {
#             "propertytype": listing.propertytype,
#             "listings": listing.listings
#             # "percent": listing.percent
#             }
        
#         # Append all columns to the object
#         property_types.append(ptypes_dict)
    
#     session.close()
#     # Return the json
#     return jsonify(property_types)

#######################################################
# Render the Dashboard HTML 
#######################################################
@app.route("/dashboard")
def dashboard():
    """Return the Dashboard page."""
    return render_template("rw_dashboard.html")

#######################################################
# Render the Analysis Methodology HTML
#######################################################
@app.route("/methodology")
def methodology():
    """Return the Methodology page."""
    return render_template("rw_methodology.html")

########################################################
# Render the Acknowledgements HTML 
#######################################################
@app.route("/acknowledgements")
def acknowledgements():
    """Return the acknowledgements page."""
    return render_template("rw_acknowledgements.html")

########################################################
# Render the Exploratory Analysis HTML 
#######################################################
@app.route("/analysis")
def analysis():
    """Return the exploratory analysis page."""
    return render_template("rw_analysis.html")

########################################################
# Render the 1 BDR price prediction HTML 
#######################################################
@app.route("/prediction1bdr")
def prediction1bdr():
    """Return the 1 BDR price prediction page."""
    return render_template("rw_prediction1bdr.html")

########################################################
# Render the 2 BDR price prediction HTML 
#######################################################
@app.route("/prediction2bdr")
def prediction2bdr():
    """Return the 2 BDR price prediction page."""
    return render_template("rw_prediction2bdr.html")

########################################################
# Render the 3 BDR price prediction HTML 
#######################################################
@app.route("/prediction3bdr")
def prediction3bdr():
    """Return the 3 BDR price prediction page."""
    return render_template("rw_prediction3bdr.html")

########################################################
# Render the 4 BDR price prediction HTML 
#######################################################
@app.route("/prediction4bdr")
def prediction4bdr():
    """Return the 4 BDR price prediction page."""
    return render_template("rw_prediction4bdr.html")

###################################################################
# Code to actually run the app
###################################################################
if __name__ == "__main__":
    app.run(debug = True)
##################### END OF APP #############################################
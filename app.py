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
    """Return the analysis page."""
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
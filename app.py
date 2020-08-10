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
# Render the change over time plot HTML 
#######################################################
@app.route("/growth")
def growth():
    """Return the growth page."""
    return render_template("rw_growth.html")

########################################################
# Render the pricemap HTML 
#######################################################
@app.route("/pricemap")
def pricemap():
    """Return the pricemap page."""
    return render_template("rw_pricemap.html")

########################################################
# Render the prediction HTML 
#######################################################
@app.route("/prediction")
def prediction():
    """Return the prediction page."""
    return render_template("rw_prediction.html")
#############################################################################################
# Rashi's additional routes
############################################################################################

###################################################################
# Code to actually run the app
###################################################################
if __name__ == "__main__":
    app.run(debug = True)
##################### END OF APP #############################################
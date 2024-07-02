from flask import Blueprint, render_template
import psycopg2

view = Blueprint('view', __name__)

DB_NAME = "stgbcdb81d2a7f6"
DB_USER = "usr308e594d3db4f80e"
DB_PASS = "de591a649e24bba5a421ba0063ee4bd2"
DB_HOST = "pg-99bcde18-2a38-481f-8125-ad8d06aa1cbe.schematogo.us-east-1.antimony.io"
DB_PORT = "20478"

@view.route("/")
def home():
  return render_template("home.html")

@view.route("/sec1")
def sec1():
  return render_template("sec1.html")

@view.route("/sec2")
def sec2():
  return render_template("sec2.html")


from flask import Blueprint, redirect, render_template, request, url_for
import psycopg2

view = Blueprint('view', __name__)

DB_NAME = "stgbcdb81d2a7f6"
DB_USER = "usr308e594d3db4f80e"
DB_PASS = "de591a649e24bba5a421ba0063ee4bd2"
DB_HOST = "pg-99bcde18-2a38-481f-8125-ad8d06aa1cbe.schematogo.us-east-1.antimony.io"
DB_PORT = "20478"

@view.route("/")
def index():
  return render_template("index.html")
  
@view.route("/home")
def home():
  return render_template("home.html")

@view.route("/auth", methods=['GET','POST'])
def auth():
  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")
    
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM users"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()

    user_found = False
    authorized = False
    for row in data:
      
      if username == row[0]:
        user_found = True
        if password == row[1]:
          authorized = True
        break

    if user_found:
      if not authorized:
        pass
      else:
        return redirect(url_for("view.home"))
    else:
      pass
  
  return render_template("auth.html")

@view.route("/sec1")
def sec1():
  return render_template("sec1.html")

@view.route("/sec2")
def sec2():
  return render_template("sec2.html")


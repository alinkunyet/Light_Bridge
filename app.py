from flask import Flask, jsonify, render_template, jsonify
import psycopg2

app = Flask(__name__)

DB_NAME = "stgbcdb81d2a7f6"
DB_USER = "usr308e594d3db4f80e"
DB_PASS = "de591a649e24bba5a421ba0063ee4bd2"
DB_HOST = "pg-99bcde18-2a38-481f-8125-ad8d06aa1cbe.schematogo.us-east-1.antimony.io"
DB_PORT = "20478"


@app.route("/home")
def home():
  data = None
  
  try:
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()

    sql = "SELECT * FROM users"
    cur.execute(sql)
    data = cur.fetchall()

    cur.close()
    conn.close()
  except Exception as e:
    print(e)
    
  return render_template("index.html", users = data, title = "Users")

@app.route("/")
def sec1computing():
  data = None

  try:
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()

    sql = "SELECT * FROM sec1computing"
    cur.execute(sql)
    data = cur.fetchall()

    cur.close()
    conn.close()
  except Exception as e:
    print(e)

  return render_template("sec1computing.html", notes = data, title = "Secondary 1 - Computing")

@app.route("/class")
def secclass():
  data = None

  try:
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()

    sql = "SELECT * FROM sec1computing"
    cur.execute(sql)
    data = cur.fetchall()

    cur.close()
    conn.close()
  except Exception as e:
    print(e)

  return jsonify(data)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)
from flask import Blueprint, redirect, render_template, request, url_for
import psycopg2

sec1view = Blueprint('sec1view', __name__)

DB_NAME = "stgbcdb81d2a7f6"
DB_USER = "usr308e594d3db4f80e"
DB_PASS = "de591a649e24bba5a421ba0063ee4bd2"
DB_HOST = "pg-99bcde18-2a38-481f-8125-ad8d06aa1cbe.schematogo.us-east-1.antimony.io"
DB_PORT = "20478"


@sec1view.route("/", methods=['GET', 'POST'])
@sec1view.route("/sec1computing", methods=['GET', 'POST'])
def sec1computing():

  if request.method == 'POST':

    classNum = request.form.get("classNum")

    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec1computing ORDER BY classno"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()

    numbers = []
    for row in data:
      numbers.append(str(row[0]))

    if request.form['button'] == 'add':
      if classNum in numbers or classNum == "":
        pass  #class already exist
      else:
        return redirect(url_for("sec1view.sec1computingInsert", classNum=classNum))

    if request.form['button'] == 'update':
      if classNum in numbers:
        return redirect(url_for("sec1view.sec1computingUpdate", classNum=classNum))
      else:
        pass  #class does not exist

    return render_template("sec1computing.html", data=data)

  else:

    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec1computing ORDER BY classno DESC"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("sec1computing.html",
                           notes=data,
                           title="Secondary 1 - Computing")


#update page
@sec1view.route("/sec1computingUpdate", methods=['GET', 'POST'])
def sec1computingUpdate():
  if request.method == "POST":
    try:
      conn = psycopg2.connect(database=DB_NAME,
                              user=DB_USER,
                              password=DB_PASS,
                              host=DB_HOST,
                              port=DB_PORT)
      cur = conn.cursor()

      classNo = request.form.get("num")
      date = request.form.get("date")
      topic = request.form.get("topic")
      objectives = request.form.get("objectives")
      method = request.form.get("method")
      teacher = request.form.get("teacher")
      student = request.form.get("student")

      sql = "UPDATE sec1computing SET date = %s, topic = %s, objectives = %s, method = %s, teacheractivity = %s, studentactivity = %s WHERE classno = %s"
      val = (date, topic, objectives, method, teacher, student, classNo)
      cur.execute(sql, val)
      conn.commit()
      cur.close()
      conn.close()
    except Exception as e:
      print(e)

    return redirect(url_for("sec1view.sec1computing"))

  else:
    classNo = request.args.get('classNum')
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec1computing WHERE classno = " + str(classNo)
    cur.execute(sql)
    note = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("sec1computingUpdate.html",
                           note=note,
                           classNum=classNo,
                           title="Update")


@sec1view.route("/sec1computingInsert", methods=['GET', 'POST'])
def sec1computingInsert():
  classNum = request.form.get("classNum")

  if request.method == "POST":
    
    classNo = request.form.get("num")
    date = request.form.get("date")
    topic = request.form.get("topic")
    objectives = request.form.get("objectives")
    method = request.form.get("method")
    teacher = request.form.get("teacher")
    student = request.form.get("student")

    try:
      conn = psycopg2.connect(database=DB_NAME,
                              user=DB_USER,
                              password=DB_PASS,
                              host=DB_HOST,
                              port=DB_PORT)
      cur = conn.cursor()

      sql = "INSERT INTO sec1computing (classno, date, topic, objectives, method, teacheractivity, studentactivity) VALUES (%s, %s, %s, %s, %s, %s, %s)"
      val = (classNo, date, topic, objectives, method, teacher, student)

      cur.execute(sql, val)
      conn.commit()
      cur.close()
      conn.close()
    except Exception as e:
      print(e)

    return redirect(url_for("sec1view.sec1computing"))

  else:
    classNum = request.args.get('classNum')
    return render_template("sec1computingInsert.html", classNum=classNum)

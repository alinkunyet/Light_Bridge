from flask import Blueprint, redirect, render_template, request, url_for
import psycopg2

sec2view = Blueprint('sec2view', __name__)

DB_NAME = "stgbcdb81d2a7f6"
DB_USER = "usr308e594d3db4f80e"
DB_PASS = "de591a649e24bba5a421ba0063ee4bd2"
DB_HOST = "pg-99bcde18-2a38-481f-8125-ad8d06aa1cbe.schematogo.us-east-1.antimony.io"
DB_PORT = "20478"

#Secondary 2 Mathematics
@sec2view.route("/sec2maths", methods=['GET', 'POST'])
def sec2maths():

  if request.method == 'POST':

    classNum = request.form.get("classNum")

    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec2maths ORDER BY classno"
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
        return redirect(url_for("sec2view.sec2mathsInsert", classNum=classNum))

    if request.form['button'] == 'update':
      if classNum in numbers:
        return redirect(url_for("sec2view.sec2mathsUpdate", classNum=classNum))
      else:
        pass  #class does not exist

    return render_template("sec2maths.html", data=data)

  else:

    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec2maths ORDER BY classno DESC"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("sec2maths.html",
                           notes=data,
                           title="Secondary 2 - Mathematics")


#update page
@sec2view.route("/sec2mathsUpdate", methods=['GET', 'POST'])
def sec2mathsUpdate():
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

      sql = "UPDATE sec2maths SET date = %s, topic = %s, objectives = %s, method = %s, teacheractivity = %s, studentactivity = %s WHERE classno = %s"
      val = (date, topic, objectives, method, teacher, student, classNo)
      cur.execute(sql, val)
      conn.commit()
      cur.close()
      conn.close()
    except Exception as e:
      print(e)

    return redirect(url_for("sec2view.sec2maths"))

  else:
    classNo = request.args.get('classNum')
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec2maths WHERE classno = " + str(classNo)
    cur.execute(sql)
    note = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("sec2mathsUpdate.html",
                           note=note,
                           classNum=classNo,
                           title="Update")


@sec2view.route("/sec2mathsInsert", methods=['GET', 'POST'])
def sec2mathsInsert():
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

      sql = "INSERT INTO sec2maths (classno, date, topic, objectives, method, teacheractivity, studentactivity) VALUES (%s, %s, %s, %s, %s, %s, %s)"
      val = (classNo, date, topic, objectives, method, teacher, student)

      cur.execute(sql, val)
      conn.commit()
      cur.close()
      conn.close()
    except Exception as e:
      print(e)

    return redirect(url_for("sec2view.sec2maths"))

  else:
    classNum = request.args.get('classNum')
    return render_template("sec2mathsInsert.html", classNum=classNum)




##########################################################################

#Secondary 2 Science
@sec2view.route("/sec2science", methods=['GET', 'POST'])
def sec2science():

  if request.method == 'POST':

    classNum = request.form.get("classNum")

    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec2science ORDER BY classno"
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
        return redirect(url_for("sec2view.sec2scienceInsert", classNum=classNum))

    if request.form['button'] == 'update':
      if classNum in numbers:
        return redirect(url_for("sec2view.sec2scienceUpdate", classNum=classNum))
      else:
        pass  #class does not exist

    return render_template("sec2science.html", data=data)

  else:

    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec2science ORDER BY classno DESC"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("sec2science.html",
                           notes=data,
                           title="Secondary 2 - Science")


#update page
@sec2view.route("/sec2scienceUpdate", methods=['GET', 'POST'])
def sec2scienceUpdate():
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

      sql = "UPDATE sec2science SET date = %s, topic = %s, objectives = %s, method = %s, teacheractivity = %s, studentactivity = %s WHERE classno = %s"
      val = (date, topic, objectives, method, teacher, student, classNo)
      cur.execute(sql, val)
      conn.commit()
      cur.close()
      conn.close()
    except Exception as e:
      print(e)

    return redirect(url_for("sec2view.sec2science"))

  else:
    classNo = request.args.get('classNum')
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec2science WHERE classno = " + str(classNo)
    cur.execute(sql)
    note = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("sec2scienceUpdate.html",
                           note=note,
                           classNum=classNo,
                           title="Update")


@sec2view.route("/sec2scienceInsert", methods=['GET', 'POST'])
def sec2scienceInsert():
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

      sql = "INSERT INTO sec2science (classno, date, topic, objectives, method, teacheractivity, studentactivity) VALUES (%s, %s, %s, %s, %s, %s, %s)"
      val = (classNo, date, topic, objectives, method, teacher, student)

      cur.execute(sql, val)
      conn.commit()
      cur.close()
      conn.close()
    except Exception as e:
      print(e)

    return redirect(url_for("sec2view.sec2science"))

  else:
    classNum = request.args.get('classNum')
    return render_template("sec2scienceInsert.html", classNum=classNum)


#############################################################################

#Secondary 2 English
@sec2view.route("/sec2english", methods=['GET', 'POST'])
def sec2english():

  if request.method == 'POST':

    classNum = request.form.get("classNum")

    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec2english ORDER BY classno"
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
        return redirect(url_for("sec2view.sec2englishInsert", classNum=classNum))

    if request.form['button'] == 'update':
      if classNum in numbers:
        return redirect(url_for("sec2view.sec2englishUpdate", classNum=classNum))
      else:
        pass  #class does not exist

    return render_template("sec2english.html", data=data)

  else:

    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec2english ORDER BY classno DESC"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("sec2english.html",
                           notes=data,
                           title="Secondary 2 - English")


#update page
@sec2view.route("/sec2englishUpdate", methods=['GET', 'POST'])
def sec2englishUpdate():
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

      sql = "UPDATE sec2english SET date = %s, topic = %s, objectives = %s, method = %s, teacheractivity = %s, studentactivity = %s WHERE classno = %s"
      val = (date, topic, objectives, method, teacher, student, classNo)
      cur.execute(sql, val)
      conn.commit()
      cur.close()
      conn.close()
    except Exception as e:
      print(e)

    return redirect(url_for("sec2view.sec2english"))

  else:
    classNo = request.args.get('classNum')
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec2english WHERE classno = " + str(classNo)
    cur.execute(sql)
    note = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("sec2englishUpdate.html",
                           note=note,
                           classNum=classNo,
                           title="Update")


@sec2view.route("/sec2englishInsert", methods=['GET', 'POST'])
def sec2englishInsert():
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

      sql = "INSERT INTO sec2english (classno, date, topic, objectives, method, teacheractivity, studentactivity) VALUES (%s, %s, %s, %s, %s, %s, %s)"
      val = (classNo, date, topic, objectives, method, teacher, student)

      cur.execute(sql, val)
      conn.commit()
      cur.close()
      conn.close()
    except Exception as e:
      print(e)

    return redirect(url_for("sec21view.sec2english"))

  else:
    classNum = request.args.get('classNum')
    return render_template("sec2englishInsert.html", classNum=classNum)


#############################################################################


#Secondry 2 computing
@sec2view.route("/sec2computing", methods=['GET', 'POST'])
def sec2computing():

  if request.method == 'POST':

    classNum = request.form.get("classNum")

    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec2computing ORDER BY classno"
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
        return redirect(url_for("sec2view.sec2computingInsert", classNum=classNum))

    if request.form['button'] == 'update':
      if classNum in numbers:
        return redirect(url_for("sec2view.sec2computingUpdate", classNum=classNum))
      else:
        pass  #class does not exist

    return render_template("sec2computing.html", data=data)

  else:

    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec2computing ORDER BY classno DESC"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("sec2computing.html",
                           notes=data,
                           title="Secondary 2 - Computing")


#update page
@sec2view.route("/sec2computingUpdate", methods=['GET', 'POST'])
def sec2computingUpdate():
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

      sql = "UPDATE sec2computing SET date = %s, topic = %s, objectives = %s, method = %s, teacheractivity = %s, studentactivity = %s WHERE classno = %s"
      val = (date, topic, objectives, method, teacher, student, classNo)
      cur.execute(sql, val)
      conn.commit()
      cur.close()
      conn.close()
    except Exception as e:
      print(e)

    return redirect(url_for("sec2view.sec2computing"))

  else:
    classNo = request.args.get('classNum')
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec2computing WHERE classno = " + str(classNo)
    cur.execute(sql)
    note = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("sec2computingUpdate.html",
                           note=note,
                           classNum=classNo,
                           title="Update")


@sec2view.route("/sec2computingInsert", methods=['GET', 'POST'])
def sec2computingInsert():
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

      sql = "INSERT INTO sec2computing (classno, date, topic, objectives, method, teacheractivity, studentactivity) VALUES (%s, %s, %s, %s, %s, %s, %s)"
      val = (classNo, date, topic, objectives, method, teacher, student)

      cur.execute(sql, val)
      conn.commit()
      cur.close()
      conn.close()
    except Exception as e:
      print(e)

    return redirect(url_for("sec2view.sec2computing"))

  else:
    classNum = request.args.get('classNum')
    return render_template("sec2computingInsert.html", classNum=classNum)

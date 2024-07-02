from flask import Blueprint, redirect, render_template, request, url_for
import psycopg2

sec1view = Blueprint('sec1view', __name__)

DB_NAME = "stgbcdb81d2a7f6"
DB_USER = "usr308e594d3db4f80e"
DB_PASS = "de591a649e24bba5a421ba0063ee4bd2"
DB_HOST = "pg-99bcde18-2a38-481f-8125-ad8d06aa1cbe.schematogo.us-east-1.antimony.io"
DB_PORT = "20478"

#Secondary 1 Mathematics
@sec1view.route("/sec1maths", methods=['GET', 'POST'])
def sec1maths():

  if request.method == 'POST':

    classNum = request.form.get("classNum")

    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec1maths ORDER BY classno"
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
        return redirect(url_for("sec1view.sec1mathsInsert", classNum=classNum))

    if request.form['button'] == 'update':
      if classNum in numbers:
        return redirect(url_for("sec1view.sec1mathsUpdate", classNum=classNum))
      else:
        pass  #class does not exist

    return render_template("sec1maths.html", data=data)

  else:

    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec1maths ORDER BY classno DESC"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("sec1maths.html",
                           notes=data,
                           title="Secondary 1 - Mathematics")


#update page
@sec1view.route("/sec1mathsUpdate", methods=['GET', 'POST'])
def sec1mathsUpdate():
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

      sql = "UPDATE sec1maths SET date = %s, topic = %s, objectives = %s, method = %s, teacheractivity = %s, studentactivity = %s WHERE classno = %s"
      val = (date, topic, objectives, method, teacher, student, classNo)
      cur.execute(sql, val)
      conn.commit()
      cur.close()
      conn.close()
    except Exception as e:
      print(e)

    return redirect(url_for("sec1view.sec1maths"))

  else:
    classNo = request.args.get('classNum')
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec1maths WHERE classno = " + str(classNo)
    cur.execute(sql)
    note = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("sec1mathsUpdate.html",
                           note=note,
                           classNum=classNo,
                           title="Update")


@sec1view.route("/sec1mathsInsert", methods=['GET', 'POST'])
def sec1mathsInsert():
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

      sql = "INSERT INTO sec1maths (classno, date, topic, objectives, method, teacheractivity, studentactivity) VALUES (%s, %s, %s, %s, %s, %s, %s)"
      val = (classNo, date, topic, objectives, method, teacher, student)

      cur.execute(sql, val)
      conn.commit()
      cur.close()
      conn.close()
    except Exception as e:
      print(e)

    return redirect(url_for("sec1view.sec1maths"))

  else:
    classNum = request.args.get('classNum')
    return render_template("sec1mathsInsert.html", classNum=classNum)




##########################################################################

#Secondary 1 Science
@sec1view.route("/sec1science", methods=['GET', 'POST'])
def sec1science():

  if request.method == 'POST':

    classNum = request.form.get("classNum")

    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec1science ORDER BY classno"
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
        return redirect(url_for("sec1view.sec1scienceInsert", classNum=classNum))

    if request.form['button'] == 'update':
      if classNum in numbers:
        return redirect(url_for("sec1view.sec1scienceUpdate", classNum=classNum))
      else:
        pass  #class does not exist

    return render_template("sec1science.html", data=data)

  else:

    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec1science ORDER BY classno DESC"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("sec1science.html",
                           notes=data,
                           title="Secondary 1 - Science")


#update page
@sec1view.route("/sec1scienceUpdate", methods=['GET', 'POST'])
def sec1scienceUpdate():
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

      sql = "UPDATE sec1science SET date = %s, topic = %s, objectives = %s, method = %s, teacheractivity = %s, studentactivity = %s WHERE classno = %s"
      val = (date, topic, objectives, method, teacher, student, classNo)
      cur.execute(sql, val)
      conn.commit()
      cur.close()
      conn.close()
    except Exception as e:
      print(e)

    return redirect(url_for("sec1view.sec1science"))

  else:
    classNo = request.args.get('classNum')
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec1science WHERE classno = " + str(classNo)
    cur.execute(sql)
    note = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("sec1scienceUpdate.html",
                           note=note,
                           classNum=classNo,
                           title="Update")


@sec1view.route("/sec1scienceInsert", methods=['GET', 'POST'])
def sec1scienceInsert():
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

      sql = "INSERT INTO sec1science (classno, date, topic, objectives, method, teacheractivity, studentactivity) VALUES (%s, %s, %s, %s, %s, %s, %s)"
      val = (classNo, date, topic, objectives, method, teacher, student)

      cur.execute(sql, val)
      conn.commit()
      cur.close()
      conn.close()
    except Exception as e:
      print(e)

    return redirect(url_for("sec1view.sec1science"))

  else:
    classNum = request.args.get('classNum')
    return render_template("sec1scienceInsert.html", classNum=classNum)


#############################################################################

#Secondary 1 English
@sec1view.route("/sec1english", methods=['GET', 'POST'])
def sec1english():

  if request.method == 'POST':

    classNum = request.form.get("classNum")

    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec1english ORDER BY classno"
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
        return redirect(url_for("sec1view.sec1englishInsert", classNum=classNum))

    if request.form['button'] == 'update':
      if classNum in numbers:
        return redirect(url_for("sec1view.sec1englishUpdate", classNum=classNum))
      else:
        pass  #class does not exist

    return render_template("sec1english.html", data=data)

  else:

    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec1english ORDER BY classno DESC"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("sec1english.html",
                           notes=data,
                           title="Secondary 1 - English")


#update page
@sec1view.route("/sec1englishUpdate", methods=['GET', 'POST'])
def sec1englishUpdate():
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

      sql = "UPDATE sec1english SET date = %s, topic = %s, objectives = %s, method = %s, teacheractivity = %s, studentactivity = %s WHERE classno = %s"
      val = (date, topic, objectives, method, teacher, student, classNo)
      cur.execute(sql, val)
      conn.commit()
      cur.close()
      conn.close()
    except Exception as e:
      print(e)

    return redirect(url_for("sec1view.sec1english"))

  else:
    classNo = request.args.get('classNum')
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM sec1english WHERE classno = " + str(classNo)
    cur.execute(sql)
    note = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("sec1englishUpdate.html",
                           note=note,
                           classNum=classNo,
                           title="Update")


@sec1view.route("/sec1englishInsert", methods=['GET', 'POST'])
def sec1englishInsert():
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

      sql = "INSERT INTO sec1english (classno, date, topic, objectives, method, teacheractivity, studentactivity) VALUES (%s, %s, %s, %s, %s, %s, %s)"
      val = (classNo, date, topic, objectives, method, teacher, student)

      cur.execute(sql, val)
      conn.commit()
      cur.close()
      conn.close()
    except Exception as e:
      print(e)

    return redirect(url_for("sec1view.sec1english"))

  else:
    classNum = request.args.get('classNum')
    return render_template("sec1englishInsert.html", classNum=classNum)


#############################################################################


#Secondry 1 computing
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

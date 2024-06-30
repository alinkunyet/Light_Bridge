from flask import Blueprint, redirect, render_template, request, url_for
import psycopg2

sec1view = Blueprint('sec1view', __name__)

DB_NAME = "stgbcdb81d2a7f6"
DB_USER = "usr308e594d3db4f80e"
DB_PASS = "de591a649e24bba5a421ba0063ee4bd2"
DB_HOST = "pg-99bcde18-2a38-481f-8125-ad8d06aa1cbe.schematogo.us-east-1.antimony.io"
DB_PORT = "20478"


@sec1view.route("/", methods=['GET', 'POST'])
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

    if classNum in numbers:
      return redirect(url_for("sec1view.update", classNum = classNum))

    return render_template("sec1computing.html", data = data)
  
  else:

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
    
    return render_template("sec1computing.html",
       notes=data,
       title="Secondary 1 - Computing")
  

@sec1view.route("/update", methods=['GET', 'POST'])
def update():
  if request.method == "POST":
    try :
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
      cur.execute(sql,val)
      conn.commit()
      cur.close()
      conn.close()
    except Exception as e:
      print(e)
     
    return redirect(url_for("sec1view.sec1computing"))
  	
  else:
    classNo =  request.args.get('classNum')
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
    
    return render_template("update.html", note = note, classNum = classNo, title = "Update")



@sec1view.route("/blank")
def blank():
  return render_template("blank.html")
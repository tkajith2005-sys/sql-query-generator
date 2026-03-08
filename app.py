from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="nm_project"
)

@app.route('/', methods=['GET','POST'])
def home():
    result = []
    if request.method == 'POST':
        question = request.form['question']

        if "all students" in question:
            query = "SELECT * FROM students"
        elif "marks above 80" in question:
            query = "SELECT * FROM students WHERE marks > 80"
        else:
            query = "SELECT * FROM students"

        cursor = db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

    return render_template("index.html", result=result)

app.run(debug=True)
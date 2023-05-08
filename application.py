from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registrants")
def registrants():
    return render_template("registered.html")

@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("dorm"):
        return render_template("failure.html")
    file = open("registered.csv", "a")
    writer = csv.writer(file)
    writer.writerow((request.form.get("name"), request.form.get("dorm")))
    file.close()
    return render_template("success.html")

@app.route("/registered")
def registered():
    with open("registered.csv", "r") as file:
        reader = csv.reader(file)
        students = list(reader)
        registrants = []
        for listOfStudents in students:
            if listOfStudents:
                registrants.append(str(listOfStudents[0]) + ' from ' + str(listOfStudents[1]))
    return render_template("registered.html", students=registrants)

if __name__ == '__main__':
    app.run(debug=True)
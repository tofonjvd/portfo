from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<string:page_name>")
def page_name(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open("database.csv", "a", newline="") as database:
        fname=data["fname"]
        lname=data["lname"]
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([fname,lname,email,subject,message])
        return email


@app.route('/submit_form', methods=['POST', 'GET'])
def send():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template("thank_you.html",
            fname=data["fname"],
            lname=data["lname"],
            email=data["email"],
            subject=data["subject"],
            message=data["message"])
        # return redirect("/thank_you.html")
    else:
        return "Something went wrong !!!"


@app.route('/go_to_resume')
def show_resume():
    return render_template("resume.html")
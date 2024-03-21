from flask import Flask, render_template, request
from database import load_projects_from_db, load_project_from_db,add_massage_to_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  projects = load_projects_from_db()
  return render_template('home.html',
                         myskills=projects,
                         myname='Jury Alsultan')


@app.route("/project/<id>")
def show_project(id):
  project = load_project_from_db(id)
  return render_template('projectdetails.html', project=project)


@app.route("/contactus")
def contactpage():
  return render_template('contactus.html')


@app.route("/massage", methods=['post'])
def massagepage():
  data = request.form

  add_massage_to_db(data)
  return render_template('massage_submitted.html', massage=data)

  

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=True)

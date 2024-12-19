from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__) #created a flask application

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
  }
]

# now we need to tell flask what it should return when a certain url is requested. Hence we also need to register routes which are part of the url after the domain names
@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>") #we use <> if we want to give a variable route to the url
def show_job(id):
  job = load_jobs_from_db()[int(id)-1]
  if not job:
    return "Not Found", 404

  return render_template('jobpage.html', 
                         job=job)
  
@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  add_application_to_db(id, data)
  return render_template('application_submitted.html', 
                         application=data,
                         job=job)

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  #we give debug = true so that everytime we make a change in the code, it automatically reloads the page

#mysql://root:UfjActQAADoVrmMEuuXwMLgQrhxpwOzq@junction.proxy.rlwy.net:15282/railway
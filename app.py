from flask import Flask, render_template, jsonify

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
    return render_template('home.html', jobs=JOBS, company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  #we give debug = true so that everytime we make a change in the code, it automatically reloads the page
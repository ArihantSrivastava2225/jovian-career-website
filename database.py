#connect to databse and extract data from the database
import mysql.connector 
from mysql.connector import Error

connection = mysql.connector.connect(
    host='junction.proxy.rlwy.net',          # e.g., 'localhost' or your remote host
    user='root',      # e.g., 'root'
    password='UfjActQAADoVrmMEuuXwMLgQrhxpwOzq',  # Replace with your MySQL password
    database='railway',
    port=15282
)

def load_jobs_from_db():
  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM jobs")
    results = cursor.fetchall()
    jobs=[]
    keys=("id", "position", "location", "salary", "currency", "responsibilities", "requirements")
    for row in results:
      values = row
      #we need to convert the tuple to a dictionary as we are working on a dictionary in our html files
      jobs.append(dict(zip(keys, values)))
    return jobs
#finally we did it:
                # Connected to the database
                # (1, 'Data Analyst', 'Bengaluru', 1000000, 'Rs.', 'Process data', 'btech cse, python expertise')
                # (2, 'Data Scientist', 'New Delhi', 1500000, 'Rs.', 'Innovation with data', 'btech cse, python exprtise')
                # Database connection closed
def load_job_from_db(id):
  with connection.cursor() as cursor:
    sql = "SELECT * FROM jobs WHERE id = %s"
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    keys=("id", "position", "location", "salary", "currency", "responsibilities", "requirements")
    values = result
    job = dict(zip(keys, values))
    return job

def add_application_to_db(job_id, data):
  with connection.cursor() as cursor:
    sql = "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (job_id, data['full_name'], data['email'], data['linkedin_url'], data['education'], data['work_experience'], data['resume_url']))
    connection.commit()
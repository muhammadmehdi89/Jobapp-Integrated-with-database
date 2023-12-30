from flask import Flask,render_template,jsonify,request
from database import load_jobs_from_db, load_job_from_db,applications_to_db 

app = Flask(__name__)
JOBS = [
    {
    'id' : 1,
    'Job title' : 'Data Scientist',
    'Location' : 'Karachi, Pakistan',
    'Salary' :  120000
    },
    {
    'id' : 2,
    'Job title' : 'Intern',
    'Location' : 'Karachi Pakistan'
    },
    {
    'id' : 3,
    'Job title' : 'Data Analyst',
    'Location' : 'Lahore Pakistan',
    'Salary' : 80000
    },
    {
    'id' : 4,
    'Job title' : 'Back End',
    'Location' : 'Karachi Pakistan',
    'Salary' : 120000
    }
]


@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs,
                           company_name='Muhammad',search = 'search')
@app.route("/contact")
def Contact():
    return render_template('Contact.html', jobs=JOBS,
                           company_name='Muhammad',search = 'search')
@app.route("/jobs/<id>")
def show(id):
    jobs = load_job_from_db(id)
    return render_template('jobs.html',jobs = jobs
                           ,company_name = 'Muhammad')

@app.route("/job/<id>/apply", methods = ['post'])
def submit(id):
    data = request.form
    jobs = load_job_from_db(id)
    #applications_to_db(id,data)
    return render_template('application_submitted.html'
                           ,company_name = 'Muhammad',application = data,jobs=jobs)



@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)

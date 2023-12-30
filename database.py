from sqlalchemy import create_engine, text
import pandas as pd
db_connection_string = "mysql+pymysql://gllat690w3t6d9hg6y33:pscale_pw_PlbSoJLsjLoc9VgPZcoajO7NPy78dzOzr4ESWm4DgPk@aws.connect.psdb.cloud/muhammadcareers?charset=utf8mb4"
engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl" : {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("Select * from jobs"))
        jobs = pd.DataFrame(result)
        
        return jobs
    
        #print(dict(jobs))
def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text(f"Select * from jobs where id = {id}"))
        jobs = pd.DataFrame(result)
        return jobs

def applications_to_db(job_id,data):
    with engine.connect() as conn:
        full_name=data['full_name']
        email=data['email']
        linkedin_url=data['linkedin_url']
        education = data['education']
        work_experience=data['work_experience'],
        resume_url=data['resume_url']
        x = conn.execute(text(f"Insert into applications (job_id,full_name,email,linkedin_url,education,work_experience,resume_url) Values({job_id},{full_name}, {email},{linkedin_url},{education}, {work_experience}, {resume_url})"))
        print(x)

'''with engine.connect() as conn:
        result = conn.execute(text("Select * from jobs"))
        result_all = result.all()
        print(pd.DataFrame(result_all))

'''
#python database.py

from sqlalchemy import create_engine, text
import pandas as pd
db_connection_string = "mysql+pymysql://your_username:your_password@your_database_host/your_database_name?charset=utf8mb4"
engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl" : {
            "ssl_ca": "write ssl from your database: /.../.../......"
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

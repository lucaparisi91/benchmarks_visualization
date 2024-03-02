import psycopg2
from config import load_config
import random 
import numpy as np
import datetime
import copy
import time
def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)



class database:

    def __init__(self,filename):
        config = load_config(filename)
        self.conn=connect(config)

    def _execute(self,command):
        print(command)
        with self.conn.cursor() as cur:
            pass
            cur.execute(command)
        self.conn.commit()

    def add_test(self,job ):
        hash_test=job["hash"]
        command = f"INSERT INTO test(name, environment, hash) VALUES ( '{job['name']}', '{job['environment']}','{hash_test}');"
        self._execute(command)
        for metric in job["metrics"]:
            self._execute( 
                f"INSERT INTO METRIC(name,unit,test_id) SELECT '{metric['name']}' AS name, '{metric['unit']}' AS unit,test_id FROM test WHERE hash='{hash_test}';"
            )
    def add_job(self,job):

        command=f"INSERT INTO job(job_id,test_id,successful,start_time) SELECT {job['id']} AS job_id,test_id,{job['successful']} as successful, '{job['start_time']}' AS start_time FROM test WHERE hash='{job['hash']}';"
        self._execute(command)
        time.sleep(1)
        for performance in job["performance"]:
            command=f"INSERT INTO performance SELECT test_id,metric_id,{job['id']} AS job_id,{performance['value']} AS VALUE  FROM metric WHERE test_id=(SELECT test_id FROM test WHERE hash='{job['hash']}') AND name='{performance['metric']}';"
            self._execute(command)
            


def generate_random_tests(template):
    rng=np.random.default_rng()
    job_ids= np.arange(345,450,)
    values=rng.uniform(low=0.1, high=13.3, size=len(job_ids))


    times= [ (datetime.datetime.now() - datetime.timedelta(days=1) ).strftime("%Y-%m-%d %H:%M:%S+00") for job_id in job_ids ]

    benchmarks=[]
    for job_id , time,value in zip(job_ids,times,values):
        dummy_job=copy.deepcopy(template)
        dummy_job["start_time"]=time
        dummy_job["id"]=job_id
        dummy_job["performance"][0]["value"]=value
        benchmarks.append(dummy_job)
    return benchmarks


if __name__ == '__main__':
    test_benchio = {
                "name" : "benchio",
                "environment" : "gnu",
                "hash" : "6543yui",
                "metrics": [ {"name":"bandwidth","unit":"GiB/s"}]
            }
    template_job = {
        "hash" : "6543yui",
        "successful" : True, 
        "id": 12345,
        "start_time" : "2024-01-12 14:32:00+00",
        "performance" : 
        [
            {"metric" : "bandwidth","value":0.8}
        ]
    }

    db=database("db.ini")


    #db.add_test(test_benchio)
    #db.add_job(test_job)
    test_jobs=generate_random_tests(template_job)
    print(test_jobs)
    for test_job in test_jobs:
        db.add_job(test_job)
        


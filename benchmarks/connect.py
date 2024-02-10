import psycopg2
from config import load_config

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

    def add_job(self,job ):

        with self.conn.cursor() as cur:
    
        
        
            command = f"INSERT INTO test(name, environment, hash) VALUES ( '{job['name']}', '{job['environment']}','{job['hash']}');"
            print(command)

            cur.execute(command)
        self.conn.commit()



if __name__ == '__main__':
        job = {
                "name" : "benchio",
                "environment" : "gnu",
                "hash" : "6543yui"
                }
        
        db=database("db.ini")
        db.add_job(job)


        

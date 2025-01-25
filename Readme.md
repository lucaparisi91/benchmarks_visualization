
# Visualization of Reframe tests and benchmarking 

The project consists in creating a database ( postgresql ) to hold data from benchmarks. Those benchmarks are then queried from Graphana and a visualization is obtained.]

## Graphana

```bash
sudo grafana-cli admin reset-admin-password
```

## Database 

Install the postgresql database with 

```bash
sudo dnf install -y postgresql-server
sudo dnf install -y postgresql
sudo postgresql-setup --initdb
sudo systemctl enable postgresql.service
sudo systemctl start postgresql 
sudo -u postgres psql postgres
postgres=# \password postgres
Enter it again: 
postgres=# 

sudo reboot
```

Get startarted by startating the database in the VM

```bash
systemctl start postgresql.service
```

Create the benchmrks database. Run `sudo -u postgres psql ` to open the database shell

```bash
sudo -u postgres createdb benchmarks

```


The database was created with the commands 

```SQL
CREATE TABLE test ( name varchar(40), environment varchar(40), test_id SERIAL NOT NULL PRIMARY KEY , hash VARCHAR(20) );
CREATE TABLE metric ( name varchar(40), unit varchar(15), test_id int , CONSTRAINT testk FOREIGN KEY(test_id) REFERENCES test (test_id) ON DELETE CASCADE, metric_id SERIAL NOT NULL PRIMARY KEY );
CREATE TABLE job ( job_id SERIAL NOT NULL PRIMARY KEY, successful boolean, start_time TIMESTAMP WITH TIME ZONE, test_id int, CONSTRAINT testk FOREIGN KEY(test_id) REFERENCES test(test_id)   );
CREATE TABLE performance ( value DOUBLE PRECISION , metric_id int, job_id int, benchmark_id SERIAL NOT NULL PRIMARY KEY, CONSTRAINT metrick FOREIGN KEY(metric_id) REFERENCES metric, CONSTRAINT jobk FOREIGN KEY(job_id) REFERENCES job ON DELETE CASCADE  );
ALTER TABLE test ADD CONSTRAINT hash_unique UNIQUE(hash);

```

```SQL
INSERT INTO test ( name, environment ) VALUES ('benchio', 'gnu');
CREATE USER cse WITH PASSWORD 'cse';
SELECT usename FROM pg_user;
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO cse;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO cse;
```
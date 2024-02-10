
# Visualization of Reframe tests and benchmarking 

The project consists in creating a database ( postgresql ) to hold data from benchmarks. Those benchmarks are then queried from Graphana and a visualization is obtained.]

## Graphana

```bash
sudo grafana-cli admin reset-admin-password
```

## Database 

- Strings should always be used within quotes

```SQL
CREATE TABLE test ( name varchar(40), environment varchar(40), test_id SERIAL NOT NULL PRIMARY KEY , hash VARCHAR(20) );
CREATE TABLE metric ( name varchar(40), unit varchar(15), test_id int REFERENCES test(test_id)  );
CREATE TABLE job ( job_id int, test_id int REFERENCES test(test_id), successfull boolean, start_time timestamp with time zone   );
INSERT INTO test ( name, environment ) VALUES ('benchio', 'gnu');
CREATE USER cse PASSWORD cse;
SELECT usename FROM pg_user;
GRANT SELECT ON test TO cse;
GRANT INSERT ON test TO cse;
GRANT UPDATE ON test TO cse;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO cse;
ALTER TABLE test ADD CONSTRAINT hash_unique UNIQUE(hash)
```

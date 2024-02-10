
# Visualization of Reframe tests and benchmarking 

The project consists in creating a database ( postgresql ) to hold data from benchmarks. Those benchmarks are then queried from Graphana and a visualization is obtained.]

## Graphana

```bash
sudo grafana-cli admin reset-admin-password
```

## Database 

```SQL
CREATE TABLE test ( name varchar(40), environment varchar(40), test_id SERIAL NOT NULL PRIMARY KEY );
```
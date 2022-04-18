# Mining

## Overview
![Docker Airflow 2.0 architecture](https://miro.medium.com/max/1100/1*pAUdLzHgRMKFw2gVuasyCA.png)

## Requirements
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/install/)

## Running
For simple usage I prepared docker-compose image of Mining service, all you need is to run following commands:
```
cd mining
docker-compose run -d
```

## Usage

* Airflow 2.2.5: [localhost:8080](http://localhost:8080/)
    * Username: admin
    * Password: admin
* PGAdmin : [localhost:5050](http://localhost:5050/)
  * Default password: admin
* Postgres DB 13
  * Username: punk
  * Password: crypto
        
Note: Airflow username and password can be configured in `/scripts/entrypoint.sh`, 
postgres credentials you can change at `docker-compose.yml`


## Configuring Airflow

It's possible to set any configuration value for Airflow from environment 
variables in **.env** file where we can set airflow running 
variables to override the default configuration that is generated as airflow.cfg 
file after the initial run.

The general rule is the environment variable should be named 
`AIRFLOW__<section>__<key>`, for example `AIRFLOW__CORE__SQL_ALCHEMY_CONN` sets 
the `sql_alchemy_conn` config option in the `[core]` section.

Check out the [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html) for more details

You can also define connections via environment variables by prefixing them 
with `AIRFLOW_CONN_` - for example `AIRFLOW_CONN_POSTGRES_MASTER=postgres://user:password@localhost:5432/master` 
for a connection called "postgres_master". The value is parsed as a URI. This 
will work for hooks etc, but won't show up in the "Ad-hoc Query" section unless 
an (empty) connection is also created in the DB

# Credits


Big thanks to @AVAInformationSystems [for their Medium article](https://medium.com/ava-information/airflow-2-0-docker-development-setup-docker-compose-postgresql-7911f553b42b), it helped me to build right docker for Airflow service and postgres db

Thanks to @mfvanek [for his code](https://github.com/mfvanek/useful-sql-scripts/tree/master/running_pg_in_docker) and [the habr article](https://habr.com/ru/post/578744/), it helped to setup postgres database

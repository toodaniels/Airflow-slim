# Airflow-LocalExecutor
Airflow Docker compose modified to use LocalExecutor and add additional requirements

## How to use

- Add your dependencies in the `requirements.txt`  file 
 - Use de commands
	 - `docker-compose up airflow-init ` to initialize the Airflow database.
	 - `docker-compose up -d`

Additionaly you can rebuild the Airflow image usind the command `docke-compose up --build` if you add a dependency after use `docker-compose up -d`.

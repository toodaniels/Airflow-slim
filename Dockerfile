FROM apache/airflow:2.1.4 

WORKDIR /opt/airflow/

# Add your extra dependencies in requirements.txt
COPY requirements.txt .

RUN pip install -r requirements.txt

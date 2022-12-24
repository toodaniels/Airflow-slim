FROM apache/airflow:latest-python3.10

WORKDIR /opt/airflow/

# Add your extra dependencies in requirements.txt
COPY requirements.txt .

RUN pip install -r requirements.txt

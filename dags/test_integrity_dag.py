from airflow import DAG
from datetime import datetime
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator, FailOperator

args = {
    'owner': 'Daniel',
    'start_date': datetime(2021,1,1), 
    'depends_on_past': False 
}   

with DAG('test_integrity_example_dag',
    schedule_interval="@daily",
    default_args=args,
    catchup=False
) as dag:

    start = DummyOperator(
        task_id="start"
    )

    task_1 = PythonOperator(
        task_id="task_1",
        python_callable=lambda x: print(x)
    )

    task_2 = PythonOperator(
        task_id="task_2",
        python_callable=lambda x: print(x)
    )

    task_3 = PythonOperator(
        task_id="task_3",
        python_callable=lambda x: print(x)
    )

    end = DummyOperator(
        task_id="end"
    )

    start >> task_1 >> task_2 >> task_3 >> end



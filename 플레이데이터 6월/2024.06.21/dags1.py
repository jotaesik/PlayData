import json
import pathlib
import airflow.utils.dates
import requests
import requests.exceptions as requests_exceptions
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pendulum
import os
kst = pendulum.timezone("Asia/Seoul")


dag = DAG(
    dag_id = 'test_dag',
    description="practice dags",
    start_date=datetime(2024, 6,20, tzinfo=kst),
    schedule_interval="*/1 * * * *",
    catchup=False,
)




def _myfunc():
    with open("/home/hadoop/a.txt", "w") as f:
        f.write(f"a.txt - {datetime.now()}")
   
def _myfunc1():
    with open("/home/hadoop/a1.txt", "w") as f:
        f.write(f"a1.txt - {datetime.now()}")   


write_time = PythonOperator(task_id='write_time',
                python_callable=_myfunc,
                dag=dag
                )

write_time1 = PythonOperator(task_id='write1_time',
                python_callable=_myfunc1,
                dag=dag
                )

write_time >> write_time1

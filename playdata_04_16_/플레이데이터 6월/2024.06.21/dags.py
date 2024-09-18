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
import pandas as pd
from airflow.operators.bash_operator import BashOperator


kst = pendulum.timezone("Asia/Seoul")


dag = DAG(
    dag_id = 'weather_dag',
    description="weather dags",
    start_date=datetime(2024, 6,21, tzinfo=kst),
    schedule_interval="*/1 * * * *",
    catchup=False,
)




def _crawling():
    url = "https://weather.naver.com/choiceApi/api?choiceQuery=%7B%22nationFcast%22%3A%7B%22aplYmd%22%3A%2220240621%22%2C%22hdayType%22%3A%22now%22%7D%7D"
    r = requests.get(url)
    weather_need = r.json()
    dict_data = weather_need["results"]["choiceResult"]["nationFcast"]
    lareaNm = [] #제주특별자치도
    tmpr = [] #온도
    fcastYmdt =[] #년월일시간
    for key , value in dict_data.items():
        # pass
        lareaNm.append(value["lareaNm"])
        tmpr.append(value["tmpr"])
        # fcastYmdt.append(value["fcastYmdt"]) 
    df = pd.DataFrame(zip(lareaNm, tmpr), columns=['지역', '온도'])

    # df.columns = ["지역","온도"]
    # df.to_csv('/home/hadoop/weather.txt')
    with open("/home/hadoop/weather.csv", "w") as f:
            # f.write("\n\n")  # 데이터 간 구분을 위한 줄바꿈 추가
            f.write(df.to_string(index=False))
   
# def _myfunc1():
#     with open("/home/hadoop/a1.txt", "w") as f:
#         f.write(f"a1.txt - {datetime.now()}")   


crawling_time = PythonOperator(task_id='write_time1',
                python_callable=_crawling,
                dag=dag
                )

scp_file = BashOperator(task_id='scp_file',
                bash_command='scp /home/hadoop/weather.csv encore@ip:/home/encore/repos2/weather.csv',
                dag=dag
                )

crawling_time >> scp_file

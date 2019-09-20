from airflow import DAG
from datetime import date, time, timedelta,datetime
from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.python_operator import PythonVirtualenvOperator
from callables.upload import run_myprog
# from ../airflow_repo.callables.upload import run_myprog


default_args = {
    "start_date": datetime(2019, 8, 1),
    "schedule_interval": "30 22 * * *",
    "retries": 3,
    # "depends_on_past": True,
    "catchup": False
}

# Tasks
# 1.  File Watcher
# def watch_for_file():
# 2.  File Transform
# 3.  Load DB
# 4.  Trigger_email


dag = DAG("load_dxb_proj",start_date=default_args['start_date'], default_args=default_args, catchup=False)

with dag:
    check_for_file = FileSensor(filepath="home/ash/landing/del.out",fs_conn_id='fs_default', task_id="s1")
    pythonvenv = PythonVirtualenvOperator(task_id="pythonvenv", python_callable=run_myprog, requirements=['elasticsearch==6.3.1', 'pandas==0.23.4'],
                                   python_version='3.6')


    check_for_file >> pythonvenv

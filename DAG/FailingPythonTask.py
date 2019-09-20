from airflow import  DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

dag = DAG("FailingpythonTask",start_date=datetime(2019,9,12), schedule_interval="@daily", catchup=False)


def myPythonFunction():
    # raise Exception
    print("Zooooo Except bbbbbbbbbbb momooooooooooooooooo")
    raise Exception


with dag:
    t1 = PythonOperator(task_id="t1",dag=dag,python_callable=myPythonFunction)
    t2 = DummyOperator(task_id="t2", trigger_rule="all_done")

    t1>>t2

if __name__ == "__main__":
    dag.cli()
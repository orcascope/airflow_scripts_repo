def run_myprog():
    print("Test my callable package ")
    import pandas as pd
    from elasticsearch import Elasticsearch
    from elasticsearch.helpers import bulk
    from time import time


    t0=time()

    # size of the bulk
    chunksize=5000

    # open csv file
    # f = open("version1.csv", encoding="utf8") # read csv

    # parse csv with pandas
    df = pd.read_csv("/home/ash/airflow_repo/data/version1.csv")
    df = df.astype(str)
    es = Elasticsearch()
    columns = list(df.columns)
    df.columns = columns
    df['id'] = range(len(df))
    docs = df.to_dict('records')

# Truncate the index first
    es.delete_by_query(index='ur_index', body='{"query": {"match_all":{}}}')

    i = 1
    for _ in docs:
        i +=1
        try:
            es.index(index='ur_index', doc_type='project_line', body=_, id=_['id'])
        except Exception:
            raise
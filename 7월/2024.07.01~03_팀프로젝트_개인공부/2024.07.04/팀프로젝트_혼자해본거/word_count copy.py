from dotenv import load_dotenv
import os
import MeCab
from collections import Counter
from datetime import datetime
import subprocess
from pyspark.sql import SparkSession
from pyspark.sql.functions import year, month, dayofmonth,col
from pyarrow import fs
import pyarrow as pa    
import pyarrow.parquet as pq
import make_table
from pyspark.sql.functions import date_format
import pyspark
from pyspark.sql import SparkSession
from sqlalchemy import create_engine
import pandas as pd
from collections import OrderedDict

def make_spark():
    spark = SparkSession.builder.config(conf=conf).getOrCreate()
    return spark

# conf 파일 정보 불러오기
def road_env(): 
    conf = {}
    with open('/home/hadoop/DE31-3rd_team3/.env', 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            conf[key] = value
    return conf
# word_tokenize 형태소 분석하기
def word_tokenize(text):
    try:
        mecab = MeCab.Tagger('-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ko-dic')
        result = mecab.parse(text)
        return result
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def mysql_engine(spark):
    conf = road_env()
    # connect to mysql
    engine = create_engine('mysql+pymysql://'+conf['USER']+':'+conf['PWD']+'@'+conf['HOST']+':'+conf['PORT']+'/'+conf['DB'])
    return engine
   

def text_file_read(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text_file = file.read()  
        return text_file

def n_into_dict(all_dic,token_out):
    # dic = dict()
    lines = token_out.strip().split('\n')
    for i in lines:
        try:
            word= i.split("\t")[0]
            stop_check = i.split("\t")[1].split(",")[0]
            if stop_check[0] =="N":
                if word not in all_dic:
                    all_dic[word]=1
                else:
                    all_dic[word]+=1
        except IndexError:
            # print(f"{i} ------>error") #끝에 EOS
            continue
    return all_dic
def insert_sql_dic(all_dic,engine):
    for i, (key, value) in enumerate(all_dic.items()):
        make_table.insert_data(engine,datetime(2024,5,i,0,0,0),"main_section","sub_section",key,value) #이것도 바꾸기...

def main():
    spark = make_spark()
    engine = mysql_engine(spark)
    sql_engine = make_table.make_engine()
    make_table.create_table(sql_engine)
    for i in range(1,23):
        date_str = f"2024-05-{i:02}"
        query = f"SELECT * FROM naver_miniproject.news WHERE datetime LIKE '{date_str}%%'"
        #여기에 뒤에 MAIN,SUB만 넣으면 됨...
        df = pd.read_sql_query(query, engine)
        for i in range(0,len(df)):
            temp = word_tokenize(df.loc[i,"content"])
            all_dic = n_into_dict(all_dic,temp) 
        # print(f"end{i}")
        insert_sql_dic(all_dic,engine)
    # sorted_data = sorted(all_dic.items(), key=lambda x: x[1], reverse=True)
    # print(sorted_data)
if __name__ == '__main__':
  main()
from dotenv import load_dotenv
import os
import MeCab
from collections import Counter
import make_table
from datetime import datetime
import subprocess
from pyspark.sql import SparkSession
from pyspark.sql.functions import year, month, dayofmonth,col
from pyarrow import fs
import pyarrow as pa    
import pyarrow.parquet as pq
from pyspark.sql.functions import date_format
import pyspark
from pyspark.sql import SparkSession

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
def word_tokenize(line):
    try:
        mecab = MeCab.Tagger('-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ko-dic')
        result = mecab.parse(line)
        return result.str
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def text_file_read(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text_file = file.read()  
        return text_file

def n_into_dict(answer_dic,token_out):
    # dic = dict()
    lines = token_out.strip().split('\n')
    for i in lines:
        try:
            word= i.split("\t")[0]
            stop_check = i.split("\t")[1].split(",")[0]
            if stop_check[0] =="N":
                if word not in answer_dic:
                    answer_dic[word]=1
                else:
                    answer_dic[word]+=1
        except IndexError:
            print(f"{i} ------>error") #끝에 EOS
            continue
    return answer_dic

def hadoop_read():
    conf = road_env()
    classpath = subprocess.Popen(["/home/hadoop/hadoop/bin/hdfs", "classpath", "--glob"], stdout=subprocess.PIPE).communicate()[0]
    os.environ["CLASSPATH"] = classpath.decode("utf-8")
    # print(conf)
    hdfs = fs.HadoopFileSystem(host=f"{conf['HADOOP_HOST']}", port=8020, user='minip3')
    return hdfs

def read_hadoop_file_list():
    pass

def read_hadoop_data():
    # spark.stop()
    spark = make_spark()
    conf = road_env()
    df = spark.read.csv(f"hdfs://{conf['HADOOP_HOST']}:{conf['HADOOP_PORT']}/user/minip3/mort/*.parquet",header=True) #일별로 바꾸기...
    return df

def main():
    conf = road_env()
    file_path = "/home/hadoop/DE31-3rd_team3/Crawler/counter.txt" #하둡에서 읽어지게
    # text_input = text_file_read(file_path)
    # token_out = word_tokenize(text_input)
    # dic = n_into_dict(token_out) 
    engine = make_table.make_engine()
    df = read_hadoop_data() #parquet파일다있다...
    answer_dic = dict() 
    for i in range(len(df.count())):
        filtered_content = df.filter(df['id'] == i).select('content')
        token_out = word_tokenize(filtered_content)
        answer_dic = n_into_dict(answer_dic,token_out) 
    
    for i, (key, value) in enumerate(answer_dic.items()):
        make_table.insert_data(engine,datetime(2024,7,4,0,0,i),i*100,i*100+i,key,value) #이것도 바꾸기...
    

if __name__ == '__main__':
  main()
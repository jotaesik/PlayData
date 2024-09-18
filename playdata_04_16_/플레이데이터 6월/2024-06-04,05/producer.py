from confluent_kafka import Producer


def delivery(err, msg):
    if err is not None:
        print("메시지 전송 실패 :{}".format(err))
    else:
        print("{}으로 {}의 데이터 전송".format(msg.topic(), msg.partition()))


producer = Producer({
    'bootstrap.servers' : 'broker1:9092,broker2:9092,broker3:9092',
    'batch.size' : 20000,
    'acks' : 'all',
    'retries' : 1,
    'linger.ms' : 1
    })


producer.poll(0)


for i in range(0, 10):
    msg_data = "전달 메시지: {}".format(i)
    producer.produce('en0605', msg_data , callback=delivery)


producer.flush()

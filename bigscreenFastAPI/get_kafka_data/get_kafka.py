#!/usr/bin/python
# -*- coding: utf-8 -*-
# creater: Alan.Song


#import json
from kafka import KafkaConsumer


#bootstrap_servers = ['10.212.1.52:9092', ]
#
consumer = KafkaConsumer("ueba", auto_offset_reset='earliest', bootstrap_servers=["10.212.1.54:9092",],consumer_timeout_ms=10000)

n = 0
for message in consumer:
    if n < 10:
        message_value=message.value.decode().replace("\\", "")
        n += 1
        print(f"Topic: {message.topic}, Partiton: {message.partition}, Offset: {message.offset}, raw_message: {message_value}")
    else:
        break
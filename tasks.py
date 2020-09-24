from celery import Celery
from celery.contrib import rdb
from time import sleep
import random
# Connecting to the rabbitmq broker through localhost
obj=Celery('tasks',backend='rpc://',broker='amqp://guest@localhost//')

@obj.task
def hello():
    sleep(random.randint(1, 10))
    rdb.set_trace()
    return "hello world!"

@obj.task
def calculator(num_1,num_2,operator):
    sleep(random.randint(1, 10))
    return str(eval(str(num_1)+operator+str(num_2)))

from celery import Celery
from time import sleep
import random
# Connecting to the rabbitmq broker through localhost
obj=Celery('tasks',backend='rpc://',broker='amqp://guest@localhost//')

@obj.task
def hello():
    sleep(random.randint(1, 10))
    return "hello world!"

@obj.task
def calculator(num_1,num_2,operator):
    sleep(random.randint(1, 10))
    return str(eval(str(num_1)+operator+str(num_2)))

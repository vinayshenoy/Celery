from tasks import hello,calculator
from time import sleep

if __name__ == '__main__':
    print("Test Celery using hello world!")
    result1=hello.delay()
    print("Execute calculator addition operation:- 4+5")
    result2=calculator.delay(4,5,"+")
    print("#---------------------------------#")
    print()
    flag1,flag2=False,False
    while True:
        if(result1.ready() and not flag1):
            print("Hello function Output: ",result1.result)
            flag1=True
        if(result2.ready() and not flag2):
            print("Calculator function Output: ",result2.result)
            flag2=True
        if(flag1 and flag2):
            print("All tasks done!!!")
            exit(0)
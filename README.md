# Celery

## Execute celery 
To execute the celery app, we execute the following command:
```
celery -A tasks worker -l info -P gevent
```

## Execute tasks 
To execute the tasks defined in celery app, we write a script called `process.py`. To execute `process.py`, we use a following command:
```
python process.py
```

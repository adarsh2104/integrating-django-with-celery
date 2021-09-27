# https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html#first-steps


# Module Objective: Creating a new task.

from celery import Celery


app = Celery('tasks', broker='pyamqp://guest@localhost//',backend='redis://localhost')
# app = Celery('<current module name>', broker='<broker: redis/rabbitmq>')



# Add new task for the app.
@app.task
def add(x, y):
    return x + y

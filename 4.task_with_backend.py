# Celery Backend: For saving the task result attributes

app = Celery('tasks', broker='pyamqp://guest@localhost//',backend='redis://localhost')

    # For Keeping Results we use Celery with result backend.like keeping status of task.
    # There are several built-in result backends to choose from:
        # SQLAlchemy/Django ORM, 
        # MongoDB, 
        # Memcached, 
        # Redis, 
        # RPC
        # Custom Built 

@app.task
def add(x, y):
    return x + y


    

        
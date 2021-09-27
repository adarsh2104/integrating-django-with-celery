from celery import Celery
# To use Celery within your project you simply import this instance.


app = Celery('tasks', broker='pyamqp://guest@localhost//',backend='redis://localhost',include=['proj.tasks'])
# app = Celery('proj',
#              broker='amqp://',
#              backend='rpc://',
#              include=['proj.tasks'])
# The include argument is a list of modules to import when the worker starts. 
# You need to add our tasks module here so that the worker is able to find our tasks.


# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()

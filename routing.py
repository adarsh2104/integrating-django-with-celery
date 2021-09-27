# The task_routes setting enables you to route tasks by name and keep everything 
# centralized in one location:

app.conf.update(
    task_routes = {
        'proj.tasks.add': {'queue': 'hipri'},
    },
)

# OR queue can also be specified at the run time.

from proj.tasks import add
add.apply_async((2, 2), queue='hipri')


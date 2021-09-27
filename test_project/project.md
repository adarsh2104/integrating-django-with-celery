https://docs.celeryproject.org/en/stable/getting-started/next-steps.html#next-steps



<!-- Starting the worker -->
<!-- cd to root of the proj -->
```
celery -A proj worker -l INFO

```

<!-- Calling the Tasks -->

<!-- delay() is a shortcut for apply_async() -->

Apply sync has many other args like : 
    * delay time to wait before run (countdown)
    * the queue it should be sent to

<!-- add.apply_async((2, 2), queue='lopri', countdown=10) -->

<!-- Applying the task() directly will execute the task in the current process, so that no message is sent: -->


<!-- Calling a task can be done in 3 ways: -->
1.task.delay()          # return Async results and task is executed.
2.task.apply_async()    # Extra args can be passed for execution return Async results and task is executed.
3.task()                # result is returned instantly (not Async results) and not queued.



<!-- Async Result object attributes  -->

<!-- You can find the task’s id by looking at the id attribute: -->

 - res.id
 - res.get
 - res.state   
 - res.failed()
 - res.successful()



started state is a special state that’s only recorded if the task_track_started setting is enabled, or if the @task(track_started=True) option is set for the task.

State stages : PENDING -> STARTED -> SUCCESS/FAILURE

STARTED - started state is a special state that’s only recorded if the task_track_started setting is enabled.
          or if the @task(track_started=True) option is set for the task.

PENDING - Not a recorded state, but rather the default state for any task id that’s unknown: this you can see from this 


<!-- Tasks PENDING -> STARTED -> RETRY -> STARTED -> RETRY -> STARTED -> SUCCESS -->
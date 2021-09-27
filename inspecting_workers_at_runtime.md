# Making a worker consume from a queue by specifying the celery worker -Q option:

```
celery -A proj worker -Q <queue_1,queue_2>
```


# Gerneral inspection commands

This is implemented by using broadcast messaging, so all remote control commands are received by every worker in the cluster.


 * Checking what task worker is currently on:
   
   ````
   celery -A proj inspect active 
   ````
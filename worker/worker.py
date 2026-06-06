import os
import time
import redis

# Added Redis connection
redis_host = os.environ.get("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

print("Worker started, waiting for tasks...", flush=True)

while True:
    try:
        # brpop blocks until a message is available in 'task_queue'
        # The timeout=0 means it will wait indefinitely
        task = r.brpop("task_queue", timeout=0)

        if task:
            # Print the exact logs requested by the assignment
            print("Worker received task", flush=True)
            print("Processing task...", flush=True)
            time.sleep(1) # Simulate some processing time
            print("Task completed", flush=True)

    except redis.exceptions.ConnectionError:
        print("Waiting for Redis to become available...", flush=True)
        time.sleep(2)

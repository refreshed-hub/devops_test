import os
import redis
from flask import Flask

app = Flask(__name__)

# Added a way to connect to Redis using the hostname defined in docker-compose
redis_host = os.environ.get("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/")
def home():
    return "App is running"

@app.route("/task")
def send_task():
    try:
        # Push a task to the Redis list (queue)
        r.lpush("task_queue", "Run worker task")
        return "Task successfully sent to Redis queue!"
    except Exception as e:
        return f"Error contacting Redis: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

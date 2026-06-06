FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port 5001 as required by the prompt
EXPOSE 5001

CMD ["python", "worker.py"]

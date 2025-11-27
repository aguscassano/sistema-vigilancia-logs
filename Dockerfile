FROM python:3.9-slim
WORKDIR /app

COPY vigilante.py .

RUN mkdir -p /var/log

CMD ["python3", "-u", "vigilante.py"]

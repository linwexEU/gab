FROM python:3.11.12-slim

RUN apt-get update && apt-get install -y libmagic1 libmagic-dev

RUN mkdir /gab_docker

WORKDIR /gab_docker

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /gab_docker/docker/app.sh

CMD ["gunicorn", "main:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]

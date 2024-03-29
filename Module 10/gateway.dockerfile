FROM python:3.10-slim-bullseye 

RUN pip install pipenv 

WORKDIR /app 

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --system 

COPY ["gateway.py", "proto.py", "./"]

EXPOSE 9696 

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "gateway:app"]
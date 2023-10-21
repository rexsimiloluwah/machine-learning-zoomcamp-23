FROM python:3.10-slim-bullseye 

RUN pip install pipenv 

WORKDIR /app 

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --system 

COPY ["app.py", "./"]
COPY ["templates", "./templates"]

EXPOSE 9698

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9698", "app:app"]
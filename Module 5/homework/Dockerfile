FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv 

WORKDIR /app 

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --system

COPY ./web ./web 

EXPOSE 9697 

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9697", "web.main:app" ]
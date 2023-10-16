# Stage 1: Build the application
FROM python:3.10 AS builder

ENV POETRY_VERSION=1.2.1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \ 
    POETRY_CACHE_DIR=/tmp/poetry_cache 

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    build-essential 

# Install Poetry
RUN pip install poetry==${POETRY_VERSION} 

WORKDIR /app 

COPY pyproject.toml poetry.lock ./ 

RUN poetry install --no-root --only main && \
    rm -rf ${POETRY_CACHE_DIR}

# Stage 2: Create the production container 
FROM python:3.10-slim-bullseye AS runtime 

ENV VIRTUAL_ENV=/app/.venv \ 
    PATH="/app/.venv/bin:${PATH}"

WORKDIR /app 

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY ./web ./web 
COPY ./models ./models 
COPY start-web.sh ./

EXPOSE 9696

# Set the environment variables for the Flask app 
# ENV FLASK_APP=main.py 
# ENV FLASK_RUN_HOST=0.0.0.0 

RUN chmod +x start-web.sh

# Start the Flask app
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "web.main:app"]



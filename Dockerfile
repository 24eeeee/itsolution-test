# pull official base image
FROM dockerhub.timeweb.cloud/library/python:3.12-slim-bookworm

# set working directory
WORKDIR /usr/src/itsolution-test

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
RUN pip install poetry
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry install

# add app
COPY runstring_app/ runstring_app/
COPY server/ server/
COPY utils/ utils/
COPY video_storage/ video_storage/
COPY manage.py .
COPY db.sqlite3 .
RUN poetry run python3 manage.py makemigrations
RUN poetry run python manage.py migrate
# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /app/code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install poetry

COPY poetry.lock pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . .
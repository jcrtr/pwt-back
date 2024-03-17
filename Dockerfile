# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /app/code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get install -y mc
RUN apt-get install -y gdal-bin libgdal-dev
RUN apt-get install -y python3-gdal
RUN apt-get install -y binutils libproj-dev
RUN pip install --upgrade pip setuptools wheel
RUN pip install poetry

COPY poetry.lock pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . .
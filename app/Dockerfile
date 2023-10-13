FROM python:3.11.2-slim-buster

WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY . .
COPY ./entrypoint.sh .
RUN chmod 755 /code/entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]

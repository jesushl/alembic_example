# pull official base image
FROM python:3.9-slim-buster

# set working directory
WORKDIR /usr/src/app

# install system dependencies
RUN apt-get update \
  && apt-get -y install  apt-utils netcat gcc postgresql python-psycopg2 libpq-dev \
  && apt-get clean dd 

# install python dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
# add app
COPY . .
 32mnjbvgcfhxdrsewa
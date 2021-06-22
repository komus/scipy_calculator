FROM python:3.8-slim

# install environment dependencies
RUN apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends \
    netcat \
    libpq-dev \
    python-dev \
    gcc \
    && apt-get -q clean

# set working directory
WORKDIR /usr/src/app

# add requirements
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install --upgrade pip
# install requirements
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app
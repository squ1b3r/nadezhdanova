FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
ADD requirements.txt ./
RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install -y ruby ruby-dev
RUN gem install sass

ADD . .

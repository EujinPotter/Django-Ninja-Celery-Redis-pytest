FROM python:3.10.4-slim-buster
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code

RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \ 
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

EXPOSE 8000
EXPOSE 5432

ADD requirements.txt /code
RUN pip3 install -r requirements.txt
COPY . /code

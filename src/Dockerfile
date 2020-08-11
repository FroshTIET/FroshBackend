### Production dockerfile. Using alpine linux

# pull official base image
FROM python:3.8.2-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies

# install build dependencies
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev \
    && apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install packages
COPY ./requirements.txt /usr/src/app/requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

RUN python -m pip install -U --force-reinstall pip  \
    && pip install wheel                            \
    && pip install -r requirements.txt              \    
    && pip install gunicorn                         \
    && pip install psycopg2-binary                  \        
    && chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

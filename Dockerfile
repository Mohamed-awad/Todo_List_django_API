# pull the official base image
FROM python:3.8.3-alpine
MAINTAINER MOHAMED AWAD


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/todo_list_app


RUN mkdir -p /usr/src/todo_list_app/docs/static/mkdocs_build

# install dependencies
COPY ./requirements.txt /usr/src/todo_list_app
RUN pip3 install --upgrade pip
RUN  apk update && apk upgrade
RUN apk add --no-cache bash\
                       pkgconfig \
                       gcc \
                       libcurl \
                       python2-dev \
                       libc-dev \
                       && rm -rf /var/cache/apk/*
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt --no-deps

# copy project
COPY . /usr/src/todo_list_app

# run database migrations
RUN python manage.py makemigrations \
    && python manage.py migrate

# build docs
RUN mkdocs build

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
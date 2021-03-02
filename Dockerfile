FROM python:3.6

ENV PYTHONUNBUFFERED 1

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -U setuptools
RUN pip install -r ./requirements.txt
WORKDIR /app
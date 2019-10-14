FROM python:3
RUN apt-get update && apt-get install gdal-bin -y
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./wait-for-it.sh /usr/bin/wait-for-it.sh
RUN ["chmod", "+x", "/usr/bin/wait-for-it.sh"]
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/
ENTRYPOINT ["sh", "./docker-entrypoint.sh"]

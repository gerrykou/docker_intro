FROM python:3.8

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src src

CMD [ "python", "./src/db_connect.py" ]

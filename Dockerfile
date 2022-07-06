FROM python:3.10.4-slim-bullseye

# set your working directory
WORKDIR /code

# copy the requirements.txt file from your local folder to the image working directory - the dot .
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the src folder
COPY src src

# specify the command that the container should run
CMD [ "python", "./src/app.py" ]

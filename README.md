# docker_intro
Introduction to Docker   

## Run images from docker hub
```shell
docker run --rm -it ubuntu bin/bash   
```

```shell
docker images 
docker ps
docker ps -a
```
https://hub.docker.com/_/python

```shell
docker pull python
docker run --rm -it python
```
```shell
docker run --rm -it python:3.10.4-slim-bullseye
```

```shell
python3 src/app.py 
```
## Build your docker images
```shell
docker build -t my_python_app .
```
```shell
docker run --rm my_python_app
```
```shell
docker run --rm -it my_python_app bash
```
```shell
docker run --rm -v "$(pwd)"/data:/code/data my_python_app
docker run --rm -it -v "$(pwd)"/data:/code/data my_python_app bash
```
## docker-compose
```shell
docker-compose build
docker-compose up
docker-compose down
```
Rename the `env_file_sample` to `.env`
```shell
docker-compose -f plus-postgres.docker-compose.yml build my_python_app_dc

docker-compose -f plus-postgres.docker-compose.yml up pgdatabase
docker-compose -f plus-postgres.docker-compose.yml up my_python_app_dc
docker-compose -f plus-postgres.docker-compose.yml down
```
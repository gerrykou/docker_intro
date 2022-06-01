# docker_intro
Introduction to Docker   

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
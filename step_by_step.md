# Step by step docker intro

[Install docker on your machine](https://docs.docker.com/get-docker/)

## Running containers from docker hub image library

[Docker hub](https://hub.docker.com/search?q=)
```shell
docker run --rm -it ubuntu bin/bash   
```
This command 
1. Downloads locally the `ubuntu` docker image  
2. Runs a container in an interactive mode ,by using the `-it` flag  
3. Starts the `bash` inside the `ubuntu` container
4. `--rm` will remove the container when the container exits  

Run `exit` to exit from `bash`  

Running `docker images` returns your local images. You should be able to see the `ubuntu` image.  

Running `docker ps` will return the running containers, chances are there are no containers running. The container has been removed after `exit` since you used `--rm`.

Running this, will download a `python:latest` image and run a container from this image.
```shell
docker run --rm -it python
```
Great, you can run a python command now, 
```python
import time
print(f'Hello World! {time.ctime()}')
```
Well, you are right, the container uses UTC as time zone.  
Type `quit()` , the container stops and is being removed.

If you want to use a specific version of python, you have to specify it in the tag `:3.10.4-slim-bullseye`  
When a tag is not specified, the default tag is `:latest`  
You can find the available images and tags [here](https://hub.docker.com/_/python)  

```shell
docker run --rm -it python:3.10.4-slim-bullseye
```
In the next step will see how to build an image that runs our python code.  

## Dockerize your Python Code

We have our code in [src/app.py](src/app.py)  
The app.py code, uses 'datetime' and 'requests' library,  
prints the current time in local timezone and in UTC,  
downloads an html file, creates a data/ directory and save the html file.  
If you want to run it in your machine, 
- Create a virtual environment  
- Install the dependencies from requirements.txt file  
- Run the code  
Use `python3` for Linux, `python` for Windows
```shell
python3 -m venv env
python3 -m pip install -r requirements.txt
python3 src/app.py
```

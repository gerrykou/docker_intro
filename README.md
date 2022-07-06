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

Type `exit` to exit from `bash`  

Type `docker images` , returns your local images. You should be able to see the `ubuntu` image.  

Type `docker ps` , returns the running containers, chances are there are no containers running. The container has been removed after `exit` since you used `--rm`.

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

Have a look on the [Dockerfile](Dockerfile) and read the comments.  
To build your image you need to run `docker build .`  
The dot `.` means build the image based on the file called Dockerfile in the current directory.  
Is better to add a tag to your image using the `-t` flag
```shell
docker build -t my_python_app .
```
  
Great, now your image has a tag. If you type `docker images` your image should be on the list.  
Now you need to run a container based on your image.  

```shell
docker run --rm my_python_app
```
This should print the what is going on in the app, but i am pretty sure it didn't download anything in your `data/` folder.
The container is already gone, it has been removed when the job finished.  

There is a way to run a container and see what is going on inside the container. Use the `-it` flags  

```shell
docker run --rm -it my_python_app bash
```
Using `ls` and `cd` you can navigate inside the container and see the available files and folders.  
If you run the python script, you can see that the `data` folder has been created and the html file has been downloaded.  
Type `exit` and the container is gone again.  

Read more about the interactive mode from the [documentation](https://docs.docker.com/engine/reference/run/#foreground)

## Share Local Volume with Container

To share you local volume with a container you will use the `-v` flag.  
`-v  ` `<path to local directory> : <path to container's directory>`  
```shell
docker run --rm -v "$(pwd)"/data:/code/data my_python_app
```
Now you can see that the container creates the `data` directory and downloads the html file.  
If you want to investigate what is going inside the container, run this:
```shell
docker run --rm -it -v "$(pwd)"/data:/code/data my_python_app bash
```
Read more from the [documentation](https://docs.docker.com/storage/)

## Run your image with Docker Compose

Open the [docker-compose.yml](docker-compose.yml) file  
As you can see, we specify a name for our service `my_python_app`  
We specify a name for our container `my_python_app_dc`  
The dot `.` next to `build` means use the `Dockerfile` that is in the current directory.  
And we also specify the volumes.  
Type `docker-compose build` to build your image.  
Type `docker-compose up` to run your services - containers, here is the `my_python_app_dc` container.  
Type `docker-compose down` to remove your services - containers.  

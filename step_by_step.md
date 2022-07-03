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

Running `docker ps` will return the running containers, chances are there are no containers running.

```shell
docker run --rm -it python
```
**Workshop 2 Demo steps**

1. Create VM
2. Update and install Docker

```shell
$ sudo apt-get update
$ sudo apt-get install docker.io
```

3. Check Docker is running

```shell
 $ sudo systemctl status docker
```

4. Create a new user called docker-user. 

```shell
$ sudo adduser docker-user
```

5. We will need to give `sudo` access to our new `docker-user`, so let's add it to the `sudo` group.

```shell
$ sudo usermod -aG sudo docker-user
```

6. Now, run the following command; this will allow us to give `sudo` permissions to docker to run our commands. 

```shell
$ sudo usermod -aG docker docker-user
```

7. Switch to docker-user home

```shell
$ su - docker-user
```

8. Run hello world

```shell
$ docker run hello-world
```

9. Run ubuntu container

```shell
$ docker search ubuntu

$ docker pull ubuntu

$ docker images

$ docker ps -all

$ docker rm ID

$ docker run -it --name mini-ubuntu ubuntu
```

10. Attach to running container

```shell
$ docker exec -it mini-ubuntu /bin/bash 

$ docker stop mini-ubuntu

$ docker rm mini-ubuntu
```

11. Run Python container

```shell
$ docker search python

$ docker run --name mini-python-container -it python

>>> print('Hello World!')

>>> exit()

$ docker ps -a

$ docker start mini-python-container 

$ echo "print('Hello from mini-python-container')" > test.py

$ docker cp test.py mini-python-container:/home

$ docker exec -it  mini-python-container python /home/test.py
```

12. Create DockerFile

```dockerfile
pico Dockerfile

FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install software-properties-common -y
RUN apt-get install python3.7 -y
ADD . /app
WORKDIR /app
CMD ["python3", "test.py"]
```

13. Build-Run

```shell
$ docker build -f Dockerfile . -t mini-python3-image

$ docker run --name test-python3-container -it mini-python3-image /bin/bash
```


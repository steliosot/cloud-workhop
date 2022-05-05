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
> Note: exit without stopping the container pressing

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
$ pico Dockerfile

FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install software-properties-common -y
RUN apt-get install python3 -y
ADD . /app
WORKDIR /app
CMD ["python3", "test.py"]
```

13. Build-Run

```shell
$ docker build -f Dockerfile . -t mini-python3-image

$ docker run --name test-python3-container -it mini-python3-image /bin/bash
```

14. Stop and remove the container

```shell
$ docker stop test-python3-container
$ docker rm test-python3-container
```

15. Create a new folder and enter on it

```shell
$ mkdir mydata
$ cd mydata
```

16. Create a new text file `file.txt` as follows.

```tex
Two households, both alike in dignity,
In fair Verona, where we lay our scene,
From ancient grudge break to new mutiny,
Where civil blood makes civil hands unclean.
From forth the fatal loins of these two foes
A pair of star-cross'd lovers take their life;
Whose misadventured piteous overthrows
Do with their death bury their parents' strife.
The fearful passage of their death-mark'd love,
And the continuance of their parents' rage,
Which, but their children's end, nought could remove
Is now the two hours' traffic of our stage;
The which if you with patient ears attend,
What here shall miss, our toil shall strive to mend.
```

17. Create a word counter in Python called `count.py`.

```python
file = open('file.txt', 'r')
read_data = file.read()
per_word = read_data.split()

print('Total Words:', len(per_word))
```

18. Create a docker file and run the script.

```dockerfile
$ pico Dockerfile

FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install software-properties-common -y
RUN apt-get install python3.7 -y
ADD . /app
WORKDIR /app
CMD ["python3", "count.py"]
```

19. Build-Run

```shell
$ docker build -f Dockerfile . -t mini-python3-2-image

$ docker run --name test-python3-2-container -it mini-python3-2-image /bin/bash
```
20. Stop and delete the container, then run it using the cli.

```shell
docker run --name test-python3-2-container -it mini-python3-2-image
```

Well done! :checkered_flag:

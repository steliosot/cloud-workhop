**Demo steps**

1. Visit [Docker Hub](https://hub.docker.com) and create account/login
2.  Create a new public repo:
* Add name
* Add description
* Public
* **Create**
3. Go to GCP and create a VM and install Docker (run the commands)

```shell
$ sudo apt-get update
$ sudo apt-get install docker.io
$ sudo adduser docker-user
$ sudo usermod -aG sudo docker-user
$ sudo usermod -aG docker docker-user
$ su - docker-user
```

4. Login to Docker (connect to docker hub)

```shell
$ docker login -u <docker_hub_username>
```

5. Clone a Node.js Repo

```shell
$ git clone https://github.com/steliosot/mini-hi.git
```

6. Enter the folder

```shell
$ cd mini-hi
```

7. Print the content of the`app.js` using the `cat` command.

```shell
$ cat app.js
```

8. Examine the Dockerfile (`cat`)

```shell
$ cat Dockerfile
```

9. Build image

```shell
$ docker build -t <steliosot/mini-hi:v1> .
```

10. Push image to Docker Hub.

```shell
$ docker push <steliosot/mini-hi:v1>
```

11. Check the Docker Hub interface
12. Search the public docker image

```shell
$ docker search <username>/<image_name> 
```

13. Now, search an image of another student
14. Go to GCP and visit GKE
15. Create your cluster
    * Enable API
    * click GKE standard
    * select a name: `workshop-gke`
    * Deploy 3 nodes (default)
    * Click create and wait...
16. Connect to the cluser using the Cloud Shell

```shell
$ gcloud container clusters get-credentials <cluster-name> --zone us-central1-c --project <project-id>

```

17. Get nodes

```shell
$ kubectl get nodes
```

18. Get cluster info

```shell
$ kubectl cluster-info
```

19. Run the container

```shell
$ kubectl run mini-hi-pod --image=steliosot/mini-hi:v1
```

20. Check if running

```shell
$ kubectl get deployments
```

or 

```shell
$ kubectl get pods
```

21. Describe / get pod's info 

```shell
$ kubectl describe pods
```

or

```shell
$ kubectl describe pods <pod_name>
```

22. Create a deployment file

* Name: `pico mini-hi-deployment.yaml`
* Edit the file and adjust your image name

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mini-hi-deployment
  labels:
    app: minihi 
spec:
  replicas: 3
  selector:
    matchLabels:
      app: minihi
  template:
    metadata:
      labels:
        app: minihi
    spec:
      containers:
      - name: minihi
        image: <YOUR_IMAGE_NAME>
        imagePullPolicy: Always
        ports:
        - containerPort: 3000
```

23. Delete your current pods

```shell
$ kubectl delete pods mini-hi-pod
```

24. Apply deployment

```shell
$ kubectl apply -f mini-hi-deployment.yaml
```

25. Get pods

```shell
$ kubectl get pods
```

26. Let's increase our pods. I need **ten** more, so `replicas:10`! Let's edit the `mini-hi-deployments.yaml` and replace `replicas:3`with `replicas:10`.

```shell
$ kubectl apply -f mini-hi-deployment.yaml
```

27. Get pods once more

```shell
$ kubectl get pods
```

28. Try the `wide` option

```shell
$ kubectl get pods -o wide
```

29. Create a load balancer, a new `mini-hi-service.yaml`

```shell
apiVersion: v1
kind: Service
metadata:
  name: mini-hi-service
  labels:
    app: mini-hi-service
spec:
  type: LoadBalancer
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 3000
  selector:
    app: minihi
  sessionAffinity: None
```

30. Apply the deployment

```shell
$ kubectl apply -f mini-hi-service.yaml
```

31. Get services

```shell
$ kubectl get services
```

32. Visit the `EXTERNAL-IP` URL

33. Edit the code to change the message (version 2)
34. Build the new image version

```shell
$ docker build -t <dockerhub-username>/<image-name>:<version> .
```

33. Push image to the Docker hub

```shell
$ docker push <dockerhub-username>/<image-name:<version>
```

34. Visit the Docker Hub platform
35. Edit deployment file to set the new updated image version

```shell
$ pico mini-hi-deployment.yaml
```

36. Apply deployments

```shell
$ kubectl apply -f mini-hi-deployment.yaml
```

37. Refresh your page!

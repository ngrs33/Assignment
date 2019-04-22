Initial Task Descriptions:
1. Create a kubernetes cluster without using minikube

2. Run a simple hello world application on the cluster

3. Add a load balancer of your choosing to route on the application

4. Create a simple app that prints the ingress and egress rules using the kubernetes api and a language of your choosing

Next I asked for below Clarifications: 
1. I need to know on what virtual machines I shoul be creating the above k8s cluster

Response for my clarifications:
“He can send us the code snippets for the ingress rules engine and rest of the stuff he can send the screen shots.  He can create the entire demo on his laptop and give us a demo during the interview.”

Below is my Final Work items for the above Tasks
1. Created a k8s cluster with two VMs and the file Createk8sCluster has the detailed steps that I followed to create the cluster

2. Ran two sample applications hello.yml and howdy.yml which has REST endpoints to print "Hello world" & "Howdy Partner"
        kubectl apply -f hello.yaml
kubectl port-forward hello-app 3000:5678
curl -kL http://127.0.0.1:3000/hello

        kubectl apply -f howdy.yaml
kubectl port-forward howdy-app 6000:5678
curl -kL http://127.0.0.1:6000/howdy

#Start another pod with busybox+curl and issue curl for each service
kubectl run busybox --rm -ti --image=yauritux/busybox-curl /bin/sh
/home # curl -kL http://hello-service:5678
hello world
/home # curl -kL http://howdy-service:5678
howdy partner

3. Used the generic nginx-Ingress-controller and ran it as load balancer and also to route the APIs from different services through a single backend ingress service
	kubectl apply -f mandatory.yaml
	kubectl apply -f cloud-generic.yaml
	kubectl create -f ingress.yaml
Now API calls can be routed through the single ingrss-nginx service
	curl -kL http://ingress-nginx/howdy
	curl -kL http://ingress-nginx/hello
	              OR
	curl -kL http://10.96.3.39/howdy
	curl -kL http://10.96.3.39/hello

4. Have a Python based code to access the list of pods from my kubenetes cluster for default namespace
        list_pods.py
osboxes@k8s-ubuntu-master:~/exps$ python3 list_pods.py
/home/osboxes/.local/lib/python3.5/site-packages/requests/__init__.py:91: RequestsDependencyWarning: urllib3 (1.25) or chardet (3.0.4) doesn't match a supported version!
  RequestsDependencyWarning)
hello-app       Running 10.40.0.1
howdy-app       Running 10.40.0.2
coredns-fb8b8dccf-dls4m Running 10.32.0.4
coredns-fb8b8dccf-rnxls Running 10.32.0.5
etcd-k8s-ubuntu-master  Running 172.16.211.186
kube-apiserver-k8s-ubuntu-master        Running 172.16.211.186
kube-controller-manager-k8s-ubuntu-master       Running 172.16.211.186
kube-proxy-2dldg        Running 172.16.211.185
kube-proxy-cxp8r        Running 172.16.211.186
kube-scheduler-k8s-ubuntu-master        Running 172.16.211.186
weave-net-gkq24 Running 172.16.211.185
weave-net-h962f Running 172.16.211.186


5. Create a Network policy that says hell-service can only be accessed from pods with label hello 
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: access-to-hello
spec:
  podSelector:
    matchLabels:
      app: hello
  ingress:
  - from:
    - podSelector:
        matchLabels:
          access: "hello"
5a. kubectl apply -f access-to-hello.yaml

5b. #verify that a normal pod cannot access hello-service but it can still access howdy-service
kubectl run busybox --rm -ti --image=yauritux/busybox-curl /bin/sh
/home # curl -vkL http://hello-service:5678
* About to connect() to hello-service port 5678 (#0)
*   Trying 10.104.198.12...
* Adding handle: conn: 0x11a75b88
* Adding handle: send: 0
* Adding handle: recv: 0
* Curl_addHandleToPipeline: length: 1
* - Conn 0 (0x11a75b88) send_pipe: 1, recv_pipe: 0


^C
/home # curl -vkL http://howdy-service:5678
* About to connect() to howdy-service port 5678 (#0)
*   Trying 10.98.209.141...
* Adding handle: conn: 0x1137db88
* Adding handle: send: 0
* Adding handle: recv: 0
* Curl_addHandleToPipeline: length: 1
* - Conn 0 (0x1137db88) send_pipe: 1, recv_pipe: 0
* Connected to howdy-service (10.98.209.141) port 5678 (#0)
> GET / HTTP/1.1
> User-Agent: curl/7.30.0
> Host: howdy-service:5678
> Accept: */*
>
< HTTP/1.1 200 OK
< X-App-Name: http-echo
< X-App-Version: 0.2.3
< Date: Mon, 22 Apr 2019 18:58:08 GMT
< Content-Length: 14
< Content-Type: text/plain; charset=utf-8
<
howdy partner

5c.#verify that a pod started with acces: "hello" label can reach hello-service and also howdy-service
osboxes@k8s-ubuntu-master:~/exps$ kubectl run busybox --rm -ti --labels="access=hello" --image=yauritux/busybox-curl /bin/sh
kubectl run --generator=deployment/apps.v1 is DEPRECATED and will be removed in a future version. Use kubectl run --generator=run-pod/v1 or kubectl create instead.
If you don't see a command prompt, try pressing enter.
/home # curl -vkL http://howdy-service:5678
* About to connect() to howdy-service port 5678 (#0)
*   Trying 10.98.209.141...
* Adding handle: conn: 0x10200b88
* Adding handle: send: 0
* Adding handle: recv: 0
* Curl_addHandleToPipeline: length: 1
* - Conn 0 (0x10200b88) send_pipe: 1, recv_pipe: 0
* Connected to howdy-service (10.98.209.141) port 5678 (#0)
> GET / HTTP/1.1
> User-Agent: curl/7.30.0
> Host: howdy-service:5678
> Accept: */*
>
< HTTP/1.1 200 OK
< X-App-Name: http-echo
< X-App-Version: 0.2.3
< Date: Mon, 22 Apr 2019 19:03:16 GMT
< Content-Length: 14
< Content-Type: text/plain; charset=utf-8
<
howdy partner
* Connection #0 to host howdy-service left intact
/home # curl -vkL http://hello-service:5678
* About to connect() to hello-service port 5678 (#0)
*   Trying 10.104.198.12...
* Adding handle: conn: 0x107a3b88
* Adding handle: send: 0
* Adding handle: recv: 0
* Curl_addHandleToPipeline: length: 1
* - Conn 0 (0x107a3b88) send_pipe: 1, recv_pipe: 0
* Connected to hello-service (10.104.198.12) port 5678 (#0)
> GET / HTTP/1.1
> User-Agent: curl/7.30.0
> Host: hello-service:5678
> Accept: */*
>
< HTTP/1.1 200 OK
< X-App-Name: http-echo
< X-App-Version: 0.2.3
< Date: Mon, 22 Apr 2019 19:03:26 GMT
< Content-Length: 12
< Content-Type: text/plain; charset=utf-8
<
hello world
* Connection #0 to host hello-service left intact

5e. Using kubectl command check all network policies hat you have defined
osboxes@k8s-ubuntu-master:~/exps$ kubectl describe netpol access-to-hello
Name:         access-to-hello
Namespace:    default
Created on:   2019-04-22 13:55:32 -0500 CDT
Labels:       <none>
Annotations:  kubectl.kubernetes.io/last-applied-configuration:
                {"apiVersion":"networking.k8s.io/v1","kind":"NetworkPolicy","metadata":{"annotations":{},"name":"access-to-hello","namespace":"default"},"...
Spec:
  PodSelector:     app=hello
  Allowing ingress traffic:
    To Port: <any> (traffic allowed to all ports)
    From:
      PodSelector: access=hello
  Allowing egress traffic:
    <none> (Selected pods are isolated for egress connectivity)
  Policy Types: Ingress



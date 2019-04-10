Initial Task Descriptions:
1. Create a kubernetes cluster without using minikube

2. Run a simple hello world application on the cluster

3. Add a load balancer of your choosing to route on the application

4. Create a simple app that prints the ingress and egress rules using the kubernetes api and a language of your choosing

Next I asked for below Clarifications: 
1. I need to know on what virtual machines I shoul be creating the above k8s cluster

Response for my clarifications:
“He can send us the code snippets for the ingress rules engine and rest of the stuff he can send the screen shots.  He can create the entire demo on his laptop and give us a demo later.”

Below is my Final Work items for the above Tasks
1. Created a k8s cluster with two VMs and the file Createk8sCluster has the detailed steps that I followed to create the cluster
2. Ran two sample applications hello.yml and howdy.yml which has REST endpoints to print "Hello world" & "Howdy Partner"
        kubectl apply -f hello.yaml
        kubectl apply -f howdy.yaml
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
5. Still working on the code to get the Ingress and Egress rules of a Network policy..



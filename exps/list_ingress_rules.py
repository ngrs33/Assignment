import os
import urllib3
from kubernetes import client, config

config.load_kube_config(
    os.path.join(os.environ["HOME"], '/home/ubuntu/.kube/config'))

v1 = client.ExtensionsV1beta1Api()
urllib3.disable_warnings()
ingress_list = v1.list_namespaced_ingress("default")
for ingress in ingress_list.items:
    print("%s" % (ingress.metadata.name))


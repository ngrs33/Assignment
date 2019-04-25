import os
import urllib3
from kubernetes import client, config
from pprint import pprint

config.load_kube_config(
    os.path.join(os.environ["HOME"], '/home/osboxes/.kube/config'))

v1 = client.ExtensionsV1beta1Api()
urllib3.disable_warnings()
net_pol_list = v1.list_network_policy_for_all_namespaces()
pprint(net_pol_list)
for net_pol in net_pol_list.items:
    print("%s" % (net_pol.metadata.name))

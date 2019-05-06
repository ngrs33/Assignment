import os
import urllib3
from kubernetes import client, config
from pprint import pprint

def main():
    # Load the client configurations
    config.load_kube_config(os.path.join(os.environ["HOME"], '/home/osboxes/.kube/config'))

    # Get network policys from all namespaces
    try:
        v1 = client.ExtensionsV1beta1Api()
        net_pol_list = v1.list_network_policy_for_all_namespaces()
        pprint(net_pol_list)
        for net_pol in net_pol_list.items:
            print("Name: %s" % (net_pol.metadata.name))
            print("Ingress Rules: %s" % (net_pol.spec.ingress))
            print("Egress Rules: %s" % (net_pol.spec.egress))
    except ApiExceptio as e:
        print("Exception Occured when calling list_network_policy_for_all_namespaces: %s\n" % e)

if __name__ == '__main__':
    main()


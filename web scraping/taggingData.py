import openai
import pandas as pd
from tqdm import tqdm
from dotenv import load_dotenv
import os 
# Load environment variables from .env file
load_dotenv()

# Load CSV file
csv_path = "kd.csv"  # Update with actual path
df = pd.read_csv(csv_path)

# Predefined list of valid tags
TAG_LIST = [
    "google-kubernetes-engine", "kubernetes-helm", "kubectl", "kubernetes-ingress",
    "amazon-eks", "kubernetes-pod", "Kubernetes-service", "kubernetes-secrets",
    "kubernetes-statefulset", "kubernetes-pvc", "kubernetes-deployment",
    "kubernetes-cronjob", "kubernetes-apiserver", "kubernetes-networkpolicy",
    "kubernetes-custom-resources", "kubernetes-security", "kubernetes-operator",
    "kubernetes-go-client", "kubernetes-networking", "kubernetes-rbac"
]

# OpenAI API Key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Initalize the client

# Initialize OpenAI client
client = openai.OpenAI(api_key= os.environ["OPENAI_API_KEY"])

# Few-shot examples for GPT-4 to learn from
EXAMPLES = """
Examples:

1. Category: Kubernetes
   Topic: Container Runtimes
   Concept: Container runtimes
   Content: Note: This section links to third party projects that provide functionality required by Kubernetes.
The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically.
To add a project to this list, read the content guide  before submitting a change.
More information.
 containerd This section outlines the necessary steps to use containerd as CRI runtime.
To install containerd on your system, follow the instructions on getting started with containerd .
Return to this step once you've created a valid

config.toml

configuration file.
Linux  Windows  You can find this file under the path

/etc/containerd/config.toml

.
You can find this file under the path

C:\Program Files\containerd\config.toml

.
On Linux the default CRI socket for containerd is

/run/containerd/containerd.sock

.
On Windows the default CRI endpoint is

npipe://./pipe/containerd-containerd

.
Configuring the systemd cgroup driver To use the systemd cgroup driver in

/etc/containerd/config.toml

with runc, set

[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]
  ...
  [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
    SystemdCgroup = true

The systemd cgroup driver is recommended if you use cgroup v2 .
Note: If you installed containerd from a package (for example, RPM or

.deb

), you may find that the CRI integration plugin is disabled by default.
You need CRI support enabled to use containerd with Kubernetes.
Make sure that cri is not included in thedisabled_plugins list within

/etc/containerd/config.toml

; if you made changes to that file, also restart containerd.
If you experience container crash loops after the initial cluster installation or after installing a CNI, the containerd configuration provided with the package might contain incompatible configuration parameters.
Consider resetting the containerd configuration with

containerd config default &gt; /etc/containerd/config.toml

as specified in getting-started.md  and then set the configuration parameters specified above accordingly.
If you apply this change, make sure to restart containerd:

sudo systemctl restart containerd

When using kubeadm, manually configure the cgroup driver for kubelet .
In Kubernetes v1.28, you can enable automatic detection of the cgroup driver as an alpha feature.
See systemd cgroup driver  for more details.
Overriding the sandbox (pause) image In your containerd config  you can overwrite the sandbox image by setting the following config:

[plugins."io.containerd.grpc.v1.cri"]
  sandbox_image = "registry.k8s.io/pause:3.10"

You might need to restart containerd as well once you've updated the config file:

systemctl restart containerd

.
CRI-O This section contains the necessary steps to install CRI-O as a container runtime.
To install CRI-O, follow CRI-O Install Instructions .
cgroup driver CRI-O uses the systemd cgroup driver per default, which is likely to work fine for you.
To switch to the cgroupfs cgroup driver, either edit

/etc/crio/crio.conf

or place a drop-in configuration in

/etc/crio/crio.conf.d/02-cgroup-manager.conf

, for example:

[crio.runtime]
conmon_cgroup = "pod"
cgroup_manager = "cgroupfs"

You should also note the changed conmon_cgroup, which has to be set to the value pod when using CRI-O with cgroupfs.
It is generally necessary to keep the cgroup driver configuration of the kubelet (usually done via kubeadm) and CRI-O in sync.
In Kubernetes v1.28, you can enable automatic detection of the cgroup driver as an alpha feature.
See systemd cgroup driver  for more details.
For CRI-O, the CRI socket is

/var/run/crio/crio.sock

by default.
Overriding the sandbox (pause) image In your CRI-O config  you can set the following config value:

[crio.image]
pause_image="registry.k8s.io/pause:3.10"

This config option supports live configuration reload to apply this change:

systemctl reload crio

or by sending SIGHUP to the crio process.
Docker Engine Note: These instructions assume that you are using the cri-dockerd  adapter to integrate Docker Engine with Kubernetes.
On each of your nodes, install Docker for your Linux distribution as per Install Docker Engine .
Install cri-dockerd , following the directions in the install section of the documentation.
For cri-dockerd, the CRI socket is

/run/cri-dockerd.sock

by default.
Mirantis Container Runtime Mirantis Container Runtime  (MCR) is a commercially available container runtime that was formerly known as Docker Enterprise Edition.
You can use Mirantis Container Runtime with Kubernetes using the open source cri-dockerd  component, included with MCR.
To learn more about how to install Mirantis Container Runtime, visit MCR Deployment Guide .
Check the systemd unit named

cri-docker.socket

to find out the path to the CRI socket.
Overriding the sandbox (pause) image The cri-dockerd adapter accepts a command line argument for specifying which container image to use as the Pod infrastructure container (“pause image”).
The command line argument to use is --pod-infra-container-image.
========================================
   → Correct Tag: kubectl

2. Category: Kubernetes
   Topic: Ingress Controllers
   Concept: Additional controllers
   Content: Note: This section links to third party projects that provide functionality required by Kubernetes.
The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically.
To add a project to this list, read the content guide  before submitting a change.
More information.
 AKS Application Gateway Ingress Controller  is an ingress controller that configures the Azure Application Gateway .
Alibaba Cloud MSE Ingress  is an ingress controller that configures the Alibaba Cloud Native Gateway , which is also the commercial version of Higress .
Apache APISIX ingress controller  is an Apache APISIX -based ingress controller.
Avi Kubernetes Operator  provides L4-L7 load-balancing using VMware NSX Advanced Load Balancer .
BFE Ingress Controller  is a BFE -based ingress controller.
Cilium Ingress Controller  is an ingress controller powered by Cilium .
The Citrix ingress controller  works with Citrix Application Delivery Controller.
Contour  is an Envoy  based ingress controller.
Emissary-Ingress  API Gateway is an Envoy -based ingress controller.
EnRoute  is an Envoy  based API gateway that can run as an ingress controller.
Easegress IngressController  is an Easegress  based API gateway that can run as an ingress controller.
F5 BIG-IP Container Ingress Services for Kubernetes  lets you use an Ingress to configure F5 BIG-IP virtual servers.
FortiADC Ingress Controller  support the Kubernetes Ingress resources and allows you to manage FortiADC objects from Kubernetes Gloo  is an open-source ingress controller based on Envoy , which offers API gateway functionality.
HAProxy Ingress  is an ingress controller for HAProxy .
Higress  is an Envoy  based API gateway that can run as an ingress controller.
The HAProxy Ingress Controller for Kubernetes  is also an ingress controller for HAProxy .
Istio Ingress  is an Istio  based ingress controller.
The Kong Ingress Controller for Kubernetes  is an ingress controller driving Kong Gateway .
Kusk Gateway  is an OpenAPI-driven ingress controller based on Envoy .
The NGINX Ingress Controller for Kubernetes  works with the NGINX  webserver (as a proxy).
The ngrok Kubernetes Ingress Controller  is an open source controller for adding secure public access to your K8s services using the ngrok platform .
The OCI Native Ingress Controller  is an Ingress controller for Oracle Cloud Infrastructure which allows you to manage the OCI Load Balancer .
OpenNJet Ingress Controller  is a OpenNJet -based ingress controller.
The Pomerium Ingress Controller  is based on Pomerium , which offers context-aware access policy.
Skipper  HTTP router and reverse proxy for service composition, including use cases like Kubernetes Ingress, designed as a library to build your custom proxy.
The Traefik Kubernetes Ingress provider  is an ingress controller for the Traefik  proxy.
Tyk Operator  extends Ingress with Custom Resources to bring API Management capabilities to Ingress.
Tyk Operator works with the Open Source Tyk Gateway & Tyk Cloud control plane.
Voyager  is an ingress controller for HAProxy .
Wallarm Ingress Controller  is an Ingress Controller that provides WAAP (WAF) and API Security capabilities.
========================================
   → Correct Tag: kubernetes-ingress

3. Category: Kubernetes
   Topic: Network Policies
   Concept: Default policies
   Content: By default, if no policies exist in a namespace, then all ingress and egress traffic is allowed to and from pods in that namespace.
The following examples let you change the default behavior in that namespace.
Default deny all ingress traffic You can create a "default" ingress isolation policy for a namespace by creating a NetworkPolicy that selects all pods but does not allow any ingress traffic to those pods.
service/networking/network-policy-default-deny-ingress.yaml 

---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
spec:
  podSelector: {}
  policyTypes:
  - Ingress

This ensures that even pods that aren't selected by any other NetworkPolicy will still be isolated for ingress.
This policy does not affect isolation for egress from any pod.
Allow all ingress traffic If you want to allow all incoming connections to all pods in a namespace, you can create a policy that explicitly allows that.
service/networking/network-policy-allow-all-ingress.yaml 

---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-all-ingress
spec:
  podSelector: {}
  ingress:
  - {}
  policyTypes:
  - Ingress

With this policy in place, no additional policy or policies can cause any incoming connection to those pods to be denied.
This policy has no effect on isolation for egress from any pod.
Default deny all egress traffic You can create a "default" egress isolation policy for a namespace by creating a NetworkPolicy that selects all pods but does not allow any egress traffic from those pods.
service/networking/network-policy-default-deny-egress.yaml 

---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-egress
spec:
  podSelector: {}
  policyTypes:
  - Egress

This ensures that even pods that aren't selected by any other NetworkPolicy will not be allowed egress traffic.
This policy does not change the ingress isolation behavior of any pod.
Allow all egress traffic If you want to allow all connections from all pods in a namespace, you can create a policy that explicitly allows all outgoing connections from pods in that namespace.
service/networking/network-policy-allow-all-egress.yaml 

---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-all-egress
spec:
  podSelector: {}
  egress:
  - {}
  policyTypes:
  - Egress

With this policy in place, no additional policy or policies can cause any outgoing connection from those pods to be denied.
This policy has no effect on isolation for ingress to any pod.
Default deny all ingress and all egress traffic You can create a "default" policy for a namespace which prevents all ingress AND egress traffic by creating the following NetworkPolicy in that namespace.
service/networking/network-policy-default-deny-all.yaml 

---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress

This ensures that even pods that aren't selected by any other NetworkPolicy will not be allowed ingress or egress traffic.
========================================
   → Correct Tag: kubernetes-networking

4. Category: Kubernetes
   Topic: Topology Aware
   Concept: How It Works
   Content: The "Auto" heuristic attempts to proportionally allocate a number of endpoints to each zone.
Note that this heuristic works best for Services that have a significant number of endpoints.
EndpointSlice controller The EndpointSlice controller is responsible for setting hints on EndpointSlices when this heuristic is enabled.
The controller allocates a proportional amount of endpoints to each zone.
This proportion is based on the allocatable  CPU cores for nodes running in that zone.
For example, if one zone had 2 CPU cores and another zone only had 1 CPU core, the controller would allocate twice as many endpoints to the zone with 2 CPU cores.
The following example shows what an EndpointSlice looks like when hints have been populated:

apiVersion: discovery.k8s.io/v1
kind: EndpointSlice
metadata:
  name: example-hints
  labels:
    kubernetes.io/service-name: example-svc
addressType: IPv4
ports:
  - name: http
    protocol: TCP
    port: 80
endpoints:
  - addresses:
      - "10.1.2.3"
    conditions:
      ready: true
    hostname: pod-1
    zone: zone-a
    hints:
      forZones:
        - name: "zone-a"

kube-proxy The kube-proxy component filters the endpoints it routes to based on the hints set by the EndpointSlice controller.
In most cases, this means that the kube-proxy is able to route traffic to endpoints in the same zone.
Sometimes the controller allocates endpoints from a different zone to ensure more even distribution of endpoints between zones.
This would result in some traffic being routed to other zones.
========================================
   → Correct Tag: kubernetes-apiserver
5. Category: Kubernetes
    Topic: Service ClusterIP allocation
    Concept:Why do you need to reserve Service Cluster IPs?
    Content:Sometimes you may want to have Services running in well-known IP addresses, so other components and users in the cluster can use them.
The best example is the DNS Service for the cluster.
As a soft convention, some Kubernetes installers assign the 10th IP address from the Service IP range to the DNS service.
Assuming you configured your cluster with Service IP range 10.96.0.0/16 and you want your DNS Service IP to be 10.96.0.10, you'd have to create a Service like this:

apiVersion: v1
kind: Service
metadata:
  labels:
    k8s-app: kube-dns
    kubernetes.io/cluster-service: "true"
    kubernetes.io/name: CoreDNS
  name: kube-dns
  namespace: kube-system
spec:
  clusterIP: 10.96.0.10
  ports:
  - name: dns
    port: 53
    protocol: UDP
    targetPort: 53
  - name: dns-tcp
    port: 53
    protocol: TCP
    targetPort: 53
  selector:
    k8s-app: kube-dns
  type: ClusterIP

But, as it was explained before, the IP address 10.96.0.10 has not been reserved.
If other Services are created before or in parallel with dynamic allocation, there is a chance they can allocate this IP.
Hence, you will not be able to create the DNS Service because it will fail with a conflict error.
========================================
    → Correct Tag:kubernetes-networkpolicy

6. Category: Kubernetes
    Topic: Storage Classes
    Concept: Allowed topologies
    Content: When a cluster operator specifies the WaitForFirstConsumer volume binding mode, it is no longer necessary to restrict provisioning to specific topologies in most situations.
However, if still required, allowedTopologies can be specified.
This example demonstrates how to restrict the topology of provisioned volumes to specific zones and should be used as a replacement for the zone and zones parameters for the supported plugins.
storage/storageclass/storageclass-topology.yaml 

apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: standard
provisioner:  example.com/example
parameters:
  type: pd-standard
volumeBindingMode: WaitForFirstConsumer
allowedTopologies:
- matchLabelExpressions:
  - key: topology.kubernetes.io/zone
    values:
    - us-central-1a
    - us-central-1b

========================================
    → Correct Tag: kubernetes-pvc

7. Category: Kubernetes
    Topic: ConfigMaps
    Concept: Using ConfigMaps
    Content:"ConfigMaps can be mounted as data volumes.
ConfigMaps can also be used by other parts of the system, without being directly exposed to the Pod.
For example, ConfigMaps can hold data that other parts of the system should use for configuration.
The most common way to use ConfigMaps is to configure settings for containers running in a Pod in the same namespace.
You can also use a ConfigMap separately.
For example, you might encounter addons  or operators  that adjust their behavior based on a ConfigMap.
Using ConfigMaps as files from a Pod To consume a ConfigMap in a volume in a Pod: Create a ConfigMap or use an existing one.
Multiple Pods can reference the same ConfigMap.
Modify your Pod definition to add a volume under

.spec.volumes[]

.
Name the volume anything, and have a

.spec.volumes[].configMap.name

field set to reference your ConfigMap object.
Add a

.spec.containers[].volumeMounts[]

to each container that needs the ConfigMap.
Specify

.spec.containers[].volumeMounts[].readOnly = true

and

.spec.containers[].volumeMounts[].mountPath

to an unused directory name where you would like the ConfigMap to appear.
Modify your image or command line so that the program looks for files in that directory.
Each key in the ConfigMap data map becomes the filename under mountPath.
This is an example of a Pod that mounts a ConfigMap in a volume:

apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: redis
    volumeMounts:
    - name: foo
      mountPath: ""/etc/foo""
      readOnly: true
  volumes:
  - name: foo
    configMap:
      name: myconfigmap

Each ConfigMap you want to use needs to be referred to in

.spec.volumes

.
If there are multiple containers in the Pod, then each container needs its own volumeMounts block, but only one

.spec.volumes

is needed per ConfigMap.
Mounted ConfigMaps are updated automatically When a ConfigMap currently consumed in a volume is updated, projected keys are eventually updated as well.
The kubelet checks whether the mounted ConfigMap is fresh on every periodic sync.
However, the kubelet uses its local cache for getting the current value of the ConfigMap.
The type of the cache is configurable using the configMapAndSecretChangeDetectionStrategy field in the KubeletConfiguration struct .
A ConfigMap can be either propagated by watch (default), ttl-based, or by redirecting all requests directly to the API server.
As a result, the total delay from the moment when the ConfigMap is updated to the moment when new keys are projected to the Pod can be as long as the kubelet sync period + cache propagation delay, where the cache propagation delay depends on the chosen cache type (it equals to watch propagation delay, ttl of cache, or zero correspondingly).
ConfigMaps consumed as environment variables are not updated automatically and require a pod restart.
Note: A container using a ConfigMap as a subPath  volume mount will not receive ConfigMap updates.
Using Configmaps as environment variables To use a Configmap in an environment variable  in a Pod: For each container in your Pod specification, add an environment variable for each Configmap key that you want to use to the

env[].valueFrom.configMapKeyRef

field.
Modify your image and/or command line so that the program looks for values in the specified environment variables.
This is an example of defining a ConfigMap as a pod environment variable: The following ConfigMap (myconfigmap.yaml) stores two properties: username and access_level:

apiVersion: v1
kind: ConfigMap
metadata:
  name: myconfigmap
data:
  username: k8s-admin
  access_level: ""1""

The following command will create the ConfigMap object:

kubectl apply -f myconfigmap.yaml

The following Pod consumes the content of the ConfigMap as environment variables: configmap/env-configmap.yaml 

apiVersion: v1
kind: Pod
metadata:
  name: env-configmap
spec:
  containers:
    - name: app
      command: [""/bin/sh"", ""-c"", ""printenv""]
      image: busybox:latest
      envFrom:
        - configMapRef:
            name: myconfigmap

The envFrom field instructs Kubernetes to create environment variables from the sources nested within it.
The inner configMapRef refers to a ConfigMap by its name and selects all its key-value pairs.
Add the Pod to your cluster, then retrieve its logs to see the output from the printenv command.
This should confirm that the two key-value pairs from the ConfigMap have been set as environment variables:

kubectl apply -f env-configmap.yaml



kubectl logs pod/ env-configmap

The output is similar to this:

...
username: ""k8s-admin""
access_level: ""1""
...

Sometimes a Pod won't require access to all the values in a ConfigMap.
For example, you could have another Pod which only uses the username value from the ConfigMap.
For this use case, you can use the

env.valueFrom

syntax instead, which lets you select individual keys in a ConfigMap.
The name of the environment variable can also be different from the key within the ConfigMap.
For example:

apiVersion: v1
kind: Pod
metadata:
  name: env-configmap
spec:
  containers:
  - name: envars-test-container
    image: nginx
    env:
    - name: CONFIGMAP_USERNAME
      valueFrom:
        configMapKeyRef:
          name: myconfigmap
          key: username

In the Pod created from this manifest, you will see that the environment variable CONFIGMAP_USERNAME is set to the value of the username value from the ConfigMap.
Other keys from the ConfigMap data are not copied into the environment.
It's important to note that the range of characters allowed for environment variable names in pods is restricted .
If any keys do not meet the rules, those keys are not made available to your container, though the Pod is allowed to start.
========================================"
    -> Correct Tag: kubernetes-secrets
"""

# Function to generate a Kubernetes tag for each row
def generate_tag(row):    
    prompt = f"""
    You are an expert in Kubernetes and cloud-native classification. Your task is to **assign the most relevant tag** from the predefined list based on the provided structured information.

    ### **Tag Selection Criteria**
    1. **Analyze the provided entry carefully** and determine the most suitable classification.
    2. **Ensure the tag represents the overall subject**—not just a minor keyword.
    3. **Follow these structured elements** for context analysis:
       - **Category:** The high-level classification (e.g., Kubernetes, Cloud Networking, Security).
       - **Topic:** A more specific topic within the category (e.g., Storage Classes, Ingress Controllers).
       - **Concept:** The key feature or subject matter (e.g., Allowed Topologies, Role-Based Access Control).
       - **Content:** Typically a detailed description or example related to the concept.

    ### **Tag List (Choose Only One)**
    {", ".join(TAG_LIST)}

    {EXAMPLES}  # Injects few-shot examples

    ### **Classify the following entry:**
    - **Category**: {row['Category']}
    - **Topic**: {row['Topic']}
    - **Concept**: {row['Concept']}
    - **Content**: {row['Content']}
    
    **Respond with only one tag from the list above. Do not explain your answer.**
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert in Kubernetes classification."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1  # Lower temperature to make responses more deterministic
        )
        # Access the response content correctly
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error processing row {row.name}: {e}")
        return "unknown"


# Apply the function to all rows and generate tags
tqdm.pandas()
df["Tag"] = df.progress_apply(generate_tag, axis=1)

# Define output file path
output_path = "tagged_kubernetes_data.csv"

# Save the DataFrame to a CSV file
df.to_csv(output_path, index=False)

# Print output for easy copy-pasting into Google Sheets
print("\nGenerated Tags (Copy and Paste into Google Sheets):\n")
print("\n".join(df["Tag"]))

print(f"\nTagging complete. Tags saved to: {output_path}")





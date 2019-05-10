

[![Documentation Status](https://readthedocs.org/projects/ska-docker/badge/?version=latest)](https://developer.skatelescope.org/projects/k8s-integration/en/latest/?badge=latest)


SKA TANGO-controls docker images on Kubernetes
===========================

The following are a set of instructions of running the SKA TANGO-controls docker images made by SKAon Kubernetes, and has been tested on minikube v0.34.1 with k8s v1.13.3 on Ubuntu 18.04.

Minikube
========

Using [Minikube](https://kubernetes.io/docs/getting-started-guides/minikube/) enables us to create a single node stand alone Kubernetes cluster for testing purposes.  If you already have a cluster at your disposal, then you can skip forward to 'Running the SKA TANGO-controls docker images on Kubernetes'.

The generic installation instructions are available at https://kubernetes.io/docs/tasks/tools/install-minikube/.

Minikube requires the Kubernetes runtime, and a host virtualisation layer such as kvm, virtualbox etc.  Please refer to the drivers list at https://github.com/kubernetes/minikube/blob/master/docs/drivers.md .

On Ubuntu 18.04 for desktop based development, the most straight forward installation pattern is to go with the `none` driver as the host virtualisation layer.  CAUTION:  this will install Kubernetes directly on your host and will destroy any existing Kubernetes related configuration you already have (eg: /etc/kubernetes, /var/lib/kubelet, /etc/cni, ...).    This is technically called 'running with scissors', but the trade off in the authors opinion is lower virtualisation overheads and simpler management of storage integration including Xauthority details etc.

The latest version of minikube is found here  https://github.com/kubernetes/minikube/releases .  Scroll down to the section for Linux, which will have instructions like:
```
curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.34.1/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
```

Now we need to bootstrap minikube so that we have a running cluster based on kvm:
```
sudo -E minikube start --vm-driver=none --extra-config=kubelet.resolv-conf=/var/run/systemd/resolve/resolv.conf
```
This will take some time setting up the vm, and bootstrapping Kubernetes.  You will see output like the following when done.
```
$ sudo -E minikube start --vm-driver=none --extra-config=kubelet.resolv-conf=/var/run/systemd/resolve/resolv.conf
😄  minikube v0.34.1 on linux (amd64)
🤹  Configuring local host environment ...

⚠️  The 'none' driver provides limited isolation and may reduce system security and reliability.
⚠️  For more information, see:
👉  https://github.com/kubernetes/minikube/blob/master/docs/vmdriver-none.md

⚠️  kubectl and minikube configuration will be stored in /home/ubuntu
⚠️  To use kubectl or minikube commands as your own user, you may
⚠️  need to relocate them. For example, to overwrite your own settings:

    ▪ sudo mv /home/ubuntu/.kube /home/ubuntu/.minikube $HOME
    ▪ sudo chown -R $USER /home/ubuntu/.kube /home/ubuntu/.minikube

💡  This can also be done automatically by setting the env var CHANGE_MINIKUBE_NONE_USER=true
🔥  Creating none VM (CPUs=2, Memory=2048MB, Disk=20000MB) ...
📶  "minikube" IP address is 192.168.86.29
🐳  Configuring Docker as the container runtime ...
✨  Preparing Kubernetes environment ...
    ▪ kubelet.resolv-conf=/var/run/systemd/resolve/resolv.conf
🚜  Pulling images required by Kubernetes v1.13.3 ...
🚀  Launching Kubernetes v1.13.3 using kubeadm ...
🔑  Configuring cluster permissions ...
🤔  Verifying component health .....
💗  kubectl is now configured to use "minikube"
🏄  Done! Thank you for using minikube!
```
The `--extra-config=kubelet.resolv-conf=/var/run/systemd/resolve/resolv.conf` flag is to deal with the coredns and loopback problems - you may not need this depending on your local setup.

Now fixup your permissions:
```
sudo chown -R ${USER} /home/${USER}/.minikube
sudo chgrp -R ${USER} /home/${USER}/.minikube
sudo chown -R ${USER} /home/${USER}/.kube
sudo chgrp -R ${USER} /home/${USER}/.kube
```

Once completed, minikube will also update your kubectl settings to include the context `current-context: minikube` in `~/.kube/config`.  Test that connectivity works with something like:
```
$ kubectl get pods -n kube-system
NAME                               READY   STATUS    RESTARTS   AGE
coredns-86c58d9df4-5ztg8           1/1     Running   0          3m24s
...
```

Helm Chart
----------

The Helm Chart based install of the SKA TANGO-controls docker images relies on [Helm](https://docs.helm.sh/using_helm/#installing-helm) (surprise!).  The easiest way to install is using the install script:
```
curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | bash
```

Cleaning Up
-----------

Note on cleaning up:
```
minikube stop # stop minikube - this can be restarted with minikube start
minikube delete # destroy minikube - totally gone!
rm -rf ~/.kube # local minikube configuration cache
# remove all other minikube related installation files
sudo rm -rf /var/lib/kubeadm.yaml /data/minikube /var/lib/minikube /var/lib/kubelet /etc/kubernetes
```

Running the SKA TANGO-controls docker images on Kubernetes
----------------------------------------

Note: your Xserver needs to allow TCP connections.  This will be different for each window manager, but on Ubuntu 18.04 using gdm3 it can be enabled by editing /etc/gdm3/custom.conf and adding:
```
[security]
DisallowTCP=false
```
In order for these changes to take effect you will need to restart X (it's just easier to reboot...).

Change the file /etc/kubernetes/addons/ingress-dp.yaml in order to set the nginx-ingress-controller to version 0.24.0:
```
...
      containers:
      - image: quay.io/kubernetes-ingress-controller/nginx-ingress-controller:0.24.0
....
```

Once the Helm client is installed (from above) and TCP based Xserver connections are enabled, change to the k8s/ directory.  The basic configuration for each component of the SKA TANGO-controls docker images is held in the `values.yaml` file.

The mode that we are using Helm in here is purely for templating - this avoids the need to install the Tiller process on the Kubernetes cluster, and we don't need to be concerend about making it secure (requires TLS and the setup of a CA).

On for the main event - we launch the SKA TANGO-controls docker images with:
```
$ make deploy KUBE_NAMESPACE=integration
```

This will give extensive output describing what has been deployed in the test namespace:
```
kubectl describe namespace integration || kubectl create namespace integration
Name:         integration
Labels:       <none>
Annotations:  <none>
Status:       Active

No resource quota.

No resource limits.
persistentvolume/pogo-ska-docker-k8s created
persistentvolumeclaim/pogo-ska-docker-k8s created
persistentvolume/tangodb-ska-docker-k8s-test created
persistentvolumeclaim/tangodb-ska-docker-k8s-test created
service/databaseds-ska-docker-k8s-test created
statefulset.apps/databaseds-ska-docker-k8s-test created
service/tangodb-ska-docker-k8s-test created
statefulset.apps/tangodb-ska-docker-k8s-test created
pod/jive-ska-docker-k8s-test created
pod/logviewer-ska-docker-k8s-test created
pod/pogo-ska-docker-k8s created
pod/tangotest-ska-docker-k8s-test created
```

Please wait patiently - it will take time for the Container images to download, and for the database to initialise.  After some time, you can check what is running with:
```
watch kubectl get all,pv,pvc,ingress -n integration
```

Which will give output like:
```
Every 2.0s: kubectl get all,pv,pvc -n integration           osboxes: Fri Mar 29 09:25:05 2019

NAME                                   READY   STATUS      RESTARTS   AGE
pod/databaseds-ska-docker-k8s-test-0   0/1     Completed   1          27s
pod/jive-ska-docker-k8s-test           1/1     Running     0          27s
pod/logviewer-ska-docker-k8s-test      1/1     Running     0          27s
pod/pogo-ska-docker-k8s                0/1     Error       1          27s
pod/tangodb-ska-docker-k8s-test-0      1/1     Running     0          27s
pod/tangotest-ska-docker-k8s-test      1/1     Running     0          27s

NAME                                     TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)     AGE
service/databaseds-ska-docker-k8s-test   ClusterIP   None         <none>        10000/TCP   27s
service/tangodb-ska-docker-k8s-test      ClusterIP   None         <none>        3306/TCP    27s

NAME                                              READY   AGE
statefulset.apps/databaseds-ska-docker-k8s-test   0/1     27s
statefulset.apps/tangodb-ska-docker-k8s-test      1/1     27s

NAME                                           CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                                     STORAGECLASS   REASON   AGE
persistentvolume/pogo-ska-docker-k8s           1Gi        RWO            Retain           Bound    integration/pogo-ska-docker-k8s           standard                27s
persistentvolume/tangodb-ska-docker-k8s-test   1Gi        RWO            Retain           Bound    integration/tangodb-ska-docker-k8s-test   standard                27s

NAME                                                STATUS   VOLUME                        CAPACITY   ACCESS MODES   STORAGECLASS   AGE
persistentvolumeclaim/pogo-ska-docker-k8s           Bound    pogo-ska-docker-k8s           1Gi        RWO            standard       27s
persistentvolumeclaim/tangodb-ska-docker-k8s-test   Bound    tangodb-ska-docker-k8s-test   1Gi        RWO            standard       27s
```

To clean up the Helm Chart release:
```
$make delete KUBE_NAMESPACE=integration
```

# Install Kubernetes with Docker Desktop

Note: Depending on the order you install Docker Desktop and Kubectl from Homebrew, this may install a symlink `/usr/local/bin/kubectl` pointing to `/usr/local/bin/kubectl.docker`. This will conflict with the `kubectl` installed by homebrew, so you may have to force Homebrew to overwrite this symlink to use the Homebrew version of kubectl.

## Instructions

1. Go to [https://www.docker.com/products/docker-desktop] and follow the instructions that match your machine's operating system.
2. Once installation is complete, start Docker Desktop.
3. For MacOSX, Go to settings in menu bar, and choose Preferences. This will open the Docker Desktop GUI application.
4. Select the Kubernetes section on the left-hand side of the page.
5. Check the check-box next to "Enable Kubernetes"
6. Click "Apply & Restart"

## Test Installation

`kubectl version`
```
$ kubectl version
Client Version: version.Info{Major:"1", Minor:"21", GitVersion:"v1.21.1", GitCommit:"5e58841cce77d4bc13713ad2b91fa0d961e69192", GitTreeState:"clean", BuildDate:"2021-05-12T14:11:29Z", GoVersion:"go1.16.3", Compiler:"gc", Platform:"darwin/amd64"}
Server Version: version.Info{Major:"1", Minor:"19", GitVersion:"v1.19.7", GitCommit:"1dd5338295409edcfff11505e7bb246f0d325d15", GitTreeState:"clean", BuildDate:"2021-01-13T13:15:20Z", GoVersion:"go1.15.5", Compiler:"gc", Platform:"linux/amd64"}
```

`kubectl config get-contexts`
```
$ kubectl config get-contexts
CURRENT   NAME             CLUSTER          AUTHINFO         NAMESPACE
*         docker-desktop   docker-desktop   docker-desktop  
```
If the current context is set to something other than `docker-desktop` run: `kubectl config use-context docker-desktop`

`kubectl get nodes -o wide`
```
$ kubectl get nodes -o wide
NAME             STATUS   ROLES    AGE   VERSION   INTERNAL-IP    EXTERNAL-IP   OS-IMAGE         KERNEL-VERSION     CONTAINER-RUNTIME
docker-desktop   Ready    master   75d   v1.19.7   192.168.65.4   <none>        Docker Desktop   5.10.25-linuxkit   docker://20.10.6
```

`kubectl get pods --all-namespaces -o wide`
```
$ kubectl get pods --all-namespaces -o wide
NAMESPACE     NAME                                     READY   STATUS    RESTARTS   AGE   IP             NODE             NOMINATED NODE   READINESS GATES
kube-system   coredns-f9fd979d6-8wt96                  1/1     Running   0          75d   10.1.0.8       docker-desktop   <none>           <none>
kube-system   coredns-f9fd979d6-rnph7                  1/1     Running   0          75d   10.1.0.9       docker-desktop   <none>           <none>
kube-system   etcd-docker-desktop                      1/1     Running   0          75d   192.168.65.4   docker-desktop   <none>           <none>
kube-system   kube-apiserver-docker-desktop            1/1     Running   0          75d   192.168.65.4   docker-desktop   <none>           <none>
kube-system   kube-controller-manager-docker-desktop   1/1     Running   0          75d   192.168.65.4   docker-desktop   <none>           <none>
kube-system   kube-proxy-q6q76                         1/1     Running   0          75d   192.168.65.4   docker-desktop   <none>           <none>
kube-system   kube-scheduler-docker-desktop            1/1     Running   0          75d   192.168.65.4   docker-desktop   <none>           <none>
kube-system   storage-provisioner                      1/1     Running   1          75d   10.1.0.6       docker-desktop   <none>           <none>
kube-system   vpnkit-controller                        1/1     Running   0          75d   10.1.0.7       docker-desktop   <none>           <none>
```
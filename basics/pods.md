# Pods

## Hello World

Create Simple Pod of a Image:
```
kubectl run hello-world-pod --image=gcr.io/google-samples/hello-app:1.0
```

Get all pods in default namespace:
```
$ kubectl get pods
NAME              READY   STATUS    RESTARTS   AGE
hello-world-pod   1/1     Running   0          59s
```

Describe the pod
```
$ kubectl describe pod/hello-world-pod
Name:         hello-world-pod
Namespace:    default
Priority:     0
Node:         docker-desktop/192.168.65.4
Start Time:   Mon, 16 Aug 2021 22:25:49 -0700
Labels:       run=hello-world-pod
Annotations:  <none>
Status:       Running
IP:           10.1.0.12
IPs:
  IP:  10.1.0.12
Containers:
  hello-world-pod:
    Container ID:   docker://5e20c72f5a2ee52521a9e837ac73ab4e94672d0febc0aab83b792cd29c5f83af
    Image:          gcr.io/google-samples/hello-app:1.0
    Image ID:       docker-pullable://gcr.io/google-samples/hello-app@sha256:60699bc165368192d6c7295b3f837a996a94812d36ef6e7feb2f9c77a558f813
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Mon, 16 Aug 2021 22:25:55 -0700
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-fzh9c (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  default-token-fzh9c:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-fzh9c
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  <none>
Tolerations:     node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  5m21s  default-scheduler  Successfully assigned default/hello-world-pod to docker-desktop
  Normal  Pulling    5m18s  kubelet            Pulling image "gcr.io/google-samples/hello-app:1.0"
  Normal  Pulled     5m16s  kubelet            Successfully pulled image "gcr.io/google-samples/hello-app:1.0" in 2.2994975s
  Normal  Created    5m16s  kubelet            Created container hello-world-pod
  Normal  Started    5m15s  kubelet            Started container hello-world-pod
```

Get a shell on the pod:
```
$ kubectl exec -ti hello-world-pod -c hello-world-pod -- /bin/sh
/ # 
```

Get the logs of the pod:
```
$ kubectl logs hello-world-pod
2021/08/17 05:25:55 Server listening on port 8080
```

Edit the pod resource in a text editor:
```
$ kubectl edit pod/hello-world-pod
pod/hello-world-pod edited
```

Delete the pod
```
$ kubectl delete pod/hello-world-pod
pod "hello-world-pod" deleted
```
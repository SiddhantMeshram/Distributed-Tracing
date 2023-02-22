This repo contains code regarding a sample python programme deployed in Microk8s environment and using Istio-Jaeger for tracing.

All the steps performed in this experiment:

1. Install Microk8s in Ubuntu environment:
    
    https://microk8s.io/docs/getting-started
	
2. Enable Istio in Microk8s.
    
    https://istio.io/latest/docs/setup/platform-setup/microk8s/

3. Use the docker file to build the docker image.

    sudo docker build . -t hello-web

4. Import the image into MicroK8s registry.

    sudo microk8s.enable registry

5. Save the image to a tar file.

    docker save hello-web > hello-web.tar

6. Import image into K8s registry.

    sudo microk8s.ctr image import hello-web.tar
 

7.  Run the following docker command to tag the image. This is required to be able to push images to external registries.

    sudo docker build . -t localhost:32000/app:ne

8. This image can be pushed to the k8s registry as follows

    sudo docker push localhost:32000/hello-web

9. Create a K8s deployment.

    sudo microk8s.kubectl apply -f depl.yaml

10. Expose the web service running at port 8080 through a NodePort.

    sudo microk8s.kubectl expose deployment hello-deployment --type=NodePort --name=hello-service

11. Enable Jaeger dashboard.

    sudo microk8s.istioctl dashboard jaeger&

12. You can filter the service and find the traces for the service.

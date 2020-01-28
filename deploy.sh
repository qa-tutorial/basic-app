#kubectl delete -f kubernetes/basic-app.yaml
kubectl set image deployment/basic-app basic-app=kubes-jenkins:5000/server:latest --record
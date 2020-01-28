#kubectl delete -f kubernetes/basic-app.yaml
kubectl set image deplotment/basic-app server=kubes-jenkins:5000/server:latest --record
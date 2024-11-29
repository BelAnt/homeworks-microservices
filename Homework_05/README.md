# Prometheus. Grafana

## Установка
```
https://chocolatey.org/install
https://kubernetes.io/ru/docs/tasks/tools/install-minikube/
https://helm.sh/docs/intro/install/
```

## Подготовительные шаги
```
minikube start
minikube addons enable ingress
docker build -t belant/users . 
docker tag belant/users belokrilov/users:v2
docker push belokrilov/users:v2  
```

## Запуск приложения

Манифесты k8s - [./kube](./kube/)

Параметры запуска PostgreSQL со скриптом инициализации - [./helm/pg-values.yaml](./helm/pg-values.yaml)

```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install k8s-pg oci://registry-1.docker.io/bitnamicharts/postgresql -f ./helm/pg-values.yaml
helm install prometheus-stack prometheus-community/kube-prometheus-stack
helm upgrade --install nginx ingress-nginx/ingress-nginx --set controller.service.externalIPs="{192.168.49.2}" --set controller.metrics.enabled=true --set controller.metrics.serviceMonitor.enabled=true --set controller.metrics.serviceMonitor.additionalLabels.release=prometheus-stack

kubectl port-forward prometheus-prometheus-stack-kube-prom-prometheus-0 9090
$env:GRAFANA_POD_NAME=$(kubectl get pods -l "app.kubernetes.io/name=grafana" -o jsonpath="{.items[0].metadata.name}")
kubectl port-forward $env:GRAFANA_POD_NAME 3000

cd .\kube\
kubectl apply -f .
minikube tunnel
```

## Результат запуска тестов

Применяемая Postman коллекция - [./postman/User REST API (CRUD).postman_collection.json](./postman/User%20REST%20API%20(CRUD).postman_collection.json)

![Results](postman/results.png?raw=true "Results")
# Работа с Helm-ом

## Установка
```
https://chocolatey.org/install
https://kubernetes.io/ru/docs/tasks/tools/install-minikube/
https://helm.sh/docs/intro/install/
```

## Запуск Minikube
```
minikube start
minikube addons enable ingress
```

## Запуск приложения

Манифесты k8s - [./kube](./kube/)

Параметры запуска PostgreSQL со скриптом инициализации - [./helm/pg-values.yaml](./helm/pg-values.yaml)

```
helm install k8s-pg oci://registry-1.docker.io/bitnamicharts/postgresql -f ./helm/pg-values.yaml
cd .\kube\
kubectl apply -f .
minikube tunnel
```

## Результат запуска тестов

Применяемая Postman коллекция - [./postman/User REST API (CRUD).postman_collection.json](./postman/User%20REST%20API%20(CRUD).postman_collection.json)

![Results](postman/results.png?raw=true "Results")
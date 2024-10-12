# Основы работы с Docker 
```
docker build -t belant/fasthealth .
docker run -d --name fasthealth -p 8000:8000 belant/fasthealth

docker login
docker tag belant/fasthealth belokrilov/belant:fasthealth
docker push belokrilov/belant:fasthealth
```
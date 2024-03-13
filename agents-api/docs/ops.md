# project operations

## Packages

pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support

## Dev environment 

1.**Build the docker Images**

```shell
pip freeze > requirements.txt
```

```shell
docker build -f docker/dev/Dockerfile.dev -t agents-api:dev .
```
1.**Build the Docker containers**

```shell
docker compose -f docker/dev/docker-compose.dev.yml build
```

1.**Run the Docker containers**
```shell
docker compose -f docker/dev/docker-compose.dev.yml up
```

1.**Create migrations**

```shell
docker compose -f docker/dev/docker-compose.dev.yml run web python manage.py makemigrations
```
1.**Apply migrations**
```shell
docker compose -f docker/dev/docker-compose.dev.yml run web python manage.py migrate
```

## Docker

### Remove all images
```shell
docker rmi -f $(docker images -aq)
```

### Remove Container Prune
```shell
docker container prune
```


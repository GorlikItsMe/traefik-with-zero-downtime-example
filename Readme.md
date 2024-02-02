# How to deploy without downtime with Docker and Traefik

## Reqiurements

- docker
- Traefik
- docker-compose
- <https://github.com/Wowu/docker-rollout>

## How to?

1. Dockerfile should contain `HEALTHCHECK` instruction
2. To update your container without downtime run this:

```bash
docker rollout -f docker-compose.yml flask_app -t 30
```

flask_app is the name of container in `docker-compose.yml`

## Why it dont work

- Your service cannot have `container_name` and `ports` defined in `docker-compose.yml`, as it's not possible to run multiple containers with the same name or port mapping. Use a proxy as described below.
- Proxy like Traefik or nginx-proxy is required to route traffic.
- Each deployment will increment the index in container name (e.g. project-web-1 -> project-web-2).
- You can only redeploy containers that have a `HEALTHCHECK` instruction in their Dockerfile. (If not, it will just kill old container and start new one)
- You can only redeploy one container at a time. (If you have multiple containers in `docker-compose.yml` you have to redeploy them one by one)

## Snippets

```bash
docker compose up -d --scale flask_app=2
```

```bash
docker rollout -f docker-compose.yml flask_app
docker rollout -f docker-compose.yml flask_app -t 30
```

docker compose build
# https://github.com/Wowu/docker-rollout
docker rollout -f docker-compose.yml flask_app -t 30
